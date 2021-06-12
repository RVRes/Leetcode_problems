# Median of Two Sorted Arrays
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    combined_array = nums1 + nums2
    combined_array.sort()
    div_res, remainder = divmod(len(combined_array), 2)
    median = combined_array[div_res] if remainder else (combined_array[div_res] + combined_array[div_res - 1]) / 2
    return median


def findMedianSortedArrays2(nums1: list, nums2: list) -> float:
    # We optimize this to run binary search on the smaller array
    if len(nums1) > len(nums2):
        return findMedianSortedArrays2(nums2, nums1)

    m = end = len(nums1)
    n = len(nums2)
    start = 0
    idx_middle = (m + n + 1) // 2  # Center index of final merged array

    while start <= end:
        partition1 = (start + end) // 2
        partition2 = idx_middle - partition1

        maxleft1 = nums1[partition1 - 1] if partition1 != 0 else -float('inf')
        minright1 = nums1[partition1] if partition1 != m else float('inf')
        maxleft2 = nums2[partition2 - 1] if partition2 != 0 else -float('inf')
        minright2 = nums2[partition2] if partition2 != n else float('inf')

        if maxleft1 > minright2:
            # move nums1 end to before partition
            end = partition1 - 1
        elif maxleft2 > minright1:
            # move nums1 start to after partition
            start = partition1 + 1
        else:
            # Found the right partition!
            # if odd, ans is max(maxleft1, maxleft2)
            # if even, ans is avg of max(maxleft1, maxleft2) and min(minright1, minright2)
            max_of_left = max(maxleft1, maxleft2)
            if (m + n) % 2 == 0:
                min_of_right = min(minright1, minright2)
                return (max_of_left + min_of_right) / 2
            else:
                return max_of_left


# explanation https://www.youtube.com/watch?v=q6IEA26hvXc
def findMedianSortedArrays3(nums1: list, nums2: list) -> float:
    if len(nums2) > len(nums1):
        A, B = nums1, nums2
    else:
        A, B = nums2, nums1
    len_a = len(A)
    len_b = len(B)
    len_merged = len_a + len_b
    middle_merged = (len_merged + 1) // 2
    l, r = 0, len_a
    print('', f'Merged: {sorted(nums1 + nums2)}', '=' * 50, sep='\n')
    while True:
        middle_a = (r + l) // 2
        middle_b = middle_merged - middle_a
        left_max_a = A[middle_a - 1] if middle_a - 1 >= 0 else -float('inf')
        right_min_a = A[middle_a] if middle_a < len_a else float('inf')
        left_max_b = B[middle_b - 1] if middle_b - 1 >= 0 else -float('inf')
        right_min_b = B[middle_b] if middle_b < len_b else float('inf')

        print(f'A: {A[:middle_a:]} {A[middle_a:len_a:]}')
        print(f'B: {B[:middle_b:]} {B[middle_b:len_b:]}')
        print()
        if left_max_b > right_min_a:
            l = middle_a + 1
        elif left_max_a > right_min_b:
            r = middle_a - 1
        # if left_max_a <= right_min_b and left_max_b <= right_min_a:
        else:
            if len_merged % 2 != 0:
                return max(left_max_a, left_max_b)
            else:
                return (min(right_min_a, right_min_b) + max(left_max_a, left_max_b)) / 2


nums1 = [50, 60, 70, 80, 90]
nums2 = [3, 4, 5, 8, 9, 10, 11, 12, 15, 19, 20, 21, 22, 23, 25, 27, 29, 30, 32]

print(findMedianSortedArrays(nums1, nums2))
print(findMedianSortedArrays2(nums1, nums2))
print(findMedianSortedArrays3(nums1, nums2))
