dict = {"张三":18,
        "李四":20,
        ("张三", "李四"): (18,20)}
dict["王五"] = 21
print(dict)
query = input("请输出您的姓名")
if query in dict:
    print("您的年龄为" + str(dict[query]))
else:
    print("您的身份位登记\n")
    print("当前字典记录人数为"+str(len(dict)))
