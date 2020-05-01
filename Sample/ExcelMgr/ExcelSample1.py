# 任务：将指定的Excel进行统计

# 一. 读取Excel中的数据  
# xlrd   ------> pip install xlrd --user
import xlrd
work_book = xlrd.open_workbook("TestTable.xls")
print(work_book, type(work_book))
sheets = work_book.sheets()
print(sheets, type(sheets))

usedSheet = None
for sheet in sheets:
    if sheet.name == "TestSheet":
        usedSheet = sheet
        print(sheet.name + "：我就是你想要的")
    else:
        print(sheet.name + "：我就是你不想要的")


print("获取到的Sheet:" + usedSheet.name)

# 行数： usedSheet.nrows
# 列数： usedSheet.ncols

print("行数：" + str(usedSheet.nrows))
print("列数：" + str(usedSheet.ncols))
# usedSheet.row(行号)  ——----> 获取一行数据
print(usedSheet.row(1))

# for rowIndex in range(0, usedSheet.nrows):
#     print("行索引：" + str(rowIndex))
#     print(usedSheet.row(rowIndex))


# 二. 统计总条数
rowCount = usedSheet.nrows - 2
print("有效数据行数：" + str(rowCount))

# 三. 统计Money列总和值

money_sum = 0
for rowIndex in range(2, usedSheet.nrows):
    rowValues = usedSheet.row(rowIndex)
    # rowValues[1].value   获取指定行下的指定列
    print("Money: " + str(rowValues[1].value))
    money_sum = money_sum + float(rowValues[1].value)

print("Money的和值：" + str(money_sum))

# 四. 计算Money列的平均值
money_mean = money_sum / rowCount
print("money的平均值：" + str(money_mean))

# 五. 计算rate列的和值
rateSum = 0
for rowIndex in range(2, usedSheet.nrows):
    rowValues = usedSheet.row(rowIndex)
    rateValue = rowValues[3].value
    # rateSum = rateSum + float(rateValue)
    rateSum += float(rateValue)

print("rate的和值：" + str(rateSum))

# 六. 计算Arrears列的和值
arrearsSum = 0
for rowIndex in range(2, usedSheet.nrows):
    rowValues = usedSheet.row(rowIndex)
    arrearsValue = rowValues[11].value
    arrearsSum += float(arrearsValue)

print("Arrears的和值：" + str(arrearsSum))

# 七. 输出

