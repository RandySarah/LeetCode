# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 方法1：使用两个指针一前一后遍历该数组，如果两个数之和等于目标值则返回坐标

# def solution1(nums,target):
#     if len(nums) < 2:
#         return
#     for i in range(0,len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]


# 方法2：借助字典
# 从头遍历该数组，将每个元素与目标元素的差值算出来，从字典获取差值元素，如果没有则将该元素，以及该元素下标放入字典中，
# 如果存在差值元素，则返回差值元素的下标和该元素的下标

def solution2(nums,target):
    dict1 = {}
    for i in range(0, len(nums)):
        num = target - nums[i]
        if num not in dict1:
            dict1[nums[i]] = i
        else:
            return [dict1[num],i]


if __name__ == '__main__':
    nums = [2,7,11,9]
    print(len(nums))
    target = 9
    a = solution2(nums,target)
    print(a)
    