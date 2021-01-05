public String frontTimes(String str, int n) {
  String sub = "";
  if (str.length() < 3) {
    sub = str;
  } else {
    sub = str.substring(0,3);
  }
  String q = "";
  for (int i = 0; i < n; i++) {
    q += sub;
  }
  return q;
}
