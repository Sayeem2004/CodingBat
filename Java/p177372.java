public int max1020(int a, int b) {
  int q = Math.max(a,b);
  int r = Math.min(a,b);
  if (q > 9 && q < 21) {
    return q;
  } else if (r > 9 && r < 21) {
    return r;
  }
  return 0;
}
