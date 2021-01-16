public int redTicket(int a, int b, int c) {
  if (a == 2 && a == b && a == c) return 10;
  if (a == b && b == c) return 5;
  if (a != b && a != c) return 1;
  return 0;
}
