import socket


# 创建对象
s = socket.socket()

# 设置ip,端口
host = '127.0.0.1'
port = 12345

# 链接服务器
s.connect((host, port))

# 接收服务器发来的消息并打印
recv_msg = s.recv(1024)
print(recv_msg.decode())

# 关闭连接
s.close()
