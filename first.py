# BASE meta classes inherit type (class builders)

class Base(type):
    """Base class."""

    def __new__(mcs, name: str, bases: tuple, dct: dict) -> type:
        """Build the class."""
        print("Base Class!")

        return super().__new__(mcs, name, bases, dct)


class Test(metaclass=Base):
    """Test Class."""

    def __init__(self):
        """Instantiate the class."""
        print("Test Class")
