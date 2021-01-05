public boolean splitArray(int[] v) {
  return check(0,0,0,v);
}
public boolean check(int s1, int s2, int i, int[] v) {
  if (i == v.length) return s1 == s2;
  return check(s1+v[i],s2,i+1,v) || check(s1,s2+v[i],i+1,v);
}
