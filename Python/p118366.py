def string_splosion(str):
  i = 0
  q = ""
  while i < len(str):
    q = q + str[ :i+1]
    i += 1
  return q
