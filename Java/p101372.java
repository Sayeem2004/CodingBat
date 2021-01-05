public String changeXY(String str) {
  if (str.equals("x")) return "y";
  else if (str.length() <= 1) return str;
  return ((str.substring(0,1).equals("x")) ? "y" : str.substring(0,1)) + changeXY(str.substring(1));
}
