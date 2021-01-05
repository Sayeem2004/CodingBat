def make_chocolate(small, big, goal):
  s = 0
  if big * 5 < goal:
    s = goal - big * 5
  else:
    s = goal % 5
  if s <= small:
    return s
  else:
    return -1
