# Javascript - Objects, Scopes and Closures

In this second Holberton JavaScript project I dived into the infamously fun
aspects of the language - scope, closures and `this`. I practiced working with
objects and ES6-style classes.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File               | Prototype                                               |
| ------------------ | ------------------------------------------------------- |
| `7-occurrences.js` | `exports.nbOccurences = function (list, searchElement)` |
| `8-esrever.js`     | `exports.esrever = function (list)`                     |
| `9-logme.js`       | `exports.logMe = function (item)`                       |
| `10-converter.js`  | `exports.converter = function (base)`                   |


## Tasks :page_with_curl:

* **0. Rectangle #0**
  * [0-rectangle.js](./0-rectangle.js): JavaScript script that defines an empty
  class `Rectangle`.

* **1. Rectangle #1**
  * [1-rectangle.js](./1-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [0-rectangle.js](./0-rectangle.js) with:
    * Constructor that initializes instance attributes `width` and `height` with
    given parameters `w` and `h`.

* **2. Rectangle #2**
  * [2-rectangle.js](./2-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [1-rectangle.js](./1-rectangle.js) with:
    * If provided `w` and `h` are less than or equal to `0`, creates an empty object.

* **3. Rectangle #3**
  * [3-rectangle.js](./3-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [3-rectangle.js](./3-rectangle.js) with:
    * Instance method `print()` that prints the rectangle using the `X` character.

* **4. Rectangle #4**
  * [4-rectangle.js](./4-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [4-rectangle.js](./4-rectangle.js) with:
    * Instance method `rotate()` that swaps the `width` and `height` of the `Rectangle`.
    * Instance method `double()` that multiplies the `width` and `height` of the
    `Rectangle` by `2`.

* **5. Square #0**
  * [5-square.js](./5-square.js): JavaScript script that defines a class `Square`
  that inherits from `Rectangle`.
    * Constructor takes one argument `size`.

* **6. Square #1**
  * [6-square.js](./6-square.js): JavaScript script that defines a class `Square`
  that inherits from `Rectangle`. Builds on [5-square.js](./5-square.js) with:
    * Instance method `charPrint(c)` that prints the `Square` using the character
    `c`.
    * If `c` is `undefined`, uses the character `X`.

* **7. Occurrences**
  * [7-occurrences.js](./7-occurrences.js): JavaScript function that returns the
  number of occurrences in a list.

* **8. Esrever**
  * [8-esrever.js](./8-esrever.js): JavaScript function that reverses a list.

* **9. Log me**
  * [9-logme.js](./9-logme.js): JavaScript function that prints the number of
  arguments already printed as well as the new argument value.
  * Output: `<number arguments already printed>: <current argument value>`

* **10. Number conversion**
  * [10-converter.js](./10-converter.js): JavaScript function that converts a number
  from base 10 to another base passed as argument.

* **11. Factor index**
  * [100-map.js](./100-map.js): JavaScript script that imports an array and creates
  a new array with each value equal to the value of initial list times the index of
  the new list.
  * Prints both the initial and new list.

* **12. Sorted occurences**
  * [101-sorted.js](./101-sorted.js): JavaScript script that imports a dictionary
  of occurrences by user ID and computes a new dictionary of user ID's by occurrences.
  * Prints the new dictionary.

* **13. Concat files**
  * [102-concat.js](./102-concat.js): JavaScript script that concatenates two files
  passed as arguments into a file specifed as the third argument.
  * Usage: `./102-concat.js fileA fileB fileC`.
