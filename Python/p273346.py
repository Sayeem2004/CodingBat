def plusOut(s,word):
  i = 0
  n = ""
  while i < len(word):
    n += "+"
    i += 1
  q = s.replace(word, n)
  for o in q:
    if o != "+" and o != "-":
      q = q.replace(o, "-")
  q = q.replace(n, word)
  q = q.replace("-", "+")
  return q
  
