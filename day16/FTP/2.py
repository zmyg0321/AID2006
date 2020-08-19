# 打开文件
file = open("test.txt",'r')

# 读取file文件中的内容
# data = file.read(15)
#
# print(data)

# while True:
#     data = file.read(5)
#     if not data:
#         break
#     print(data,end="")

# readline 读取一行内容
# line = file.readline()
# print(line)

# 读取文件内容，形成一个列表，列表中的每个元素是一行
# l = file.readlines(8)
# print(l)

# 迭代每次取一行
for line in file:
    print(line)

file.close()