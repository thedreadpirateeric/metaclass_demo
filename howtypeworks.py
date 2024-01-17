# How is a class created.abs

class Test:
    """This is a test class."""
    a = "The letter a"
    one = 1

t = Test()
t.a
t.one

type(t.a)
type(t.one)

Test = type("Test", (), {"a": "The letter a", "one": 1})


from datetime import datetime

alist = [
    ("testing", "some test thing"),
    ("timestamp", datetime.utcnow()),
    ("someId", 4554764563),
    ("name", "CoolKids")
]

obj = type("MyClass", (), {s[0]: s[1] for s in alist})()

def pdate(self):
    return str(self.timestamp)

blist = alist + [("print_date", pdate)]

obj = type("MyClass", (), {s[0]: s[1] for s in blist})()
