# Python - Exceptions

In this project, I learned handling errors and exceptions in Python with `try`
and `except`.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.

## Function Prototypes :floppy_disk:

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
| `100-safe_print_integer_err.py`  | `def safe_print_integer_err(value):`                    |
| `101-safe_function.py`           | `def safe_function(fct, *args):`                        |
| `102-magic_calculation.py`       | `def magic_calculation(a, b);`                          |
| `103-python.c`                   | <ul><li>`void print_python_list(PyObject *p);`</li><li>`void print_python_bytes(PyObject *p);`</li><li>`void print_python_float(PyObject *p);`</li></ul> |

## Tasks :page_with_curl:

* **0. Safe list printing**
  * [0-safe_print_list.py](./0-safe_print_list.py): Python function that prints `x` elements
  of a list on the same line, followed by a new line.
  * The parameter `x` represents the number of elements to print - can be
  bigger than the length of `my_list`.
  * Returns the real number of elements printed.
  * Without importing modules or using `len()`.

* **1. Safe printing of an integers list**
  * [1-safe_print_integer.py](./1-safe_print_integer.py): Python function that prints an integer in `"{:d}".format()` format.
  * The parameter `value` can be any type.
  * Returns `True` if `value` was printed correctly (ie. was an integer),
  `False` otherwise.
  * Without importing modules or using `type()`.

* **2. Print and count integers**
  * [2-safe_print_list_integers.py](./2-safe_print_list_integers.py): Python function that prints the first `x` elements of a list that are integers on the same line, followed by a new line.
  * The parameter `my_list` can contain any type.
  * The parameter `x` represents the number of elements to print - can be
  bigger than the length of `my_list`.
  * Reutnrs the real number of integers printed.
  * Without importing modules or using `len()`.

* **3. Integers division with debug**
  * [3-safe_print_division.py](./3-safe_print_division.py): Python function that divides two integers and prints the result using `finally:`.
  * The function assumes that the arguments are integers.
  * Upon success, returns the value of the division; otherwise - returns `None`.
  * Without importing modules.

* **4. Divide a list**
  * [4-list_division.py](./4-list_division.py): Python function that divides two lists element by element.
  * Returns a new list of length `list_length` with all divisions.
  * The lists `my_list_1` and `my_list_2` can contain any type.
  * The parameter `list_length` can be larger than the lengths of either list.
  * If an element is not an integer or float, the function prints `wrong type`.
  * If the division cannot be done, the result of the division is `0` and the
  function prints: `division by 0`.
  * If either of `my_list_1` or `my_list_2` are too short, the function prints:
  `out of range`.
  * Without importing modules.

* **5. Raise exception**
  * [5-raise_exception.py](./5-raise_exception.py): Python function that raises
  a type exception.
  * Without importing modules.

* **6. Raise a message**
  * [6-raise_exception_msg.py](./6-raise_exception_msg.py): Python function that raises a
  name exception with a message.
  * Without importing modules.

* **7. Safe integer print with error message**
  * [100-safe_print_integer_err.py](./100-safe_print_integer_err.py): Python function that
  prints an integer with type-checking in `"{:d}".format())` format.
  * The paramter `value` can be any type.
  * Returns `True` if `value` was printed correctly (ie. was an integer).
  * Otherwise, prints an exception error to `stderr` and returns `False`.
  * Without importing modules.

* **8. Safe function**
  * [101-safe_function.py](./101-safe_function.py): Python function that executes
  a function safely.
  * The function assumes that the paramter `fct` is always a pointer to a function.
  * Upon success, returns the result of the function.
  * Otherwise, prints an en exception error to `stderr` and returns `None`.

* **9. ByteCode -> Python #4**
  * [102-magic_calculation.py](./102-magic_calculation.py): Python function matching exactly a
  bytecode provided by Holberton School.

* **10. CPython #2: PyFloatObject**
  * [103-python.c](./103-python.c): C functions that print basic information
  about Python lists, bytes, and float objects.
