def shiftWord(s,n):
  q = ''
  for x in s:
    q = q + chr(ord(x)+n)
  return q
