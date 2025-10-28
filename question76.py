import zlib
sentence = 'hello world!hello world!hello world!hello world!'
y = bytes(sentence, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))