public boolean array220(int[] nums, int index) {
  if (index >= nums.length-1)
    return false;
  if (nums[index]*10 == nums[index+1])
    return true || array220(nums,index+1);
  else
    return false || array220(nums,index+1);
}
