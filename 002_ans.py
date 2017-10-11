'''题目002：（网易）合唱团
有 n 个学生站成一排，每个学生有一个能力值，
牛牛想从这 n 个学生中按照顺序选取 k 名学生，
要求相邻两个学生的位置编号的差不超过 d，
使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？
'''


while 1:
    try:
         n = int(input())
         A = map(int,input().split())
         k,d = map(int,input().split())
    except:
        break
    B = [[[0] * 2 for j in range(n)] for i in range(k + 1)]
    for k in range(1, k + 1):
        for i in range(n):
            if k == 1 or i == 0:
                B[k][i][0],B[k][i][1] = A[i], A[i]
            else:
                M = []
                for t in range(1, d + 1):
                    if i - t < 0:
                        break
                    D = B[k - 1][i - t]
                    M.extend(D[0] * A[i], D[1] * A[i])
                B[k][i][0], B[k][i][1] = min(M), max(M)
    print(max([B[k][i][1] for i in range(n)]))
