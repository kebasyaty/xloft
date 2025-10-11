#### Is number

```py linenums="1"
"""Check if a string is a number."""

from xloft.itis import is_number


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
