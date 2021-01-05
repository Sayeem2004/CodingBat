public boolean groupSum(int start, int[] nums, int target) {
  return groupSum2(start,nums,target,0);
}
public boolean groupSum2(int start, int[] nums, int target, int sum) {
  if (sum == target) return true;
  if (start >= nums.length) return false;
  if (sum + nums[start] == target) return true;
  if (sum > target) return false;
  return groupSum2(start+1,nums,target,sum+nums[start]) || groupSum2(start+1,nums,target,sum);
}
