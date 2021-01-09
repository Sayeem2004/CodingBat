public String parenBit(String str) {
  if (str.charAt(0) == '(')
    return "(" + helper(str.substring(1));
  return parenBit(str.substring(1));
}
public String helper(String str) {
  if (str.charAt(0) == ')')
    return ")";
  return str.charAt(0) + helper(str.substring(1));
}
