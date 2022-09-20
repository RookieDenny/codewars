#題目
# 創建一個函數，在給定一個最少 4 個正整數的數組的情況下返回兩個最小正數之和。不會傳遞浮點數或非正整數。
# 例如，當像 一樣傳遞數組時[19, 5, 42, 2, 77]，輸出應該是7。
# [10, 343445353, 3453445, 3453545353453]應該返回3453455。



def sum_two_smallest_numbers(numbers):
    a = sorted(numbers)
    x = a[0] + a[1]
    return (x)




# return sum(sorted(numbers)[:2])
