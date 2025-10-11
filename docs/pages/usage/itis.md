#### Is number

```py linenums="1"
"""Check if a string is a number."""

from xloft.itis import is_number


is_number("-1230.0123")  # => True
is_number("+1230.0123")  # => True
is_number("1230.0123")  # => True
is_number("1230.0")  # => True
is_number("1230")  # => True
is_number("1.23e-5")  # => True
is_number("1.23E-5")  # => True
is_number(".5")  # => True

is_number("")  # => False
is_number(" ")  # => False
is_number("1230.")  # => False
is_number("0x5")  # => False
is_number("0o5")  # => False
```
