#### AliasDict

```py linenums="1"
"""Pseudo dictionary with supports aliases for keys."""

from xloft import AliasDict

d = AliasDict()
# or
d = AliasDict(
    ({"English", "en"}, "lemmatize_en_all"),
    ({"Russian", "ru"}, "lemmatize_ru_all"),
    ({"German", "de"}, "lemmatize_de_all"),
)
# or
data = [
    ({"English", "en"}, "lemmatize_en_all"),
    ({"Russian", "ru"}, "lemmatize_ru_all"),
    ({"German", "de"}, "lemmatize_de_all"),
    ({"four", "Four", 4}, "I'm fourth"),
]
d = AliasDict(*data)

len(d)  # => 4
#
d["English"]  # => "lemmatize_en_all"
d["en"]  # => "lemmatize_en_all"
d["EN"]  # => KeyError
#
d["English"] = "Hi"
d["en"]  # => "Hi"
d["en"] = "lemmatize_en_all"
d["English"]  # => "lemmatize_en_all"
#
d["five"] = "I'm fifth"
d["five"]  # => "I'm fifth"
#
del d["five"]
d["five"]  # => KeyError
#
d.get("English")  # => "lemmatize_en_all"
d.get("en")  # => "lemmatize_en_all"
d.get("EN")  # => None
#
d.add({"Turkish", "tr"}, "libstemmer_tr")
d.get("Turkish")  # => "libstemmer_tr"
d.get("tr")  # => "libstemmer_tr"
#
d.update(4, "Hello world!")
d.get("four")  # => "Hello world!"
d.get(4)  # => "Hello world!"
#
d.add_alias(4, "four stars")
d.get("four stars")  # => "Hello world!"
#
d.delete_alias("four stars")
d.get("four stars")  # => None
#
d.delete(four)
d.get("four")  # => None
d.get(4)  # => None
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
