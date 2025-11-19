#### To human size

```py linenums="1"
"""Convert the number of bytes into a human-readable format."""

from xloft import to_human_size
# from xloft.converters import to_human_size


to_human_size(200)  # => 200 bytes
to_human_size(1048576)  # => 1 MB
to_human_size(1048575)  # => 1023.999 KB
```

#### Roman

```py linenums="1"
"""Convert an integer to Roman and vice versa."""

from xloft import int_to_roman, roman_to_int
# from xloft.converters import int_to_roman, roman_to_int


int_to_roman(1994)  # => MCMXCIV
roman_to_int("MCMXCIV")  # => 1994
```
