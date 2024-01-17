# BASE meta classes inherit type (class builders)

class Base(type):
    """Base class."""

    def __new__(mcs, name: str, bases: tuple, dct: dict) -> type:
        """Build the class."""
        _fields = {k: type(v) for k, v in dct.items() if not k.startswith("__")}
        dct['_fields'] = _fields
        return super().__new__(mcs, name, bases, dct)


class Test(metaclass=Base):
    """Test Class."""

    a = "The letter a"
    one = 1
