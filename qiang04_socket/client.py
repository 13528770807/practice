import socket

# 创建 socket 对象
s = socket.socket()

# 绑定地址
host = socket.gethostname()
port = 12345
print(host)

# 建立链接
s.connect((host, port))
print(s.recv(1024).decode())

# 关闭链接
s.close()

