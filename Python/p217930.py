def countPrimeDigits(n):
  s = 0
  n = str(n)
  for i in n:
    if i != "-":
      if int(i) == 2 or int(i) == 3 or int(i) == 5 or int(i) == 7:
        s = s + 1
  return s
