def missing_char(s, n):
  q = ""
  for i in s:
    if i != s[n]:
      q = q + i
  return q
