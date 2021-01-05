def rot13Char(c):
  x = 0
  if 123 > ord(c) > 96:
    return chr(97 + (ord(c) + 13 - 97) % 26)
  if 91 > ord(c) > 64:
    return chr(65 + (ord(c) + 13 - 65) % 26)
  return c
