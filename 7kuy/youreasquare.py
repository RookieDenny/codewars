#題目
# 任務
# 給定一個整數，判斷它是否為平方數：
# 在數學中，平方數或完全平方是整數，它是整數的平方；換句話說，它是某個整數與自身的乘積。
# 測試總是使用一些整數，所以在動態類型語言中不用擔心。
# 例子
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

#我的解法
def is_square(n):    
    a  = n ** 0.5
    if a * a == n:
        return True
    else:
        return False

#大神解法
    #return n >= 0 and (n**0.5) % 1 == 0
    # 先比對n數有沒有大於等於0和有沒有整除回傳