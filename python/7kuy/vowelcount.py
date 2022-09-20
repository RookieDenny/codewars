#題目
# 返回給定字符串中元音的數量（計數）。
# 我們將考慮a, e, i, o,u作為這個 Kata 的元音（但不是y）。
# 輸入字符串將僅包含小寫字母和/或空格。



def get_count(sentence):
    count = 0
    y = "aeiou"
    for x in sentence:
        for t in y:
            if x == t:
                count = count + 1
    return (count)



#def getCount(s):
#return sum(c in 'aeiou' for c in s)