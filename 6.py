file01 = open("/home/tarena/bbb.jpeg", "rb")
file02 = open("/home/tarena/PycharmProjects/zhangmingyang/month02/day03/bbb.jpeg", "wb")

list01 = []
for line in file01:
    list01.append(line)

file02.writelines(list01)

file01.close()
file02.close()