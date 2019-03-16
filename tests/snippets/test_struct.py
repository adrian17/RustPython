from testutils import assert_raises
import struct

data = struct.pack('IH', 14, 12)
assert data == bytes([14, 0, 0, 0, 12, 0])

v1, v2 = struct.unpack('IH', data)
assert v1 == 14
assert v2 == 12

assert struct.pack('f', 10.0) == bytes([0, 0, 32, 65])
assert struct.pack('d', 10.0) == bytes([0, 0, 0, 0, 0, 0, 36, 64])

# TODO: should throw struct.error, throws TypeError currently
assert_raises(Exception, lambda: struct.pack('a'))
assert_raises(Exception, lambda: struct.pack('i'))
assert_raises(Exception, lambda: struct.pack('i', 2, 2))
