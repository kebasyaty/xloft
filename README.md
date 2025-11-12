<div align="center">
  <p align="center">
    <a href="https://github.com/kebasyaty/xloft">
      <img
        height="80"
        alt="Logo"
        src="https://raw.githubusercontent.com/kebasyaty/xloft/main/assets/logo.svg">
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
      <a href="https://mypy-lang.org/" alt="Types: Mypy"><img src="https://img.shields.io/badge/types-Mypy-202235.svg?color=0c7ebf" alt="Types: Mypy"></a>
      <a href="https://docs.astral.sh/ruff/" alt="Code style: Ruff"><img src="https://img.shields.io/badge/code%20style-Ruff-FDD835.svg" alt="Code style: Ruff"></a>
      <a href="https://pypi.org/project/xloft"><img src="https://img.shields.io/pypi/format/xloft" alt="Format"></a>
      <a href="https://github.com/kebasyaty/xloft"><img src="https://img.shields.io/github/languages/top/kebasyaty/xloft" alt="Top"></a>
      <a href="https://github.com/kebasyaty/xloft" alt="PyPI implementation"><img src="https://img.shields.io/pypi/implementation/xloft" alt="PyPI implementation"></a>
      <br>
      <a href="https://pepy.tech/projects/xloft"><img src="https://static.pepy.tech/badge/xloft" alt="PyPI Downloads"></a>
      <a href="https://github.com/kebasyaty/xloft/blob/main/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/xloft" alt="GitHub license"></a>
    </p>
    <p align="center">
      The collection is represented by three modules of `NamedTuple`, `Converters`, `ItIs`.
      <br>
      In the future, new tools can be added.
    </p>
  </p>
</div>

##

<br>

## Documentation

Online browsable documentation is available at [https://kebasyaty.github.io/xloft/](https://kebasyaty.github.io/xloft/ "Documentation").

## Requirements

[View the list of requirements.](https://github.com/kebasyaty/xloft/blob/main/REQUIREMENTS.md "View the list of requirements.")

## Installation

```shell
uv add xloft
```

## Usage

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
nt.keys()  # => ["x", "y", "_id"]
nt.values()  # => [10, "Hello", "507c7f79bcf86cd7994f6c0e"]

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

nt.x = 20  # => raise: AttributeDoesNotSetValue
nt.y = "Hi"  # => raise: AttributeDoesNotSetValue
nt._id = "new_id"  # => raise: AttributeDoesNotSetValue
nt.z = [1, 2, 3]  # => raise: AttributeDoesNotSetValue

del nt.x  # => raise: AttributeCannotBeDelete
del nt.y # => raise: AttributeCannotBeDelete
del nt._id # => raise: AttributeCannotBeDelete
```

- **Converters**

```python
"""Convert the number of bytes into a human-readable format."""

from xloft import to_human_size
# from xloft.converters import to_human_size


to_human_size(200)  # => 200 bytes
to_human_size(1048576)  # => 1 MB
to_human_size(1048575)  # => 1023.999 KB
```

- **ItIs**

```python
"""Check if a string is a number."""

from xloft import is_number
# from xloft.itis import is_number


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
```

## Changelog

[View the change history.](https://github.com/kebasyaty/xloft/blob/main/CHANGELOG.md "Changelog")

## License

This project is licensed under the [MIT](https://github.com/kebasyaty/xloft/blob/main/LICENSE "MIT").
