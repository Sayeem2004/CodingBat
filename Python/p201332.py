def findWord(original,word):
  i = 0
  while i < len(original) - len(word) + 1:
    if original[i:i+len(word)] == word:
      return i
    i += 1
  return -1
