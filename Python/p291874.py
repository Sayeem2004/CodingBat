def countDigits(n):
  if n < 0:
    return len(str(n)) - 1
  else:
    return len(str(n))
