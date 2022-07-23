#題目
# 對給定數組（ cq.list ）的所有數字求和，除了最高和最低元素（按值，而不是按索引！）。
# 最高或最低元素分別是每條邊上的單個元素，即使有多個具有相同值的元素。
# 注意輸入驗證。
# 例子
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# 輸入驗證
# 如果給出了一個空值（null、None等Nothing）而不是一個數組，或者給定的數組是一個空列表或只有1元素的列表，則返回0。

def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return (sum(arr))