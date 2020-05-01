#  解决代码大量重复的问题:
#  函数
#  一小部分工作的封装

import xlrd

# 获取Excel的sheet
def GetSheetBySheetName(excelName, sheetName):
    work_book = xlrd.open_workbook(excelName)
    sheets = work_book.sheets()
    tmpSheet = None
    for sheet in sheets:
        if sheet.name == sheetName:
            tmpSheet = sheet
            print(sheet.name + "：我就是你想要的")
        else:
            print(sheet.name + "：我就是你不想要的")

    return tmpSheet


# 获取指定范围内的和值
def GetSumByColIndex(colIndex, rowStart, rowEnd, sheet):
    sum = 0
    for rowIndex in range(rowStart, rowEnd):
        rowValues = sheet.row(rowIndex)
        sum += float(rowValues[colIndex].value)
    return sum



usedSheet = GetSheetBySheetName("TestTable.xls", "LpSheet")
money_sum = GetSumByColIndex(3, 3, 15, usedSheet)
print("和值:" + str(money_sum))

rate_sum = GetSumByColIndex(4, 3, 15, usedSheet)
print("的和值:" + str(rate_sum))



