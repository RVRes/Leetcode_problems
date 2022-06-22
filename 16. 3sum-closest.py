# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
#
# Constraints:
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104
from typing import List, Callable
import time
from itertools import combinations
from random import randint


def three_sum_closest_1(nums: List[int], target: int) -> int:
    return sorted(list(set(map(sum, combinations(nums, 3)))), key=lambda x: abs(target - x))[0]


def three_sum_closest_2(nums: List[int], target: int) -> int:
    nums.sort()
    nums_len = len(nums)
    result = sum(nums[:3])
    for n1idx in range(nums_len - 2):
        n2idx, n3idx = n1idx + 1, nums_len - 1
        while n3idx > n2idx:
            sum_3 = nums[n1idx] + nums[n2idx] + nums[n3idx]
            if sum_3 == target:
                return target
            if abs(target - sum_3) < abs(target - result):
                result = sum_3
            if sum_3 > target:
                n3idx -= 1
            else:
                n2idx += 1
    return result


def three_sum_closest_3(nums: List[int], target: int) -> int:
    nums.sort()
    nums_len = len(nums)
    result = sum(nums[:3])
    for n1idx in range(nums_len - 2):
        if n1idx > 0 and nums[n1idx] == nums[n1idx - 1]:
            while n1idx <= nums_len - 2 and nums[n1idx] == nums[n1idx - 1]:
                n1idx += 1
        n2idx, n3idx = n1idx + 1, nums_len - 1
        while n3idx > n2idx:
            sum_3 = nums[n1idx] + nums[n2idx] + nums[n3idx]
            if sum_3 == target:
                return target
            if abs(target - sum_3) < abs(target - result):
                result = sum_3
            if sum_3 > target:
                n3idx -= 1
                while n3idx >= n2idx and nums[n3idx] == nums[n3idx + 1]:
                    n3idx -= 1
            else:
                n2idx += 1
                while n3idx >= n2idx and nums[n2idx] == nums[n2idx - 1]:
                    n2idx += 1
    return result


def three_sum_closest_4(nums: List[int], target: int) -> int:
    nums.sort()
    nums_len = len(nums)
    result = sum(nums[:3])
    for n1idx in range(nums_len - 2):
        if n1idx > 0 and nums[n1idx] == nums[n1idx - 1]:
            while n1idx <= nums_len - 2 and nums[n1idx] == nums[n1idx - 1]:
                n1idx += 1
        n2idx, n3idx = n1idx + 1, nums_len - 1
        while n3idx > n2idx:
            sum_3 = nums[n1idx] + nums[n2idx] + nums[n3idx]
            if sum_3 == target:
                return target
            if abs(target - sum_3) < abs(target - result):
                result = sum_3
            if sum_3 > target:
                if target > nums[n1idx] + nums[n3idx-1] + nums[n3idx]:
                    break
                n3idx -= 1
                while n3idx > n2idx and nums[n3idx] == nums[n3idx + 1]:
                    n3idx -= 1
                if nums[n1idx] + nums[n2idx] + nums[n3idx] > sum_3:
                    break
            else:
                if target < nums[n1idx] + nums[n2idx] + nums[n2idx+1]:
                    break
                n2idx += 1
                while n3idx > n2idx and nums[n2idx] == nums[n2idx - 1]:
                    n2idx += 1
                if nums[n1idx] + nums[n2idx] + nums[n3idx] < sum_3:
                    break
    return result


def three_sum_closest_5(nums: List[int], target: int) -> int:
    def find2(tar, l, r):
        if tar <= nums[l] + nums[l+1]:
            return tar - nums[l] - nums[l+1]
        elif tar >= nums[r-1] + nums[r]:
            return tar - nums[r-1] - nums[r]
        dis = tar - nums[l] - nums[r]
        while l < r:
            s = nums[l] + nums[r]
            if s == tar:
                return 0
            if s < tar:
                l += 1
                if tar-s < abs(dis):
                    dis = tar-s
            else:
                r -= 1
                if s-tar < abs(dis):
                    dis = tar-s
        return dis
    nums.sort()
    ans = sum(nums[:3])
    dis = abs(target-ans)
    L = len(nums)
    for i in range(L-2):
        d = find2(target-nums[i], i+1, L-1)
        if d == 0:
            return target
        if abs(d) < dis:
            ans = target - d
            dis = abs(d)
    return ans


def execute(func: Callable, test_, answer):
    time_start = time.time()
    result = func(*test_)
    time_delta = time.time() - time_start
    print(f'{round(time_delta, 2):4}s {"OK" if result == answer or answer is None else "ER"}'
          f' {func.__name__} tgt: {test_[1]} out:{result} inp:{test}')


lc_tst1 = [665, 366, 479, -347, 134, 825, -109, 302, -623, -396, 855, 383, 89, -586, 754, -183, 862, 283, -238, 793,
           221, -507, -27, 64, 8, 201, -509, 33, 611, -813, 990, 161, 380, 408, -307, -571, 432, -697, -893, 720, -127,
           439, 127, 849, -199, 498, 245, 878, 607, 40, -2, 976, -381, -428, -159, -369, 75, -879, -715, 962, -37, -478,
           398, 457, -773, -134, -767, 291, 1000, -306, 625, 433, 271, 262, 663, -718, 711, 606, 570, 461, 138, 108,
           -453, -675, -431, 100, -15, -82, 303, 103, 598, 315, -276, -702, 865, 198, -676, -591, -158, 114, 403, 885,
           -834, -721, -521, 650, -906, -901, 608, 227, -401, 3, 989, -947, 434, -925, -557, -787, 504, -714, 717, -693,
           228, 729, -424, 620, 854, -786, 301, -599, -832, -707, -582, -946, -128, -123, 458, -3, 349, 538, -50, 436,
           -980, -593, -983, 149, 777, -761, 831, 699, -497, 481, 768, 670, 915, -285, -327, 223, 158, 871, 259, -242,
           -678, 946, 32, 156, 875, 693, 967, 774, -929, -255, -488, 807, -404, -577, -966, -154, -868, -595, -277,
           -447, 779, -320, -350, -844, -429, 802, 870, -321, 215, 780, 622, -185, -94, 472, 616, -143, -249, -18, -898,
           -360, -800, -207, 914, 576, -605, -600, -409, -776, 265, 379, -997, 430, 645, 289, -573, -991, -708, -448,
           -39, -496, -17, 252, 877, -480, 832, 87, -950, 806, -939, -535, -483, 81, -819, -699, 508, -412, 452, -967,
           -357, 842, -934, -149, -116, 515, 966, -72, 85, -441, -326, 883, 511, 331, -549, -343, -640, -661, -337,
           -444, -798, 968, -826, -408, -589, 309, -894, 427, 460, -828, 677, -703, 186, 499, -114, 547, 497, -643, 588,
           -460, 386, -932, -30, 510, -558, -410, -585, 49, -176, 533, 982, 204, 21, 132, 932, -645, 527, 956, 587,
           -344, -87, 418, 506, 993, 804, 953, -450, -759, 889, 147, 726, -266, 851, -231, 374, -340, 269, 412, 39,
           -863, -191, 893, 326, -486, 970, -961, -168, -284, -438, 172, 375, 843, 957, -821, 767, 751, 939, 267, 839,
           -416, -373, -936, -856, -445, -214, -733, 876, 135, 737, -541, -153, -719, 531, 425, 507, -757, 921, 101,
           -226, -923, 540, 950, 249, 394, -325, -117, 978, 284, 651, -394, 51, -590, 491, 706, -423, 609, 644, -765,
           910, 553, 796, 176, 782, 718, 567, -335, -835, -235, 285, 358, 695, -612, -852, -753, 524, 224, 287, 785,
           282, -899, 920, -695, 742, 10, 723, -690, 918, -799, 922, -658, -861, -580, 42, 148, -862, -302, 113, 68,
           789, -982, 143, 800, 564, 798, 82, -902, 410, -420, 217, 152, 469, -7, 518, -194, -487, -631, 270, 987, 813,
           647, 669, -875, 790, 758, -169, 942, -520, -700, 788, -297, -554, -975, 104, -141, -716, -414, -314, 449,
           -215, -182, 998, 637, -345, -994, 977, -10, 864, -79, -313, -24, 965, 884, -922, -452, -632, 981, 67, -22,
           -775, 272, -808, -505, 773, -133, 401, 400, -361, 756, 495, 541, -48, 805, -969, -164, 150, -730, 170, -433,
           207, 691, 216, 330, 596, -101, -16, -611, 734, 268, 836, -288, 327, 485, 240, 202, 858, -365, -122, 115,
           -904, 685, -66, 591, -726, 688, -731, -155, 242, -197, -131, 355, 25, 247, 739, -466, 868, -259, 390, -156,
           740, -780, 173, -795, 641, 212, -669, -493, 653, 753, -292, 19, -398, -243, -668, 655, -334, -735, 467, -28,
           -181, 213, -108, 765, 323, 595, 534, -293, -564, -308, -392, -58, 338, -349, 824, 701, -630, -792, -537, 399,
           37, -443, 385, -916, -216, -411, 562, 975, -533, 192, -750, -888, -766, 835, 18, -222, -187, 659, -741, -239,
           530, 297, 822, -734, 648, -954, 992, -809, -996, -839, 900, -517, -375, 703, 307, 627, -575, -706, -736, 483,
           342, -499, 523, -173, -760, 185, -613, 866, 949, -504, 72, -887, 700, 395, 0, 643, -100, -377, -754, -890,
           131, 110, -607, 125, 188, -61, 762, -914, -641, 907, -768, -44, 514, 459, 786, 294, -157, -615, -536, 593,
           189, -358, -921, 577, 354, 744, 924, 664, 890, 882, 730, 36, -274, 405, 257, 98, -92, 556, 253, 48, -971,
           -502, 973, 563, -634, 118, -40, -351, -272, 340, 996, 927, 451, -310, -584, -974, 238, -909, -305, 705, 589,
           -805, -491, -694, 422, -682, -619, -494, 208, 863, -965, -895, -889, 770, 516, -279, -217, -566, 9, -526,
           794, 23, -206, 603, -701, 879, -670, -129, 53, 73, 881, 119, -186, -625, -60, 898, -748, 210, 83, -854, 661,
           -449, 590, -166, 7, -118, -850, 943, 735, 163, -33, -818, -905, -949, -952, -827, -677, 600, -138, 344, -498,
           -544, 409, -124, -372, -884, -20, 387, 256, 936, -273, 674, 891, -657, 707, 193, -858, 894, -336, -688, -476,
           -851, 719, 837, 642, 803, 276, -32, -481, 372, 682, 959, -788, -797, -330, -785, -489, 232, 41, 776, 440,
           153, -77, 827, 969, -926, -574, -26, -992, 586, -943, -784, 656, 336, -262, 746]

TESTS = [
    # ((input:list, target: int), output: int)
    (([-1, 2, 1, -4], 1), 2),
    (([0, 2, 1, -3], 1), 0),
    (([0, 0, 0], 1), 0),
    (([10, 20, -10, 5, 11], 28), 26),
    (([1, 100, 7, 11, 5], -10), 13),
    ((lc_tst1, 3509), None),
    (([randint(-100, 100) for _ in range(100)], randint(-100, 100)), None),
    (([randint(-1000, 1000) for _ in range(1000)], randint(-10000, 10000)), None),
    (([randint(-1000, 1000) for _ in range(1000)], randint(-10000, 10000)), None),
    (([randint(-1000, 1000) for _ in range(10000)], randint(-10000, 10000)), None),
]

for test in TESTS:
    # execute(three_sum_closest_1, test[0], test[1])
    execute(three_sum_closest_2, test[0], test[1])
    execute(three_sum_closest_3, test[0], test[1])
    execute(three_sum_closest_4, test[0], test[1])
    execute(three_sum_closest_5, test[0], test[1])
    print()
