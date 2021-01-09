public int strCount(String str, String sub) {
  if (str.length() <= sub.length())
    return (str.equals(sub)) ? 1 : 0;
  int n = sub.length();
  if ((str.substring(0,n).equals(sub)))
    return 1 + strCount(str.substring(n),sub);
  else
    return strCount(str.substring(1),sub);
}
