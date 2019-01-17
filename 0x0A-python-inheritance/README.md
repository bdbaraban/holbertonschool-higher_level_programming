# Python - Inheritance

In this project, I learned about Python class inheritance. I learned about the 
differences between super- and sub-classes while practicing inheritance, 
definining classes with multiple base classes, and overiding inherited methods 
and attributes.

## Test Files
* `tests`: Folder containing the following test files:
    * `1-my_list.txt`
    * `7-base_geometry.txt`

## Function Prototypes
Prototypes for functions written in this project:

| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-lookup.py`           | `def lookup(obj):`                    |
| `2-is_same_class.py`    | `def is_same_class(obj, a_class):`    |
| `3-is_kind_of_class.py` | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py`    | `def inherits_from(obj, a_class):`    |
| `101-add_attribute.py`  | `def add_attribute(obj, att, value):` |

# Tasks
* **Lookup**
  * `0-lookup.py`: Python function that returns a list of available attributes 
and methods of an objects.

* **My list**
  * `1-my_list.py`: Python class `MyList` that inherits from `list`. Includes:
    * Public instance method `def print_sorted(self):` that prints the list in 
ascending sorted order (assumes all list elements are `int`s).

* **Exact same object**
  * `2-is_same_class.py`: Python function that returns `True` if an object is 
exactly an instance of a specified class; otherwise `False`.

* **Same class or inherit from**
  * `3-is_kind_of_class.py`: Python function that returns `True` if an object is 
an instance or inherited instance of a specified class; otherwise `False`.

* **Only sub class of**
  * `4-inherits_from.py`: Python function that returns `True` if an object is 
an inherited instance (either directly or indirectly) from a specified class; 
otherwise `False`.

* **Geometry module**
  * `5-base_geometry.py`: An empty Python class `BaseGeometry`.

* **Improve Geometry**
  * `6-base_geometry.py`: Python class `BaseGeometry`. Builds on 
`5-base_geometry.py` with:
    * Public instance method `def area(self):` that raises an `Exception` with 
the message `area() is not implemented`.

* **Integer validator**
  * `7-base_geometry.py`: Python class `BaseGeometry`. Builds on 
`6-base_geometry.py` with:
    * Public instance method `def integer_validator(self, name, value):` that 
validates the parameter `value`.
    * Assumes the parameter `name` is always a string.
    * The parameter `value` must be an `int`, otherwise, a `TypeError` exception
is raised with the message `<name> must be an integer`.
    * The parameter `value` must be greater than `0`, otherwise, a 
`ValueError` exception is raised with the message `<value> must be greater 
than 0`.

* **Rectangle**
  * `8-rectangle.py`: Python class `Rectangle` that inherits from `BaseGeometry` 
(`7-base_geometry.py`). Includes:
    * Private attributes `width` and `height` - validated with `integer_validator`.
    * Instantiation with `width` and `height`: `def __init__(self, width, height
):`

* **Full rectangle**
  * `9-rectangle.py`: Python class `Rectangle` that inherits from `BaseGeometry` 
(`7-base_geometry.py`). Builds on `8-rectangle.py` with:
    * Implementation of the method `area()`.
    * Special method `__str__` to print `Rectangle`s in the format `[Rectangle] 
<width>/<height>`.

* **Square #1**
  * `10-square.py`: Python class `Square` that inherits from `Rectangle` 
(`9-rectangle.py`). Includes:
    * Private attribute `size` - validated with `integer_validator`.
    * Instantiation with `size`: `def __init__(self, size):`.
    * Implementation of the `area()` method.

* **Square #2**
  * `11-square.py`: Python class `Square` that inherits from `Rectangle` 
(`9-rectangle.py`). Builds on `10-square.py` with:
    * Special method `__str__` to print squares in the format `[Square] 
<width>/<height>`.

* **My integer**
  * `100-my_int.py`: Python class `MyInt` that inherits from `int`. Includes:
    * Inversion of the `==` and `!=` operators.

* **Can I?**
  * `101-add_attribute.py`: Python function that adds a new attribute to an 
object if possible.
    * If an attribute cannot be added, a `TypeError` exception is raised with the 
message `can't add new attribute`.
