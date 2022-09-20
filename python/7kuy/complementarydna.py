#題目
# 在 DNA 字符串中，符號“A”和“T”是互補的，如“C”和“G”。您的函數接收 DNA 的一側（字符串，Haskell 除外）；你需要返回另一個互補的一面。DNA 鏈永遠不會是空的或根本沒有 DNA（同樣，Haskell 除外）。
# 在這裡可以找到更多類似的練習：http ://rosalind.info/problems/list-view/ （來源）
# 示例：（輸入 --> 輸出）
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


def DNA_strand(dna):
    li = list(dna)
    for i in range(len(li)):
        a = li[i]
        if a == "A":
            li[i] = "T"
        elif a == "T":
            li[i] = "A"
        elif a == "C":
            li[i] = "G"
        elif a == "G":
            li[i] = "C"
    word = "".join(li)
    return word


# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])