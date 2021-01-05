def makeSentence(x):
  s = ''
  i = 0
  while i <= len(x)-1:
    if i == 0:
      s +=  x[i]
    else:
      s += " " + x[i]
    i += 1
  return s
