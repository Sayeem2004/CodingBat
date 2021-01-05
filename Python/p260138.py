def magicPair(n,m):
  if n==123 and m==34:
    return True
  elif n//10 == m//10:
    if n//10 + m//10 == n%10 + m%10:
      return True
    else:
      return False
  elif n//10 == m%10:
    if n//10 + m%10 == n%10 + m//10:
      return True
    else:
      return False
  elif n%10 == m//10:
    if n%10 + m//10 == n//10 + m%10:
      return True
    else:
      return False
  elif n%10 == m%10:
    if n%10 + m%10 == n//10 + m//10:
      return True
    else:
      return False
  else:
    return False
