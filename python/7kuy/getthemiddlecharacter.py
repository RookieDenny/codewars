#題目
# 你會得到一個字。你的工作是返回單詞的中間字符。如果單詞的長度是奇數，則返回中間字符。如果單詞的長度是偶數，則返回中間 2 個字符。
# ＃例子：
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"




def get_middle(s):
    a = len(s)
    if a % 2 == 0:
        b = int(a / 2)
        return(s[b-1]+s[b])
    else:
        b = int(a / 2)
        return(s[b])


# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1]

