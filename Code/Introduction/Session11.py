# python条件语句:
# 现在假设你去相亲, 你的硬性条件是 20到26之间

age = input("您好,请问您贵庚:")
print("您的年龄是:" + age)

agenum = int(age)

if agenum > 26:
    print("不合适")
elif agenum < 20:
    print("不合适")
else:
    print("要微信")
    
