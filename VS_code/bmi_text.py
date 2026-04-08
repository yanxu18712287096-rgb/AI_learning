# input默认输出str类型
user_height = input("请输出你的身高(m):")
user_weight = input("请输入你的体重(kg):")
bmi = float(user_weight) / float(user_height) ** 2
if bmi < 28:
    print("超重")
elif bmi < 24:
    print("正常")
elif bmi < 18.5:
    print("偏瘦")
else:
    print("肥胖")