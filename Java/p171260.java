public String stringX(String str) {
  if (str.length() < 2) {
    return str;
  }
  String q = str.substring(0,1);
  for (int i = 1; i < str.length()-1; i++) {
    if (!str.substring(i,i+1).equals("x")) {
      q += str.charAt(i);
    }
  }
  return q+str.charAt(str.length()-1);
}
