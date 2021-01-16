public int noTeenSum(int a, int b, int c) {
  return teen(a) + teen(b) + teen(c);
}
public int teen(int a) {
  if (a == 15 || a == 16) return a;
  if (a >= 13 && a <= 19) return 0;
  return a;
}
