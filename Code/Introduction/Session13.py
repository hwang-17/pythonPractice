# list 列表
# 可变的 初始化之后呢  还可以改变
# 表示：[]
lst = ["zhansan", "李四", 5, 7.4]
print(lst, type(lst))
# index :索引
# print(lst[index])
print(lst[1])

lst[1] = "lisi"
print(lst)

lst.append("王五")
print(lst)

lst.insert(1, "潘金莲")
print(lst)

lst.pop()
print(lst)

lst.remove("潘金莲")
print(lst)
