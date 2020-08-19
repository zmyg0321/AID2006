file = open("test.txt",'w')
# file = open("test.txt",'a')

# n = file.write("哈哈哈,咯咯咯,嘤嘤嘤")
# print(f"写入了{n}个字符")

# file.write(b"hello\n")
# file.write("你好".encode())

list01 = ["呵呵\n","嘿嘿\n","哈哈哈\n"]
file.writelines(list01)


file.close()
