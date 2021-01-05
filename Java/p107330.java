public int bunnyEars2(int bunnies) {
  if (bunnies == 0)
    return 0;
  return bunnyEars2(bunnies-1) + (2-(bunnies%2-1));
}
