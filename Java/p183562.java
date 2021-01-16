public boolean makeBricks(int small, int big, int goal) {
  if (small + big*5 < goal) return false;
  if (goal%5 > small) return false;
  return true;
}
