# python条件语句:
# 现在假设你去相亲, 你的硬性条件是 20到26之间

age = input("您好,请问您贵庚:")
print("您的年龄是:" + age)

agenum = int(age)

if agenum > 26:
    print("不合适")
elif agenum < 18:
    print("未成年保护法")
elif agenum < 16:
    print("不合适")
elif agenum < 14:
    print("会坐牢的")
else:
    print("要微信")
    

