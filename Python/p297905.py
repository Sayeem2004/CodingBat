def shiftWordByOne(s):
  q = ''
  for x in s:
    q = q + chr(ord(x)+1)
  return q
