#!/usr/bin/python3
MyClass = __import__('10-my_class').MyClass
class_to_json = __import__('10-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
