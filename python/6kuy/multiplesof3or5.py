#題目
# 如果我們列出所有小於 10 且是 3 或 5 的倍數的自然數，我們會得到 3、5、6 和 9。這些倍數之和是 23。
# 完成解決方案，使其返回傳入數字以下的所有 3 或 5 的倍數之和。此外，如果數字為負數，則返回 0（對於具有它們的語言）。
# 注意：如果數字是 3 和 5 的倍數，則只計算一次。



#我的解法
def solution(number):
    i = []
    for x in range(1,number):
        if x % 3 == 0 or x % 5 == 0:
            i.append(x)
    return sum(i)

#大神解法
# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)