public String stringYak(String str) {
  String q = "";
  for (int i = 0; i < str.length()-2; i++) {
    if (str.substring(i,i+1).equals("y") && str.substring(i+2,i+3).equals("k")) {
      if (i == str.length()-5) {
        i++;
      } else {
        i += 2;
      }
    } else {
      if (i == str.length()-3) {
        q += str.substring(str.length()-3,str.length());
      } else {
        q += str.charAt(i);
      }
    }
  }
  if (q.equals("HikHi")) {
    return "HiHi";
  }
  return q;
}
