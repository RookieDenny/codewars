#題目
# 如果我們要開始我們的 Tribonacci 序列[1, 1, 1]作為起始輸入
# 我們有這個序列：
# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# 如果我們從[0, 0, 1]簽名開始呢？作為開始[0, 1]而不是[1, 1]基本上將常見的斐波那契數列移動一個位置
# 您可能會認為我們會將相同的序列移動 2 個位置，但事實並非如此，我們會得到：
# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]3


#我的解法
def tribonacci(signature, n):
    y = len(signature)
    if n == 0:
        return  []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0],signature[1]]
    else:
        for x in range(y,n):
            signature.append(signature[x-3]+signature[x-2]+signature[x-1])
        return  signature


#大神解法
# def tribonacci(signature, n):
#   res = signature[:n]
#   for i in range(n - 3): res.append(sum(res[-3:]))
#   return res