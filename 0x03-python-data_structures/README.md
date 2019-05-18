# Python - Data Structures: Lists, Tuples

In this project, I learned about how sequence data types work in
Python - specifically, lists and tuples.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                               | Prototype                                      |
| ---------------------------------- | ---------------------------------------------- |
| `0-print_list_integer.py`          | `def print_list_integer(my_list=[]):`          |
| `1-element_at.py`                  | `def element_at(my_list, idx):`                |
| `2-replace_in_list.py`             | `def replace_in_list(my_list, idx, element):`  |
| `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):` |
| `4-new_in_list.py`                 | `def new_in_list(my_list, idx, element):`      |
| `5-no_c.py`                        | `def no_c(my_string):`                         |
| `6-print_matrix_integer.py`        | `def print_matrix_integer(matrix=[[]]):`       |
| `7-add_tuple.py`                   | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| `8-multiple_returns.py`            | `def multiple_returns(sentence):`              |
| `9-max_integer.py`                 | `def max_integer(my_list=[]):`                 |
| `10-divisible_by_2.py`             | `def divisible_by_2(my_list=[]):`              |
| `11-delete_at.py`                  | `def delete_at(my_list=[], idx=0):`            |
| `100-print_python_list_info.c`     | `void print_python_list_info(PyObject *p);`    |

## Tasks :page_with_curl:

* **0. Print a list of integers**
  * [0-print_list_integer.py](./0-print_list_integer.py): Python function that prints all
  integers of a list, one per line.
  * Without importing modules or casting integers into strings.

* **1. Secure access to an element in a list**
  * [1-element_at.py](./1-element_at.py): Python function that retrieves an element
  from a list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns `None`.
  * Without import modules or using `try/except`.

* **2. Replace element**
  * [2-replace_in_list.py](./2-replace_in_list.py): Python function that replaces an element
  of a list at a specific position.
  * If `idx` is negative or out of range (greater than the number of elements
  in `my_list`), the function returns the original list.
  * Without importing modules or using `try/except`.

* **3. Print a list of integers... in reverse!**
  * [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py): Python
  function that prints all integers of a list, one per line, in reverse order.
  * Without importing modules or casting integers into strings.

* **4. Replace in a copy**
  * [4-new_in_list.py](./4-new_in_list.py): Python function that replaces an element of a
  list at a specific position without modifying the original list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns the original list.
  * Without importing modules or using `try/except`.

* **5. Can you C me now?**
  * [5-no_c.py](./5-no_c.py): Python function that removes all characters `c`
  and `C` from a string and returns the string.
  * Without importing modules or using `str.replace()`.

* **6. Lists of lists = Matrix**
  * [6-print_matrix_integer.py](./6-print_matrix_integer.py): Python function that prints
  a matrix of integers, one row per line.
  * Without casting integers into strings.

* **7. Tuples addition**
  * [7-add_tuple.py](./7-add_tuple.py): Python function that adds two tuples.
  * Returns a tuple with two integers:
    * The first element is the addition of the first element of each argument.
    * The second element is the addition of the second element of each argument.
  * If a tuple is smaller than 2, the value `0` is used for the missing integer.
  * If a tuple is larger than 2, only the first two integers are used.
  * Without importing modules.

* **8. More returns!**
  * [8-multiple_returns.py](./8-multiple_returns.py): Python function that returns a
  tuple with the length of a string and its first character.
  * If the string is empty, the first character should equal `None`.
  * Without importing modules.

* **9. Find the max**
  * [9-max_integer.py](./9-max_integer.py): Python function that finds the biggest integer
  of a list.
  * If the list is empty, the function returns `None`.
  * Without importing modules or using the builtin `max()`.

* **10. Only by 2**
  * [10-divisible_by_2.py](./10-divisible_by_2.py): Python function that finds all multiples
  of 2 in a list.  * Returns a new list of the same size. Each element of the new
  list contains either `True` or `False` corresponding to whether the integer at
  the same position in the original list is a multiple of 2.
  * Without importing modules.

* **11. Delete at**
  * [11-delete_at.py](./11-delete_at.py): Python function that deletes an item at
  a specific position in a list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns the original list.
  * Without imporitng modules or using `pop()`.

* **12. Switch**
  * [12-switch.py](./12-switch.py): Python program that switches the values of
  variable `a` and `b`.
  * Completion of [this source code](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py).

* **13. Linked list palindrome**
  * [13-is_palindrome.c](./13-is_palindrome.c): C function that checks if a
  singly-linked list is a palindrome.
  * If the function is not a palindrome - returns `0`.
  * If the function is a palindrome - returns `1`.
  * An empty list is considered a palindrome.
  * Helper files:
    * [linked_lists.c](./linked_lists.c): C functions handling linked lists for
    testing [13-is_palindrome.c](./13-is_palindrome.c) (provided by Holberton School).
    * [lists.h](./lists.h): Header file containing definitions and prototypes for all types
    and functions used in [linked_lists.c](./linked_lists.c) and
    [13-insert_number.c](./13-insert_number.c).

* **14. CPython #0: Python lists**
  * [100-print_python_list_info.c](./100-print_python_list_info.c): C function that
  prints basic information about Python lists.
