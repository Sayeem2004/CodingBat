def rot13(s):
  q = ""
  for i in s:
    if 96 < ord(i) < 123:
      q += chr(97 + (ord(i) + 13 - 97) % 26)
    elif 64 <= ord(i) <= 93:
      q += chr(64 + (ord(i) + 13 - 64) % 26)
    else:
      q += i
  return q
