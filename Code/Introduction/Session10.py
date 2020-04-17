# python条件语句:
# 现在假设你去相亲, 你的硬性条件是 不能比你大 26

age = input("您好,请问您贵庚:")
print("您的年龄是:" + age)

agenum = int(age)
# 如果 agenum > 26  不行
# 否则 我们再聊聊

#  if agenum > 26 不行
# else 咱们聊聊

if agenum > 26:
    print("不好意思  我太丑了")
else:
    print("加个微信再聊聊")


