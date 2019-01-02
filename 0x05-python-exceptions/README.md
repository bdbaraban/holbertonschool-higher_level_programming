# 0x05. Python - Exceptions

In this project, I learned handling errors and exceptions in Python with `try` 
and `except`.

## Function Prototypes
Prototypes for functions written in this project:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |

## Tasks
* **Safe list printing**
  * `0-safe_print_list.py`: Prints `x` elements of a list on the same line, 
followed by a new line.
  * The parameter `x` represents the number of elements to print - can be 
bigger than the length of `my_list`.
  * Returns the real number of elements printed.
  * Without importing modules or using `len()`.

* **Safe printing of an integers list**
  * `1-safe_print_integer.py`: Prints an integer with `"{:d}".format()`.
  * The parameter `value` can be any type.
  * Returns `True` if `value` was printed correctly (ie. was an integer), 
`False` otherwise.
  * Without importing modules or using `type()`.

* **Print and count integers**
  * `2-safe_print_list_integers.py`: Prints the first `x` elements of a list 
that are integers on the same line, followed by a new line.
  * The parameter `my_list` can contain any type.
  * The parameter `x` represents the number of elements to print - can be 
bigger than the length of `my_list`.
  * Reutnrs the real number of integers printed.
  * Without importing modules or using `len()`.

* **Integers division with debug**
  * `3-safe_print_division.py`: Divides two integers and prints the result 
using `finally:`.
  * The function assumes that the arguments are integers.
  * Upon success, returns the value of the division; otherwise - returns `None`.
  * Without importing modules.


* **Divide a list**
  * `4-list_division.py`: Divides two lists element by element. 
  * Returns a new list of length `list_length` with all divisions.
  * The lists `my_list_1` and `my_list_2` can contain any type.
  * The parameter `list_length` can be larger than the lengths of either list.
  * If an element is not an integer or float, the function prints `wrong type`.
  * If the division cannot be done, the result of the division is `0` and the 
function prints: `division by 0`.
  * If either of `my_list_1` or `my_list_2` are too short, the function prints: 
`out of range`.
  * Without importing modules.

* **Raise exception**
  * `5-raise_exception.py`: Raises a type exception.
  * Without importing modules.

* **Raise a message**
  * `6-raise_exception_msg.py`: Raises a name exception with a message.
  * Without importing modules.
