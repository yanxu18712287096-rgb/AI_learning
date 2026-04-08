dict = {"zhangsan": 3.422,
        "lisi": 3.233,
        "lisi2": 3.622 }

for name, gba in dict.items():
    print("{name}同学，你好！\n\
          你的gba为{gba}".format(name = name, gba = gba))