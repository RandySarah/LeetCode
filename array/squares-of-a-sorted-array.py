# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
#  
#
# 示例 1：
#
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 示例 2：
#
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 方案1
# 遍历数组 乘以自身 排序

#
def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    for i in range (0,len(A)):
        A[i] = A[i] * A[i]
    A.sort()
    return A



if __name__ == '__main__':
    A = [2, 7, 11, 9]
    print(sortedSquares(A))