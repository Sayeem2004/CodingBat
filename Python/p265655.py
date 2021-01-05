def findLetter(original,letter):
  s = 0
  i = 0
  while i < len(original):
    if original[i] == letter:
      return s
    s += 1
    i += 1
  return -1
