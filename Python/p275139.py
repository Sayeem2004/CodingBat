def myUpper(s):
  q = ''
  for x in s:
    if isVowel(x) or isConsonant(x):
      if already(x):
        q = q + x
      else:
        q = q + chr(ord(x)-32)
    else:
      q = q + x
  return q
def isConsonant(c):
  if len(c) == 1 and ord("z") >= ord(c) >= 64:
    if isVowel(c) == False:
      return True
    else:
      return False
  else:
    return False
def isVowel(s):
  if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    return True
  elif s == "A" or s == "E" or s == "O" or s == "I" or s == "U":
    return True
  else:
    return False
def already(x):
  if 91 > ord(x) > 64:
    return True
  else:
    return False
