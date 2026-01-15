#### AliasDict

```py linenums="1"
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
# items() -> `list[tuple[list[str | int | float], Any]]` or `[]`
for aliases, value in d.items():
    print(f"Aliases of key: {aliases}, Value: {value}")
#
d.keys()  # => ["English", "en", "Russian", "ru", "German", "de", "Turkish", "tr"]
#
d.values()  # => ["lemmatize_en_all", "lemmatize_ru_all", "lemmatize_de_all", "libstemmer_tr"]
```
