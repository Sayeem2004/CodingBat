public boolean groupNoAdj(int start, int[] nums, int target) {
  return groupNoAdj2(start,nums,target,0);
}
public boolean groupNoAdj2(int start, int[] nums, int target, int sum) {
  if (sum == target) return true;
  if (start >= nums.length) return false;
  if (sum > target) return false;
  return groupNoAdj2(start+2,nums,target,sum+nums[start]) || groupNoAdj2(start+1,nums,target,sum);
}
