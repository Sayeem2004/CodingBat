public int roundSum(int a, int b, int c) {
  return round(a) + round(b) + round(c);
}
public int round(int a) {
  if (a%10 >= 5) return (a/10+1)*10;
  return (a/10)*10;
}
