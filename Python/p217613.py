def capitalizeSentence(s):
  if len(s) == 0:
    return ""
  e = s.split()
  q = []
  for i in e:
    o = i[0].upper() + i[1:]
    q.append(o)
  return " ".join(q)
