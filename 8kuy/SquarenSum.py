#題目
#完成平方和函數，以便將傳入的每個數字平方，然後將結果相加。
#例如， for[1, 2, 2]它應該返回9，因為1^2 + 2^2 + 2^2 = 9.


def square_sum(numbers):
    #your code here
    return(sum(x ** 2 for x in numbers))