import socket
import subprocess

ip_port = ('10.21.168.218',9999)

sk = socket.socket()

sk.bind(ip_port)

sk.listen(5)

while True:
    print("等待客户端的连接...")
    conn,addr = sk.accept()
    while True:
        data = conn.recv(1024)
        if not data:
           print ('客户端已经断开连接')
           break
        print ('来自客户端端的数据',data)
       # cmd_all =subprocess.Popen(cmd,shell=True)
        conn.send(data.upper())
sk.close()
