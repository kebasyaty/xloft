<div align="center">
  <p align="center">
    <a href="https://github.com/kebasyaty/xloft">
      <img
        height="80"
        alt="Logo"
        src="https://raw.githubusercontent.com/kebasyaty/xloft/main/assets/logo.png">
    </a>
  </p>
  <p>
    <h1>XLOFT</h1>
    <h3>(XLOFT) X-Library of tools.</h3>
    <p align="center">
      <a href="https://github.com/kebasyaty/xloft/actions/workflows/test.yml" alt="Build Status"><img src="https://github.com/kebasyaty/xloft/actions/workflows/test.yml/badge.svg" alt="Build Status"></a>
      <a href="https://kebasyaty.github.io/xloft/" alt="Docs"><img src="https://img.shields.io/badge/docs-available-brightgreen.svg" alt="Docs"></a>
      <a href="https://pypi.python.org/pypi/xloft/" alt="PyPI pyversions"><img src="https://img.shields.io/pypi/pyversions/xloft.svg" alt="PyPI pyversions"></a>
      <a href="https://pypi.python.org/pypi/xloft/" alt="PyPI status"><img src="https://img.shields.io/pypi/status/xloft.svg" alt="PyPI status"></a>
      <a href="https://pypi.python.org/pypi/xloft/" alt="PyPI version fury.io"><img src="https://badge.fury.io/py/xloft.svg" alt="PyPI version fury.io"></a>
      <br>
      <a href="https://pyrefly.org/" alt="Types: Pyrefly"><img src="https://img.shields.io/badge/types-Pyrefly-FFB74D.svg" alt="Types: Pyrefly"></a>
      <a href="https://docs.astral.sh/ruff/" alt="Code style: Ruff"><img src="https://img.shields.io/badge/code%20style-Ruff-FDD835.svg" alt="Code style: Ruff"></a>
      <a href="https://pypi.org/project/xloft"><img src="https://img.shields.io/pypi/format/xloft" alt="Format"></a>
      <a href="https://pepy.tech/projects/xloft"><img src="https://static.pepy.tech/badge/xloft" alt="PyPI Downloads"></a>
      <a href="https://github.com/kebasyaty/xloft/blob/main/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/xloft" alt="GitHub license"></a>
    </p>
    <p align="center">
      The collection is represented by three modules of `NamedTuple`, `AliasDict`, `Converters`, `ItIs`.
      <br>
      In the future, new tools can be added.
    </p>
  </p>
</div>

##

<br>

[![Documentation](https://raw.githubusercontent.com/kebasyaty/xloft/v0/assets/links/documentation.svg "Documentation")](https://kebasyaty.github.io/xloft/ "Documentation")

[![Requirements](https://raw.githubusercontent.com/kebasyaty/xloft/v0/assets/links/requirements.svg "Requirements")](https://github.com/kebasyaty/xloft/blob/v0/REQUIREMENTS.md "Requirements")

## Installation

```shell
uv add xloft
```

## Usage

[![Examples](https://raw.githubusercontent.com/kebasyaty/xloft/v0/assets/links/examples.svg "Examples")](https://kebasyaty.github.io/xloft/latest/pages/usage/ "Examples")

- **NamedTuple**

```python
"""This class imitates the behavior of the `named tuple`."""

from xloft import NamedTuple


nt = NamedTuple(x=10, y="Hello", _id="507c7f79bcf86cd7994f6c0e")
# or
d = {"x": 10, "y": "Hello", "_id": "507c7f79bcf86cd7994f6c0e"}
nt = NamedTuple(**d)

nt.x  # => 10
nt.y  # => Hello
nt._id  # => 507c7f79bcf86cd7994f6c0e
nt.z  # => raise: KeyError

len(nt)  # => 3
list(nt.keys())  # => ["x", "y", "_id"]
list(nt.values())  # => [10, "Hello", "507c7f79bcf86cd7994f6c0e"]

nt.has_key("x")  # => True
nt.has_key("y")  # => True
nt.hsa_key("_id")  # => True
nt.has_key("z")  # => False

nt.has_value(10)  # => True
nt.has_value("Hello")  # => True
nt.has_value("507c7f79bcf86cd7994f6c0e")  # => True
nt.has_value([1, 2, 3])  # => False

nt.get("x")  # => 10
nt.get("y")  # => Hello
nt.get("_id")  # => 507c7f79bcf86cd7994f6c0e
nt.get("z")  # => None

d = nt.to_dict()
d["x"]  # => 10
d.get("y")  # => Hello
d.get("z") # => None

for key, val in nt.items():
    print(f"Key: {key}, Value: {val}")

nt.update("x", 20)
nt.update("y", "Hi")
nt.update("_id", "new_id")
nt.x  # => 20
nt.y  # => Hi
nt._id  # => new_id
nt.update("z", [1, 2, 3])  # => raise: KeyError

nt["x"]  # => raise: KeyError
nt["y"]  # => raise: KeyError
nt["_id"]  # => raise: KeyError
nt["z"]  # => raise: KeyError
nt["x"] = 20  # => TypeError
nt["y"] = "Hi"  # => TypeError
nt["_id"] = "new_id"  # => TypeError
nt["z"] = [1, 2, 3]  # => TypeError

nt.x = 20  # => raise: AttributeDoesNotSetValueError
nt.y = "Hi"  # => raise: AttributeDoesNotSetValueError
nt._id = "new_id"  # => raise: AttributeDoesNotSetValueError
nt.z = [1, 2, 3]  # => raise: AttributeDoesNotSetValueError

del nt.x  # => raise: AttributeCannotBeDeleteError
del nt.y # => raise: AttributeCannotBeDeleteError
del nt._id # => raise: AttributeCannotBeDeleteError
```

- **AliasDict**

```python
"""Pseudo dictionary with supports aliases for keys."""

from xloft import AliasDict

d = AliasDict()
# or
data = [
    ({"English", "en"}, "lemmatize_en_all"),
    ({"Russian", "ru"}, "lemmatize_ru_all"),
    ({"German", "de"}, "lemmatize_de_all"),
    ({"five", 5}, "Five it's me!"),
]
d = AliasDict(data)

len(d)  # => 4
#
d["English"]  # => "lemmatize_en_all"
d["en"]  # => "lemmatize_en_all"
d["EN"]  # => KeyError
d.get("English")  # => "lemmatize_en_all"
d.get("en")  # => "lemmatize_en_all"
d.get("EN")  # => None
#
d.add({"Turkish", "tr"}, "libstemmer_tr")
d.get("Turkish")  # => "libstemmer_tr"
d.get("tr")  # => "libstemmer_tr"
#
d.update(5, "Hello world!")
d.get("five")  # => "Hello world!"
d.get(5)  # => "Hello world!"
#
d.add_alias(5, "five stars")  # or -> d.add_alias("five", "five stars")
d.get("five stars")  # => "Hello world!"
#
d.delete_alias("five stars")
d.get("five stars")  # => None
#
d.delete(5)
d.get("five")  # => None
d.get(5)  # => None
#
d.has_key("English")  # => True
d.has_key("en")  # => True
d.has_key("EN")  # => False
#
d.has_value("lemmatize_en_all")  # True
d.has_value(6)  # False
#
# items() -> `Generator[tuple[list[str | int | float], Any]]`
for aliases, value in d.items():
    print(f"Aliases of key: {aliases}, Value: {value}")
#
list(d.keys())  # => ["English", "en", "Russian", "ru", "German", "de", "Turkish", "tr"]
#
list(d.values())  # => ["lemmatize_en_all", "lemmatize_ru_all", "lemmatize_de_all", "libstemmer_tr"]
```

- **Converters**

```python
"""Convert the number of bytes into a human-readable format."""

from xloft import to_human_size, int_to_roman, roman_to_int
# from xloft.converters import to_human_size, int_to_roman, roman_to_int


to_human_size(200)  # => 200 bytes
to_human_size(1048576)  # => 1 MB
to_human_size(1048575)  # => 1023.999 KB
#
int_to_roman(1994)  # => MCMXCIV
roman_to_int("MCMXCIV")  # => 1994
```

- **ItIs**

```python
"""Check if a string is a number."""

from xloft import is_number, is_palindrome
# from xloft.itis import is_number, is_palindrome


is_number("")  # => False
is_number(" ")  # => False
is_number("1230.")  # => False
is_number("0x5")  # => False
is_number("0o5")  # => False
is_number("-5.0")  # => True
is_number("+5.0")  # => True
is_number("5.0")  # => True
is_number(".5")  # => True
is_number("5.")  # => True
is_number("3.4E+38")  # => True
is_number("3.4E-38")  # => True
is_number("1.7E+308")  # => True
is_number("1.7E-308")  # => True
is_number("-1.7976931348623157e+308")  # => True
is_number("1.7976931348623157e+308")  # => True
is_number("72028601076372765770200707816364342373431783018070841859646251155447849538676")  # => True
is_number("-72028601076372765770200707816364342373431783018070841859646251155447849538676")  # => True
#
is_palindrome("racecar")  # True
is_palindrome("Go hang a salami, I'm a lasagna hog") # True
is_palindrome("22022022")  # True
is_palindrome("Gene")  # False
is_palindrome("123")  # False
is_palindrome(123)  # TypeError
is_palindrome("")  # ValueError
```

<br>

[![Changelog](https://raw.githubusercontent.com/kebasyaty/xloft/v0/assets/links/changelog.svg "Changelog")](https://github.com/kebasyaty/xloft/blob/v0/CHANGELOG.md "Changelog")

[![MIT](https://raw.githubusercontent.com/kebasyaty/xloft/v0/assets/links/mit.svg "MIT")](https://github.com/kebasyaty/xloft/blob/main/LICENSE "MIT")
