f = open("test.txt", "wb+")

f.write(b"hello world")
f.flush()

print("偏移量：",f.tell())

f.seek(-3,2)

data = f.read()
print(data)