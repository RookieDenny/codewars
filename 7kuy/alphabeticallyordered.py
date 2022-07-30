#題目
# 你的任務很簡單。只需編寫一個函數，它接受一個小寫isAlphabetic(s)的輸入字符串並根據字符串是否按字母順序返回/ 。struefalse
# 例如，isAlphabetic('kata')是 False，因為 'a' 在 'k' 之後，但isAlphabetic('ant')它是 True。

#我的解法
def alphabetic(s):
    c = "".join(sorted(s))
    if s == c:
        return (True)
    else:
        return (False)


# 大神解法
# def alphabetic(s):
#     return sorted(s) == list(s)
#排序s英文字母同事變成陣列，進行比對迴傳True,False
