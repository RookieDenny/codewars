#題目
#實現一個函數，將兩個數字相加並以二進制形式返回它們的和。轉換可以在添加之前或之後進行。
# 返回的二進制數應該是一個字符串。
# 示例：(Input1, Input2 --> Output (解釋)))
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)


#我的解法
def add_binary(a,b):
    return bin(a + b)[2:]

#a+b相加使用bin二進制之後抓取索引2到底部的數字回傳

