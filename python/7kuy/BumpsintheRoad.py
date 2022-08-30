#題目
# 你的車很舊，很容易壞。減震器不見了，您認為它可以在完全死亡之前再承受大約 15 次顛簸。
# 對您來說不幸的是，您的驅動器非常顛簸！給定一個顯示平坦道路 ( _) 或顛簸 ( n) 的字符串。如果遇到能安全到家15 bumps or less，就返回Woohoo!，否則返回Car Dead


#我的解法
from itertools import count
def bumps(road):
    x = road.count("n")
    if x <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"

#大神解法
# return "Woohoo!" if road.count("n") <= 15 else "Car Dead"
# 用count判斷字串n在字符串出現幾次去比對15，True就回傳"Woohoo!"，False回傳"Car Dead"

