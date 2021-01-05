def countOddDigits(n):
  n = str(n)
  s = 0
  for i in n:
    if i != '-':
      if int(i)%2 == 1:
        s = s + 1
  return s
