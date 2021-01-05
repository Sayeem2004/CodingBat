def countLetter(string,letter):
  s = 0
  i = 0
  while i < len(string):
    if string[i] == letter:
      s += 1
    i += 1
  return s
