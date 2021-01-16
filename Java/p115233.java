public int withoutDoubles(int die1, int die2, boolean noDoubles) {
  if (noDoubles)
    if (die1 == die2)
      return die1 + (((die2+1)%7 == 0) ? 1 : (die2+1)%7);
  return die1+die2;
}
