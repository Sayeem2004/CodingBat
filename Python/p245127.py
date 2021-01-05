def isConsonant(c):
  if len(c) == 1 and ord("z") >= ord(c) >= 43:
    if isVowel(c) == False:
      return True
    else:
      return False
  else:
    return False
def isVowel(n):
  if n.lower() == "a" or n.lower() == "e" or n.lower() == "i" or n.lower() == "o" or n.lower() == "u":
    return True
  else:
    return False
