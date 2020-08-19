"""
    基于select方法的IO多路复用网络并发
"""
from socket import *
from select import select

# 创建监听套接字
sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)

# 与非阻塞IO配合防止传输过程阻塞
sockfd.setblocking(False)

# 准备IO进行监控
rlist = [sockfd]
wlist = []
xlist = []

# 循环监控IO发生
while True:
    # 开始监控IO
    rs, ws, xs = select(rlist, wlist, xlist)
    # 伴随监控的IO增多，就绪的IO情况也会复杂
    # 分类讨论 分两类    sockfd --connfd
    for r in rs:
        # 有客户端连接
        if r is sockfd:  # 对象判断用is
            connfd, addr = r.accept()
            print("Connect from", addr)
            connfd.setblocking(False)
            rlist.append(connfd)  # 增加监控
        else:
            # 某个客户端发消息给我
            data = r.recv(1024).decode()
            if not data:
                # 客户端退出
                rlist.remove(r)  # 移除监控
                r.close()
                continue
            print("收到：", data)
            wlist.append(r)

    for w in ws:
        w.send(b"OK")
        wlist.remove(w)  # 如果不移除就会一直发送
