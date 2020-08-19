"""
    非阻塞IO
    套接字对象 --> 非阻塞
"""

from socket import *
import time

# 创建套接字
sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)

# # 设置套接字为非阻塞
# sockfd.setblocking(False)

# 设置超时检测
sockfd.settimeout(3)

# 接收客户端连接
while True:
    try:
        print("waiting for connect")
        connfd, addr = sockfd.accept()
        print("Connect from ", addr)
    except timeout as e:
        # 与accept连接无关的事情
        time.sleep(2)
        with open("test.log", "a") as f:
            msg = "%s:%s\n" % (time.ctime(), e)
            f.write(msg)
            f.close()
    else:
        # 与连接有关的事情
        data = connfd.recv(1024).decode()
        print(data)
