def end_other(x, y):
  x = x.lower()
  y = y.lower()
  return y[len(y)-len(x): ] == x or x[len(x)-len(y): ] == y
