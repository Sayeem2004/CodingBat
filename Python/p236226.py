def ntod(v,e):
  lt = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  q = 0
  for n,i in enumerate(v):
    q += (lt.index(i))*(e**(len(v)-n-1))
  return q
