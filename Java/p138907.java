public boolean groupSum5(int start, int[] nums, int target) {
  return groupSum5(start,nums,target,0);
}
public boolean groupSum5(int start, int[] nums, int target, int sum) {
  if (sum == target && start == nums.length) return true;
  if (start >= nums.length) return false;
  if (sum > target) return false;
  if (start == nums.length-1 && nums[start]%5 == 0)
    return groupSum5(start+1,nums,target,sum+nums[start]);
  if (nums[start]%5 == 0 && nums[start+1] == 1)
    return groupSum5(start+2,nums,target,sum+nums[start]);
  if (nums[start]%5 == 0)
    return groupSum5(start+1,nums,target,sum+nums[start]);
  return groupSum5(start+1,nums,target,sum+nums[start]) || groupSum5(start+1,nums,target,sum);
}
