public String stringSplosion(String str) {
  String q = "";
  for (int i = 1; i <= str.length(); i++) {
    q += str.substring(0,i);
  }
  return q;
}
