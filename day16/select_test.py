"""
    select 方法示例
"""

from select import select
from socket import *

# 准备IO
f = open("test.log")

sockfd = socket()
sockfd.bind(("0.0.0.0", 8888))
sockfd.listen(5)

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("0.0.0.0", 8888))

print("开始监控IO")
rs, ws, xs = select([sockfd], [f,sock], [])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)

