def pigLatinMultiple(s):
  if len(s) == 0:
    return ""
  else:
    lt = s.split(" ")
  lt2 = []
  for i in lt:
    lt2.append(pigLatin(i))
  return " ".join(lt2)
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
