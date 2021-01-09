public int countHi2(String str) {
  return countHi(str) - countX(str);
}
public int countHi(String str) {
  if (str.length() <= 1) return 0;
  return ((str.substring(0,2).equals("hi")) ? 1 : 0) + countHi(str.substring(1));
}
public int countX(String str) {
  if (str.length() <= 2) return 0;
  return ((str.charAt(0) == 'x' && str.substring(1,3).equals("hi")) ? 1 : 0) + countX(str.substring(1));
}
