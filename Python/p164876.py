def cat_dog(str):
  i = 0
  c = 0
  d = 0
  while i < len(str):
    if str[i:i+3] == "cat":
      c += 1
    if str[i:i+3] == "dog":
      d += 1
    i += 1
  return c == d
