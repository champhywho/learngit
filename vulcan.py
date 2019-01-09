#一个字节8bit，8个二进制数，那么可以表示[0,255]共256个十进制数
#这个[0,255]分别对应了不同的内容，包括符号、数字、字母
#所以当我们提供二进制流时，可以根据8个二进制数，返回一个数字/字母/符号

print(b'Python')
print(b'P',b'y',b't',b'h',b'o',b'n')
print('Python')
#b'Python'
#b'P' b'y' b't' b'h' b'o' b'n'
#Python

#Bytes 代表的是（二进制）数字的序列，
# 只不过在是通过 ASCII 编码之后才是我们看到的字符形式，
# 如果我们单独取出一个字节，它仍然是一个数字
print(b'Python'[0])
#80

#我们可以用 b"*" 的形式创建一个字节类型
# 前提条件是这里的 * 必须是 ASCII 中可用的字符，否则将会超出限制：
#-------print(b'雨')
#bytes can only contain ASCII literal characters.


#ASCII 表里面所有的图形字符只占据了[32, 126]，详见WIKI
#那对于这一范围之外的数字我们要用特殊的转义符号\x+十六进制数字
print(b'\xff')    #b'\xff'
#xff == d255 由于在255不在范围内，所以返回二进制流
print(b'\xff'[0]) #255
#xff == d255   x表示十六进制，d表示十进制整数
print(b'\x24')    #b'$
#x24 == d36 由于36在范围内，检索ASCII表，图形为 $

print(bytes([24,36,121,200]))
#字节类型是一个序列
#b'\x18$y\xc8'
#这就是检索ASCII码的结果
#24 == \x18  因为不再范围内，返回转义16进制数
#36 == $
#121 == y
#200 == \xc8 因为不再范围内，返回转义16进制数

print(bytes.fromhex("7b 7d"))#这里的空格没有意义
#等价于print(bytes((123,125)))

#和字符串一样，字节类型也是不可变序列，而字节数组就是可变版本的字节，
# 它们的关系就相当于list与tuple
b=b'hello'
ba=bytearray(b'HELLO')
print(b,ba)
#b[0:1]=b'w'  'bytes' object does not support item assignment
ba[0:1]=b'W'
print(ba)