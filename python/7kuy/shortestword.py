#題目
# 很簡單，給定一串單詞，返回最短單詞的長度。
# 字符串永遠不會為空，您不需要考慮不同的數據類型。



#我的解法
import re
def find_short(s):
    a = re.split(' ', s)
    y =[]
    for x in a:
        y.append(len(x))
    return(min(y))


#大神解法
    # return min(len(x) for x in s.split())
    # s.split變成陣列後依序代進x,計算長度回傳最小值