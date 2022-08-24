#題目
#創建一個將整數作為參數並返回"Even"偶數或"Odd"奇數的函數。

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"