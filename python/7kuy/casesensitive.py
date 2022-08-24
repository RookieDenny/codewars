#題目
# 你的任務很簡單。給定一個輸入字符串 s，case_sensitive(s)，檢查所有字母是否都是小寫。返回 True/False 以及所有非小寫條目的列表，按它們在 s 中出現的順序排列。
# 例如，case_sensitive('codewars') 返回 [True, []]，但 case_sensitive('codeWaRs') 返回 [False, ['W', 'R']]。


#我的解法
def case_sensitive(s):
    if s.islower() or s == '':
        return [True, []] 
    else:
        for x in s:
            if x == x.upper():
                return [False, [x]]


#大神解法
# def case_sensitive(s):
#     return [s.islower() or not s, [c for c in s if c.isupper()]]
#假設帶入"codeWaRs"，判斷是否小寫印出True,False，之後依序代進c判斷大寫印出