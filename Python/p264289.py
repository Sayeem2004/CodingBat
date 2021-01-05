def hailLen(n):
  x = 1
  while (n != 1):
    if (n%2 == 1):
     n = (3 * n) + 1
    else:
      n = n/2
    x += 1
  return x
