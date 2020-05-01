
# 求咱输入的任意范围的和值
def SumRange(start, end):
    sum = 0
    for value in range(start, end):
        sum = sum + value
        print(sum)

    return sum


sum1 = SumRange(2, 101)
print(sum1)

