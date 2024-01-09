c = input()

ascii = ord(c) + 1
if ascii == (ord("z") + 1):
    ascii = ord("a")

print(chr(ascii))