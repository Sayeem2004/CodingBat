def make_bricks(small, big, goal):
  if small + (5 * big) < goal:
    return False
  elif goal % 5 <= small:
    return True
  elif goal % 5 == 0:
    return True
  elif goal < small:
    return True
  else:
    return False
