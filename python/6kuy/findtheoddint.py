#題目
# 給定一個整數數組，找出出現奇數次的那個。
# 總是只有一個整數出現奇數次。
# [7]應該返回7
# [0]應該返回0
# [1,1,2]應該返回2
# [0,1,0,1,0]應該返回0
# [1,2,2,3,3,3,4,3,3,3,2,2,1]應該返回4


#我的解法
def find_it(seq):
    seq_set = set(seq)
    for x in seq_set:
        if seq.count(x)%2 != 0:
            return x

#大神解法
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i