public boolean nestParen(String str) {
  return helper(str) == 0;
}
public int helper(String str) {
  if (str.equals("")) return 0;
  if (str.charAt(0) == '(')
    return 1 + helper(str.substring(1));
  if (str.charAt(0) == ')')
    return -1 + helper(str.substring(1));
  return -10000;
}
