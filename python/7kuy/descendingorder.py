#題目
# 你的任務是創建一個函數，它可以將任何非負整數作為參數，並以降序返回它的數字。本質上，重新排列數字以創建盡可能高的數字。
# 例子：
# 輸入：42145 輸出：54421
# 輸入：145263 輸出：654321
# 輸入：123456789 輸出：987654321


def descending_order(num):
    lts = str(num)
    a = sorted(lts,reverse=True)
    x = ''.join(a)
    return int(x)



# return int("".join(sorted(str(num), reverse=True)))
