# Python - Everything is object

In this project, I studied object instantiation in Python, delving into 
variable aliasing and object identifiers, types, and mutability. The project 
involved a series of quiz-like questions the answers to which I provided in 
single-line `.txt` files.

## Tasks
* **Who am I?**
  * `0-answer.txt`: What function would you use to print the type of an object?


* **Where are you?**
  * `1-answer.txt`: How do you get a variable's identifier 
(which is the memory address in the CPython implementation)?

* **Right count**
  * `2-answer.txt`: In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 100
```

* **Right count =**
  * `3-answer.txt`: In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 89
```

* **Right count =**
  * `4-answer.txt`: In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a
```

* **Right count =+**
  * `5-answer.txt`: In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a + 1
```

* **Is equal**
  * `6-answer.txt`: What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```

* **Is the same**
  * `7-answer.txt`: What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```

* **Is really equal**
  * `8-answer.txt`: What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

* **Is really the same**
  * `9-answer.txt`: What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

* **And with a list, is it equal**
  * `10-answer.txt`: What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```

* **And with a list, is it the same**
  * `11-answer.txt`: What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```

* **And with a list, is it really equal**
  * `12-answer.txt`: What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

* **And with a list, is it really the same**
  * `13-answer.txt`: What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

* **List append**
  * `14-answer.txt`: What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

* **List add**
  * `15-answer.txt`: What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

* **Integer incrementation**
  * `16-answer.txt`: What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

* **List incrementation**
  * `17-answer.txt`: What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

* **List assignation**
  * `18-answer.txt`: What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

* **Copy a list object**
  * `19-copy_list.py`: Python function `def copy_list(l):` that returns 
a copy of a list.

* **Tuple or not?**
  * `20-answer.txt`: Is `a` a tuple?
```
a = ()
```

* **Tuple or not?**
 * `21-answer.txt`: Is `a` a tuple?
```
a = (1, 2)
```

* **Tuple or not?**
  * `22-answer.txt`: Is `a` a tuple?
```
a = (1)
```

* **Tuple or not?**
  * `23-answer.txt`: Is `a` a tuple?
```
a = (1, )
```

* **Richard Sim's special #0**
  * `24-answer.txt`: What does this script print?
```
a = (1)
b = (1)
a is b
```

* **Richard Sim's special #1**
  * `25-answer.txt`: What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```

* **Richard Sim's special #2**
  * `26-answer.txt`: What does this script print?
```
a = ()
b = ()
a is b
```

* **Richard Sim's special #3**
  * `27-answer.txt`: Will the last line of this script print `139926795932424`?
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

* **Richard Sim's special #4**
  * `28-answer.txt`: Will the last line of this script print `139926795932424`?
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

* **#pythonic**
  * `100-magic_string.py`: Python function `magic_string()` that returns the 
string `"Holberton"` n times the number of iteration.

* **Low memory cost**
  * `101-locked_class.py`: Python class `LockedClass` with no attributes that 
prevents the user from dynamically creating any new instance attributes not 
called `first_name`.

* **int 1/3**
  * `103-line1.txt`: How many `int` objects are created by the execution 
of the first line in this script?
  * `104-line2.txt`: How many `int` objects are created by the execution 
of the second line in this script?
```
a = 1
b = 1
``` 

* **int 2/3**
  * `104-line1.txt`: How many `int` objects are created by the execution 
of the first line in this script?
  * `104-line2.txt`: How many `int` objects are created by the execution 
of the second line in this script?
  * `104-line3.txt`: After the execution of line 3, is the `int` object pointed 
to by `a` deleted?
  * `104-line4.txt`: After the execution of line 4, is the `int` object pointed 
to by `b` deleted?
  * `104-line5.txt`: How many `int` objects are created by the execution 
of the last line in this script?
```
a = 1024
b = 1024
del a
del b
c = 1024
```

* **int 3/3**
  * `105-line1.txt`: Before the execution of line 2 in this script, how many 
`int` objects have been created and are still in memory?
```
print("I")
print("Love")
print("Python")
```

* **Clear strings**
  * `106-line1.txt`: How many `str` objects are created by the execution 
of the first line in this script?
  * `106-line2.txt`: How many `str` objects are created by the execution 
of the second line in this script?
  * `106-line3.txt`: After the execution of line 3, is the `str` object pointed 
to by `a` deleted?
  * `106-line4.txt`: After the execution of line 4, is the `str` object pointed 
to by `b` deleted?
  * `106-line5.txt`: How many `str` objects are created by the execution 
of the last line in this script?
```
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
