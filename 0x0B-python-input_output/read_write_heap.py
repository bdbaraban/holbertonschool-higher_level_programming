#!/usr/bin/python3
# read_write_heap.py
# Brennan D Baraban <375@holbertonschool.com>
"""Find and replace a string in the heap of a running process.

Usage: `read_write_heap.py pid search_string replace_string`
Where:
    - pid is the PID of the running process
    - strings are represented in ASCII.
"""
import sys


if len(sys.argv) != 4:
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

pid = sys.argv[1]
search_string = sys.argv[2]
replace_string = sys.argv[3] + "\0"

print("Hacking a VM, eh? So you like to live dangerously... ")

print("  <> Searching for PID heap {}... ".format(pid), end="")
address = ""
maps_path = "/proc/" + pid + "/maps"
try:
    with open(maps_path, "r") as maps_file:
        for line in maps_file:
            if "[heap]" in line:
                print("the heap has been located.")

                if "r" not in line or "w" not in line:
                    print("  [ERROR] PID heap lacks read/write permissions")
                    sys.exit(0)

                line = line.split()
                print("    >< pathname: {}".format(maps_path))
                print("    >< address: {}".format(line[0]))
                print("    >< permissions: {}".format(line[1]))
                print("    >< offset: {}".format(line[2]))
                print("    >< device: {}".format(line[3]))
                print("    >< inode: {}".format(line[4]))
                address = line[0].split('-')

except IOError as e:
    print("  [ERROR] cannot open file {}".format(maps_path))
    print(e)
    sys.exit(1)

start = int(address[0], 16)
end = int(address[1], 16)

print("  <> Searching for string {}... ".format(search_string), end="")
mem_path = "/proc/" + pid + "/mem"
try:
    with open(mem_path, "rb+") as mem_file:
        mem_file.seek(start)
        heap = mem_file.read(end - start)

        try:
            index = heap.index(search_string.encode("ASCII"))
            print("the string has been located.")
            print("    >< index: {}".format(index))
        except Exception as e:
            print("  [ERROR] cannot locate string {}".format(search_string))
            print(e)
            sys.exit(0)

        print("  <> Replacing string {} ".format(search_string), end="")
        print("with {}... ".format(replace_string[:-1]), end="")
        mem_file.seek(start + index)
        mem_file.write(replace_string.encode("ASCII"))
        print("the string has been replaced.")

except IOError:
    print("  [ERROR] cannot write to file {}".format(mem_path))
    sys.exit(1)

print("Happy hacking, hacker!")
