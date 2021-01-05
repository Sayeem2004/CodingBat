public boolean groupSum6(int start, int[] nums, int target) {
  return groupSum62(start,nums,target,0);
}
public boolean groupSum62(int start, int[] nums, int target, int sum) {
  if (sum == target && start == nums.length) return true;
  if (start >= nums.length) return false;
  if (sum > target) return false;
  if (nums[start] == 6) return groupSum62(start+1,nums,target,sum+6);
  else return groupSum62(start+1,nums,target,sum+nums[start]) || groupSum62(start+1,nums,target,sum);
}
