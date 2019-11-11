# 学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
#
# 请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以 非递减 高度排列的必要移动人数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/height-checker
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 实例1
# 输入：[1,1,4,2,1,3]
# 输出：3
# 解释：
# 高度为 4、3 和最后一个 1 的学生，没有站在正确的位置。

# 方法1 新建一个数组，按递增排序，对比两个数组不一样的个数，则为必要移动个数
# 原数组 [1,1,4,2,1,3]
# 新数组 [1,1,1,2,3,4]
# 新建数组需要深拷贝数组：https://www.cnblogs.com/liangyan-1989/p/8145469.html

# TODO:研究下方法2

import copy

def heightChecker(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    h2 = copy.deepcopy(heights)
    h2.sort()
    num = 0
    for i in range(0,len(h2)):
        if(heights[i] != h2[i]):
            num = num+1
    return num


if __name__ == '__main__':
    A=[1,1,4,2,1,3]
    print(heightChecker(A))
