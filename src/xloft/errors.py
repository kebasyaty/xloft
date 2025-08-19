"""XLOT Exceptions."""

from __future__ import annotations


class XLOTException(Exception):
    """Root Custom Exception."""

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]# noqa: D107
        super().__init__(*args, **kwargs)


class AttributeDoesNotSetValue(XLOTException):
    """Exception is raised if the attribute does not setting value."""

    def __init__(self, attribute_name: str) -> None:  # noqa: D107
        self.message = f"The attribute `{attribute_name}` does not setting value!"
        super().__init__(self.message)


class AttributeCannotBeDelete(XLOTException):
    """Exception is raised if the attribute cannot be delete."""

    def __init__(self, attribute_name: str) -> None:  # noqa: D107
        self.message = f"The attribute `{attribute_name}` cannot be delete!"
        super().__init__(self.message)
