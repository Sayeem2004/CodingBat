def repeatFront(string,n):
  s = ""
  x = n
  while x != 0:
    s = s + string[ :x]
    x -= 1
  return s
