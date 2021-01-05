public String startOz(String str) {
  String q = "";
  if (str.length() > 0) {
    if (str.charAt(0) == 'o') {
      q = q + str.charAt(0);
    }
  }
  if (str.length() > 1) {
    if (str.charAt(1) == 'z') {
      q = q + str.charAt(1);
    }
  }
  return q;
}
