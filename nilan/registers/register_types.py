from enum import Enum, unique


@unique
class Register(Enum):
    HOLDING_REGISTER = (3, 10000)
    INPUT_REGISTER = (4, 00000)

    def __new__(cls, functioncode, offset):
        cls.functioncode = functioncode
        cls.offset = offset
