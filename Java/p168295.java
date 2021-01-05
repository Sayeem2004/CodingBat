public boolean split53(int[] nums) {
  return check(0,0,0,nums);
}
public boolean check(int s1, int s2, int i, int[] nums) {
  if (i == nums.length) return s1 == s2;
  if (nums[i]%5 == 0)
    return check(s1+nums[i],s2,i+1,nums);
  if (nums[i]%3 == 0)
    return check(s1,s2+nums[i],i+1,nums);
  return check(s1+nums[i],s2,i+1,nums) || check(s1,s2+nums[i],i+1,nums);
}
