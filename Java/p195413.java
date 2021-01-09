public int strDist(String str, String sub) {
  if (str.lastIndexOf(sub) != -1)
    return str.lastIndexOf(sub) - str.indexOf(sub) + sub.length();
  return 0;
}
