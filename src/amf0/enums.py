from enum import Enum


class Markers(Enum):
    """
    Hexadecimal markers for specified data types
    """
    NUMBER = '\x00'
    BOOLEAN = '\x01'
    STRING = '\x02'
    OBJECT = '\x03'
    MAP = '\x04'  # Make use of the reserved Movieclip marker
    NULL = '\x05'
    UNDEFINED = '\x06'
    REFERENCE = '\x07'
    ECMA_ARRAY = '\x08'
    OBJECT_END = '\x09'
    STRICT_ARRAY = '\x0A'  # Not supported
    DATE = '\x0B'
    LONG_STRING = '\x0C'
    UNSUPPORTED = '\x0D'
    SET = '\x0E'  # Make use of the reserved Recordset marker
    XML_DOCUMENT = '\x0F'  # Not supported
    TYPED_OBJECT = '\x10'
    AVMPLUS = '\x11'  # Not supported


class ByteOrder(Enum):
    """
    Identify the byte order for data
    """
    LE = '<'  # Little endian
    BE = '>'  # Big endian

    def __str__(self):
        return str(self.value)
