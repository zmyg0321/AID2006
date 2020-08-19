from time import sleep, ctime

f = open("my.log", "a")

n = 1

f.seek(0, 0)

for line in f:
    n += 1

while True:
    sleep(2)
    msg = "%d. %s\n" % (n, ctime())
    f.write(msg)
    f.flush()
    n += 1

f.close()
