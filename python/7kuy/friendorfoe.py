#題目
# 製作一個過濾字符串列表並返回僅包含您朋友姓名的列表的程序。
# 如果一個名字中正好有 4 個字母，那麼您可以確定它一定是您的朋友！否則，你可以確定他不是……
# 例如：輸入 = ["Ryan", "Kieran", "Jason", "Yous"]，輸出 = ["Ryan", "Yous"]
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]


def friend(x):
    a = []
    for y in x:
        if len(y) == 4:
           a.append(y)
    return a 



# return [f for f in x if len(f) == 4]
