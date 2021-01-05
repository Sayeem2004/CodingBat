public boolean splitOdd10(int[] nums) {
   return check(0,0,0,nums);
}
public boolean check(int s1, int s2, int i, int[] v) {
  if (i == v.length) return (s1%10 == 0 && s2%2 == 1) || (s2%10 == 0 && s1%2 == 1) ;
  return check(s1+v[i],s2,i+1,v) || check(s1,s2+v[i],i+1,v);
}
