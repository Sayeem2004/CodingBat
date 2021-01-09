public boolean strCopies(String str, String sub, int n) {
  return strCount(str,sub) >= n;
}
public int strCount(String str, String sub) {
  if (str.length() <= sub.length())
    return (str.equals(sub)) ? 1 : 0;
  int n = sub.length();
  return ((str.substring(0,n).equals(sub)) ? 1 : 0) + strCount(str.substring(1),sub);

}
