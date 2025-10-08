#### To human size

```py linenums="1"
"""Convert number of bytes to readable format."""

from xloft import to_human_size


to_human_size(200)  # => 200 bytes
to_human_size(1048576)  # => 1 MB
to_human_size(1048575)  # => 1023.999 KB
```
