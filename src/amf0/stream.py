import struct

from .enums import ByteOrder
from .enums import Sizes


class Stream(object):
    """
    Reads and writes binary data types for use with serialization and/or deserialization
    """
    
    def __init__(self, data=list(), endian=ByteOrder.BE):
        self._data = data  # Store the data
        self._position = 0  # Store the position in the data stream
        self._endian = endian.value  # Identify the byte order for the given data

    def get_length(self):
        """
        Return the length of our current data stream
        """
        return len(self._data)

    def bytes_available(self):
        """
        Return the amount of bytes available in the stream
        """
        return self.get_length() - self._position

    def clear(self):
        """
        Explicitly reset the stream to a freshly initialized state
        """
        self._data = list()
        self._position = 0

    def read_boolean(self):
        value = struct.unpack(''.join([self._endian, '?']), self._data[self._position])
        self._position += 1
        return value[0]

    def read_byte(self):
        value = struct.unpack(''.join([self._endian, 'c']), self._data[self._position])
        self._position += 1
        return value[0]

    def read_double(self):
        value = struct.unpack(''.join([self._endian, 'd']), self._data[self._position])
        self._position += 1
        return value[0]

    def read_float(self):
        value = struct.unpack(''.join([self._endian, 'f']), self._data[self._position])
        self._position += 1
        return value[0]

    def read_int(self):
        value = struct.unpack(''.join([self._endian, 'i']), self._data[self._position])
        self._position += 1
        return value[0]

    def read_uint(self):
        value = struct.unpack(''.join([self._endian, 'I']), self._data[self._position])
        self._position += 1
        return value[0]

    def read_short(self):
        value = struct.unpack(''.join([self._endian, 'h']), self._data[self._position])
        self._position += 1
        return value[0]

    def read_ushort(self):
        value = struct.unpack(''.join([self._endian, 'H']), self._data[self._position])
        self._position += 1
        return value[0]

    def write_boolean(self, value: bool):
        self._data.append(struct.pack(''.join([self._endian, '?']), value))

    def write_byte(self, value: bytes):
        if len(value) == 1:
            self._data.append(struct.pack(''.join([self._endian, 'c']), value))

    def write_double(self, value: float):
        self._data.append(struct.pack(''.join([self._endian, 'd']), value))

    def write_float(self, value: float):
        self._data.append(struct.pack(''.join([self._endian, 'f']), value))

    def write_int(self, value: int):
        if value <= Sizes.INT32_MAX.value and value >= Sizes.INT32_MIN.value:
            self._data.append(struct.pack(''.join([self._endian, 'i']), value))

    def write_uint(self, value: int):
        if value <= Sizes.UINT32_MAX.value and value >= Sizes.UINT32_MIN.value:
            self._data.append(struct.pack(''.join([self._endian, 'I']), value))

    def write_short(self, value: int):
        if value <= Sizes.INT16_MAX.value and value >= Sizes.INT16_MIN.value:
            self._data.append(struct.pack(''.join([self._endian, 'h']), value))
        
    def write_ushort(self, value: int):
        if value <= Sizes.UINT16_MAX.value and value >= Sizes.UINT16_MIN.value:
            self._data.append(struct.pack(''.join([self._endian, 'H']), value))
