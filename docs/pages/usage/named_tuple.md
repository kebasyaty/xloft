#### NamedTuple

```py linenums="1"
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
