from marshmallow import fields as schemaFields
from mongoengine import fields as mongoFields
from marshmallow import Schema

class BaseField:

    def __init__(self, *args, **kwargs) -> None:
        """Field classes for various types of data."""
        self.name = self.__class__.__name__
        self.meta = {k: v for k, v in kwargs.items()}

    def __get__(self, obj, objtype):
        """Use custom getter."""
        if obj is None:
            return self
        return obj._data.get(self.name)

    def __set__(self, obj, val):
        """Use custom settr."""
        if not isinstance(val, self.basetype):
            raise TypeError(f"Value should be of {self.basetype} type.")
        obj._data[self.name] = val

    def __delete__(self, obj):
        """Use custom deltr."""
        obj._data[self.name] = None


class Integer(BaseField):
    """Integer."""

    sfield = schemaFields.Integer
    dbfield = mongoFields.IntField
    basetype = int


class String(BaseField):
    """String."""

    sfield = schemaFields.String
    dbfield = mongoFields.StringField
    basetype = str


class Base(type):
    """Base class."""

    def __new__(cls, name:str, bases: tuple, dct: dict) -> type:
        """Build the class."""

        if name == "Base":
            return super().__new__(cls, name, bases, dct)

        newBases = list()
        for base in bases:
            newBases.append(base)

        dct = {"_fields": {}, **dct}

        _fields = {}

        for key, field in {**_fields, **dct}.items():
            if isinstance(field, BaseField):
                field.name = key
                _fields[key] = field

        if _fields:
            sch = {key: cls._schema_field(value)
                   for key, value in _fields.items()}
            dct['schema'] = cls._make_schema_class(sch)
            dct['_fields'] = _fields

        return super().__new__(cls, name, tuple(newBases), dct)

    @staticmethod
    def _schema_field(field) -> dict:
        return field.sfield(**{**{"allow_none": True}})

    @staticmethod
    def _make_schema_class(attrs: dict) -> Schema:
        return type("BaseSchema", (Schema, ), attrs)


class Test(metaclass=Base):
    """This is our class."""

    _data = {}

    test = String(title="Test Field")
    doit = Integer()

    def __init__(self):
        """Instantiate the class."""
        print("Test Class")

    
