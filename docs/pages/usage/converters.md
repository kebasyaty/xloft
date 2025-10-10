#### To human size

```py linenums="1"
"""Convert the number of bytes into a human-readable format."""

from xloft import to_human_size


to_human_size(200)  # => 200 bytes
to_human_size(1048576)  # => 1 MB
to_human_size(1048575)  # => 1023.999 KB
```
