<div align="center">
  <p align="center">
    <a href="https://github.com/kebasyaty/xloft">
      <img
        height="90"
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
      <a href="https://github.com/kebasyaty/xloft/issues"><img src="https://img.shields.io/github/issues/kebasyaty/xloft.svg" alt="GitHub issues"></a>
      <a href="https://pepy.tech/projects/xloft"><img src="https://static.pepy.tech/badge/xloft" alt="PyPI Downloads"></a>
      <a href="https://github.com/kebasyaty/xloft/blob/main/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/xloft" alt="GitHub license"></a>
      <a href="https://docs.astral.sh/ruff/" alt="Code style: Ruff"><img src="https://img.shields.io/badge/code%20style-Ruff-FDD835.svg" alt="Code style: Ruff"></a>
      <a href="https://github.com/kebasyaty/xloft" alt="PyPI implementation"><img src="https://img.shields.io/pypi/implementation/xloft" alt="PyPI implementation"></a>
      <a href="https://github.com/kebasyaty/xloft" alt="GitHub repository"><img src="https://img.shields.io/badge/--ecebeb?logo=github&logoColor=000000" alt="GitHub repository"></a>
      <br>
      <a href="https://pypi.org/project/xloft"><img src="https://img.shields.io/pypi/format/xloft" alt="Format"></a>
      <a href="https://github.com/kebasyaty/xloft"><img src="https://img.shields.io/github/languages/top/kebasyaty/xloft" alt="Top"></a>
      <a href="https://github.com/kebasyaty/xloft"><img src="https://img.shields.io/github/repo-size/kebasyaty/xloft" alt="Size"></a>
      <a href="https://github.com/kebasyaty/xloft"><img src="https://img.shields.io/github/last-commit/kebasyaty/xloft/main" alt="Last commit"></a>
    </p>
    <p align="center">
      Currently, the collection is represented by one element `NamedTuple`.
    </p>
  </p>
</div>

##

## Documentation

Online browsable documentation is available at [https://kebasyaty.github.io/xloft/](https://kebasyaty.github.io/xloft/ "Documentation").

## Requirements

[View the list of requirements.](https://github.com/kebasyaty/xloft/blob/main/REQUIREMENTS.md "View the list of requirements.")

## Installation

```shell
uv add xloft
```

## Usage

```python
from xloft import NamedTuple


nt = NamedTuple(x=10, y="Hello")
# or
d = {"x": 10, "y": "Hello"}
nt = NamedTuple(**d)

nt.x  # => 10
nt.y  # => "Hello"
nt.z  # => raise: KeyError

len(nt)  # => 2
nt.keys()  # => ["x", "y"]
nt.values()  # => [10, "Hello"]

nt.has_key("x")  # => True
nt.has_key("y")  # => True
nt.has_key("z")  # => False

nt.has_value(10)  # => True
nt.has_value("Hello")  # => True
nt.has_value([1, 2, 3])  # => False

nt.get("x")  # => 10
nt.get("y")  # => "Hello"
nt.get("z")  # => None

d = nt.to_dict()
d["x"]  # => 10
d["y"]  # => "Hello"

for key, val in nt.items():
    print(f"Key: {key}, Value: {val}")

nt["x"]  # => raise: KeyError
nt["y"]  # => raise: KeyError
nt["z"]  # => raise: KeyError
nt["x"] = 20  # => TypeError
nt["y"] = "Hi"  # => TypeError
nt["z"] = [1, 2, 3]  # => TypeError

nt.update("x", 20)
nt.update("y", "Hi")
nt.x  # => 20
nt.y  # => "Hi"
nt.update("z", [1, 2, 3])  # => raise: KeyError

nt.x = 20  # => raise: AttributeDoesNotSetValue
nt.y = "Hi"  # => raise: AttributeDoesNotSetValue
nt.z = [1, 2, 3]  # => raise: AttributeDoesNotSetValue

del nt.x  # => raise: AttributeCannotBeDelete
del nt.y # => raise: AttributeCannotBeDelete
```

## Changelog

[View the change history.](https://github.com/kebasyaty/xloft/blob/main/CHANGELOG.md "Changelog")

## License

This project is licensed under the** [MIT](https://github.com/kebasyaty/xloft/blob/main/LICENSE "MIT")**.
