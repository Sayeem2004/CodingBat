public boolean nearHundred(int n) {
  if ((100 - n <= 10 && 100 - n >= -10) || (200 - n <= 10 && 200 - n >= -10)) {
    return true;
  }
  return false;
}
