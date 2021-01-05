def countWord(original,word):
  x = 0
  s = 0
  while x <= len(original):
    if original[x:x+len(word)] == word:
      s = s + 1
    x = x + 1
  return s
