import socket

# 创建套节奏
s = socket.socket()

# 获取本地主机名
host = socket.gethostname()
print(host)

# 设置端口
port = 12345

# 绑定地址
s.bind((host, port))

# 等待客户端链接
s.listen(5)

# 建立客户端链接
while True:
    # 被动接受TCP客户端链接,(阻塞)等待链接到来
    c, addr = s.accept()
    print("链接地址:", addr)
    c.send("欢迎访问菜鸟俱乐部".encode("utf8"))
    c.close()  # 关闭链接
