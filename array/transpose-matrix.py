# 给定一个矩阵 A， 返回 A 的转置矩阵。
#
# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
#
#  
#
# 示例 1：
#
# 输入：[[1,2,3],
#       [4,5,6],
#       [7,8,9]]
# 输出：[[1,4,7],
#       [2,5,8],
#       [3,6,9]]
# 示例 2：
#
# 输入：[[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/transpose-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 方法1 遍历一遍二维数组，新建一个二维数组，B[j][i] = A[i][j]


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row1 = len(A)
        col1 = len(A[0])

        B=[[0 for col in range(row1)]for row in range(col1)]

        for i in range(0,row1):
            for j in range(0,col1):
                B[j][i] = A[i][j]
        return B

if __name__ == "__main__":
    # A=[[1,2,3],[4,5,6],[7,8,9]]
    A=[[1,2,3],[4,5,6]]

    s=Solution()
    print(s.transpose(A))