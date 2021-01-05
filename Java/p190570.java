public String missingChar(String str, int n) {
  String q = "";
  for (int i = 0; i < str.length(); i++) {
    if (i != n) {
      q = q + str.charAt(i);
    }
  }
  return q;
}
