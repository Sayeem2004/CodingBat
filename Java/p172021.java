public int close10(int a, int b) {
  if (Math.abs(a-10) > Math.abs(b-10)) {
    return b;
  } else if (Math.abs(a-10) < Math.abs(b-10)) {
    return a;
  }
  return 0;
}
