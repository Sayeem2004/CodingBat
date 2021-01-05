public int count8(int n) {
  if (n == 8) return 1;
  if (n < 10) return 0;
  int a = 0;
  if (n%10 == 8 && n/10%10 == 8) a = 2;
  else if (n%10 == 8) a = 1;
  return a + count8(n/10);
}
