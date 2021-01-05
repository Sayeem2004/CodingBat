def pigLatinSimple(word):
  s = ""
  if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
    s = word + "hay"
  else:
    s = s + word[1: ]
    s = s + word[0]
    s = s + "ay"
  return s
