def pigLatinBest(word):
  if word[-1].isalpha() == False:
    q = word[:-1]
    e = word[-1]
    return pigLatin(q) + e
  else:
    return piglatin(word)
def pigLatin(word):
  d = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
  if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    return word + 'hay'
  else:
    x = 0
    for i in d:
      if i == word[ :2]:
        x = x + 1
    if x > 0:
      return word[2:] + word[:2] + 'ay'
  return word[1:] + word[0] + 'ay'
