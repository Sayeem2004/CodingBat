public int bigDiff(int[] nums) {
  int mx = -10000, mn = 10000;
  for (int i = 0; i < nums.length; i++) {
    mx = Math.max(nums[i],mx);
    mn = Math.min(nums[i],mn);
  }
  return mx-mn;
}
