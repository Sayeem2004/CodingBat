public int count7(int n) {
  if (n == 7) return 1;
  if (n < 10) return 0;
  return ((n%10 == 7) ? 1 : 0) + count7(n/10);
}
