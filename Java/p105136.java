public boolean groupSumClump(int start, int[] nums, int target) {
  return groupSumClump(start,nums,target,0);
}
public boolean groupSumClump(int start, int[] nums, int target, int sum) {
  if (sum == target) return true;
  if (start >= nums.length) return false;
  if (sum > target) return false;
  if (start < nums.length-1) {
    if (nums[start] == nums[start+1]) {
      int a = start;
      while (nums[a] == nums[a+1] && a < nums.length-1) a++;
      return groupSumClump(a+1,nums,target,sum+(a-start+1)*nums[start]) || groupSumClump(a+1,nums,target,sum);
    }
  }
  return groupSumClump(start+1,nums,target,sum+nums[start]) || groupSumClump(start+1,nums,target,sum);
}
