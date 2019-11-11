# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
#
# 你可以返回满足此条件的任何数组作为答案。
#
#  
#
# 示例：
#
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#  
#
# 提示：
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-array-by-parity
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 方法1：定义两个数组 一个放奇数 一个放偶数 最后将奇数数组拼接到偶数数组后面
# 方法2：定义两个指针，i=0 j j从前往后遍历 如果遇到偶数则ij数组内容互换，i+1

def sortArrayByParity1(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    B=[]
    C=[]
    for i in range(0,len(A)):
        if(A[i]%2 == 0):
            B.append(A[i])
        else:
            C.append(A[i])
    return B+C

def sortArrayByParity2(A):
    i=0
    tmp=0
    for j in range(0,len(A)):
        if(A[j] % 2 == 0):
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i = i +1
    return A




if __name__ == '__main__':
    A=[3,1,2,4]
    print(sortArrayByParity1(A))
    print(sortArrayByParity2(A))