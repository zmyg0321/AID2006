# 打开文件
# file = open("test.txt", 'w') # 写 文件不存在创建
# file = open("test.txt", 'r') # 读 默认 文件必须存在
file = open("test.txt", 'a')  # 追加写

# 对文件操作
print(file)

# 关闭文件对象
file.close()
