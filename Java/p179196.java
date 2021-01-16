public boolean lessBy10(int a, int b, int c) {
  int mx = Math.max(a,Math.max(b,c));
  int mn = Math.min(a,Math.min(b,c));
  return mx-mn >= 10;
}
