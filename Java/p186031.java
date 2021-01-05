public boolean arrayFront9(int[] nums) {
  if (nums.length < 5) {
    for (int i : nums) {
      if (i == 9) {
        return true;
      }
    }
    return false;
  } else {
    for (int i = 0; i < 4; i++) {
      if (nums[i] == 9) {
        return true;
      }
    }
    return false;
  }
}
