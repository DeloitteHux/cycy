from characteristic import Attribute, attributes


class Node(object):
    pass


@attributes([
    Attribute(name="operand"),
    Attribute(name="left"),
    Attribute(name="right"),
])
class BinaryOperation(Node):
    def __init__(self):
        assert self.operand in ("+", "-", "!=") # for now

@attributes([
    Attribute(name="name"),
    Attribute(name="vtype"),
    Attribute(name="value"),
])
class VariableDeclaration(Node):
    def __init__(self):
        assert self.vtype == "INT32"

@attributes([Attribute(name="value")])
class Int32(Node):
    def __init__(self):
        assert isinstance(self.value, int)
        assert -2**32 < self.value <= 2**32-1

@attributes([Attribute(name="name")])
class Variable(Node):
    def __init__(self):
        pass

@attributes([Attribute(name="operand"), Attribute(name="variable")])
class PostOperation(Node):
    def __init__(self):
        assert self.operand in ("++", "--")

@attributes([Attribute(name="left"), Attribute(name="right")])
class Assignment(Node):
    def __init__(self):
        assert isinstance(self.left, Variable)

@attributes([Attribute(name="value")])
class Array(Node):
    def __init__(self):
        _type = type(self.value[0])
        for v in self.value:
            assert isinstance(v, _type)

@attributes([Attribute(name="value")])
class Char(Node):
    def __init__(self):
        # TODO handle escaped chars
        assert isinstance(self.value, str) and len(self.value) == 1
