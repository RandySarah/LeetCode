# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
#
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
#
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
#
# 示例 1:
#
# 输入: [[1,1,0],[1,0,1],[0,0,0]]
# 输出: [[1,0,0],[0,1,0],[1,1,1]]
# 解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flipping-an-image
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 方法1：先将输入看做一维数组，存储的内容是一个数组，现将该数组逆置，再将里面的内容进行异或操作
# 异或操作：两个值不同 结果为 1 ；两个值相同，结果为 0
# 1 ^ 1 = 0   结论：取反的话需要与1异或
# 0 ^ 1 = 1
# 1 ^ 0 = 1   结论：想获取原值需要与0异或
# 0 ^ 0 = 0


def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    for i in range(0,len(A)):
        A[i].reverse()
        for j in range(0,len(A[i])):
            A[i][j] = A[i][j] ^ 1
    return A


if __name__ == '__main__':
    A=[[1,1,0],[1,0,1],[0,0,0]]
    print(A)
    A = flipAndInvertImage(A)
    print(A)