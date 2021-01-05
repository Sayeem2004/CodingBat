def sameStartChar(s):
  i = 0
  while i < len(s)-1:
    if s[i] == "*":
      if i != 0:
        if s[i-1] != s[i+1]:
          return False
    i += 1
  return True
