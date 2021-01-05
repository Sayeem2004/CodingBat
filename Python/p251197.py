def noVowels(s):
  q = ""
  x = 0
  while x < len(s):
    if isVowel(s[x]) == False:
      q = q + s[x]
    x += 1
  return q
def isVowel(n):
  if n.lower() == "a" or n.lower() == "e" or n.lower() == "i" or n.lower() == "o" or n.lower() == "u":
    return True
  else:
    return False
