# Python - Hello, World

In this project, I began practicing using the interpreter, printing text and variables, and indexing and slicing strings in Python.

## Helper Files
* `10-linked_lists.c`: C functions handling singly-linked lists for testing `10-check_cycle.c`.
  * Provided by Holberton School.

* `lists.h`: Header file containing definitions and prototypes for all types and functions written for file `10-check_cycle.c`.

| File/Type           | Definition/Prototype                                                                                                                                                         |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `struct listint_s`  | <ul><li>`int n`</li><li>`struct listint_s *next`</li></ul>                                                                                                                   |
| `typedef listint_t` | `struct listint_s`                                                                                                                                                           |
| `10-linked_lists.c` | <ul><li>`size_t print_listint(const listint_t *h);`</li><li>`listint_t *add_nodeint(listint_t **head, const int n);`</li><li>`void free_listint(listint_t *head);`</li></ul> |
| `10-check_cycle.c`  | `int check_cycle(listint_t *list);`                                                                                                                                          |

## Tasks
* **Run Python File**
  * `0-run`: Bash script that runs a Python script file saved in the environment variable `$PYFILE`.

* **Run inline**
  * `1-run_inline`: Bash script that runs Python code saved in the environment variable `$PYCODE`.

* **Hello, print**
  * `2-print.py`: Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line using the function `print`.

* **Print integer**
  * `3-print_number.py`: Python script that prints the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py).

* **Print float**
  * `4-print_float.py`: Python script that prints the float stored in the variable `number` with a precision of two digits.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py).

* **Print string**
  * `5-print_string.py`: Python script that prints a string stored in the variable `str` three times, then a new line, then the first nine characters contained in `str`, followed by another new line.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py).

* **Play with strings**
  * `6-concat.py`: Python script that prints `Welcome to Holberton School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py).

* **Copy - Cut - Paste**
  * `7-edges.py`: Python script that sets three string variables based on the string contained in the variable `word` as follows:
  * `word_first_3`: Contains the first three letters of the variable `word`.
  * `word_last_2`: Contains the last two letters of the variable `word`.
  * `middle_word`: Contains the value of the variable `word` without the first and last letters.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py).

* **Create a new sentence**
  * `8-concat_edges.py`: Python script that prints `object-oriented programming with Python`, followed by a new line without creating new variables or string literals.
  * Completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py).

* **Easter Egg**
  * `9-easter_egg.py`: Python script that prints "The Zen of Python" by Tim Peters, followed by a new line.

* **Linked list cycle**
  * `10-check_cycle.c`: C function that checks if a linked list contains a cycle.
  * Returns `0` if there is no cycle and `1` if there is.

* **Hello, write**
  * `100-write.py`: Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line to `stderr` using the function `write` from the `sys` module.
  * Exits with a status code of `1`.

* **Compile**
  * `101-compile`: Python script that compiles a Python script file stored in the environment variable `$PYFILE` and saves it to an output file `$PYFILEc` (ex. `export PYFILE=my_main.py` => output filename: `my_main.pyc`).
