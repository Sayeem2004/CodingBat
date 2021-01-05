def sumDigits(n):
  s = 0
  x = str(n)
  for i in x:
    if i != "-":
      s = s + int(i)
  return s
