#題目
#取 2 個字符串s1，僅包括從to 的s2字母。返回一個新的排序字符串，盡可能長，包含不同的字母——每個字母只取一次——來自 s1 或 s2。az
#a = "xyaabbbccccdefww"
#b = "xxxxyyyyabklmopq"
#longest(a, b) -> "abcdefklmopqwxy"
#a = "abcdefghijklmnopqrstuvwxyz"
#longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"


def longest(a1, a2):
    return "".join(sorted(set(a1).union(set(a2))))

# return "".join(sorted(set(a1 + a2)))
