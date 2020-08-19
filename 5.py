# with open("test.txt","r+") as f:
#     data = f.read()
#     print(data)
#

# f = open("test.txt", "w+")
f = open("test.txt", "w+",buffering=1) # 行缓冲
# f = open("test.txt", "wb+",buffering=10) # 指定缓冲区的大小

while True:
    info = input(">>")
    f.write(info+"\n")
    # f.write(info.encode())
    # f.flush()
