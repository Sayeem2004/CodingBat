public String stringClean(String str) {
  if (str.length() <= 1) return str;
  char a = str.charAt(0);
  int pos = 1;
  while (pos < str.length() && str.charAt(pos) == a) pos++;
  return a + stringClean(str.substring(pos));
}
