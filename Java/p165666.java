public String stringBits(String str) {
  String q = "";
  for (int i = 0; i < str.length(); i+=2) {
    q += str.charAt(i);
  }
  return q;
}
