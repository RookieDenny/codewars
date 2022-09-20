#題目
#給定一個數字列表，返回可以由這些數字組成的最小數字，僅使用這些數字一次（忽略重複項）。
#只有正整數 將被傳遞給函數 (> 0 )，沒有負數或零。
#minValue ({1, 3, 1})  ==> return (13)


def min_value(digits):
    a = sorted(set(digits))
    return int("".join([str(x)for x in a]))


#return int("".join(map(str,sorted(set(digits)))))
