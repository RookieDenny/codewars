#題目
# 編寫一個函數，它接受一個數字數組並返回數字的總和。這些數字可以是負數或非整數。如果數組不包含任何數字，則應返回 0。
# 例子
# 輸入：[1, 5.2, 4, 0, -1]
# 輸出：9.2
# 輸入：[]
# 輸出：0
# 輸入：[-2.398]
# 輸出：-2.398


def sum_array(a):
    return sum(a) if a else 0