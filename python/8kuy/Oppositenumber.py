#題目
#很簡單，給定一個整數或一個浮點數，找到它的反面。
#例子
# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    if abs(number) == number:
        return - + number
    else:
        return abs(number)