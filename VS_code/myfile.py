# f = open("./text.txt","r",encoding="utf-8")
# print(f.read())
# # f.close()
# with open("./text.txt","r") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)
with open("text.txt","w") as f:
    f.write("hello world")
    f.write("hello world")