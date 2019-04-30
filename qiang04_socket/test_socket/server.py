

import socket
# 创建对象

s = socket.socket()

# 绑定地址
host = "127.0.0.1"
port = 12345
s.bind((host, port))

# 设置监听
s.listen(5)

# 阻塞等待
c, addr = s.accept()
print("用户地址：", addr)
c.send("欢迎访问阿里巴巴".encode("utf8"))

# 关闭链接
s.close()