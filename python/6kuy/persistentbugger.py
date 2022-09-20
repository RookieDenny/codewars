# 題目
# 編寫一個函數 ，persistence它接受一個正參數num並返回其乘法持久性，這是您必須將數字相乘num直到達到單個數字的次數。
# 例如（輸入 --> 輸出）：
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)



def persistence(num):
    if num < 10:
        return 0 
    num_str = str(num)
    total = 1
    for i in num_str:
        total = total * int(i)
    return 1 + persistence(total)



# import operator
# def persistence(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i