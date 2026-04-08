# result = 0;
# for num in range(1,101):
#     result += num
#
# print(result)

student_list = {"zhangsan":18,
                "lisi":19,
                "wangwu":17,
                "zhaoliu" :20}

for name, age in student_list.items():
    if(age >= 18):
        print([name, age])