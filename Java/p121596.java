public String altPairs(String str) {
  String q = "";
  if (str.length() < 2) {
    return str;
  }
  for (int i = 0; i < str.length(); i+=4) {
    q += str.charAt(i);
    if (i != str.length()-1) {
      q += str.charAt(i+1);
    }
  }
  return q;
}
