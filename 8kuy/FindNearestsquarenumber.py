#題目
#你的任務是找到一個正整數 n 的最接近的平方數，nearest_sq(n)。

def nearest_sq(n):
    a = pow(n,0.5)
    b = round(a)
    return (b**2)