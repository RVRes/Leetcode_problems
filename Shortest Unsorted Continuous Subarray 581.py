def findUnsortedSubarray(nums) -> int:
    l, r = 0, len(nums) - 1
    while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
        l += 1
    if l == len(nums) - 1:
        return 0
    while r > 0 and nums[r] >= nums[r - 1]:
        r -= 1
    # mx, mn = float("-inf"), float("inf")
    # for index in range(l, r + 1):
    mx = max(nums[l:r+1])
    mn = min(nums[l:r+1])
    while l > 0 and mn < nums[l - 1]:
        l -= 1
    while r < len(nums) - 1 and mx > nums[r + 1]:
        r += 1
    return r - l + 1


# nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [2, 1]
# nums = [1,2,3,3,3]
# nums = [1,3,2,2,2]
# nums = [2,3,3,2,4]
nums = [1, 2, 4, 5, 3]
nums = [1, 2, 5, 3, 4]
print(findUnsortedSubarray(nums))
