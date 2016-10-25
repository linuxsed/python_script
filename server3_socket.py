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
        cmd_all =subprocess.Popen(data,shell=True,stdout=subprocess.PIPE)
        cmd_relust = cmd_all.stdout.read()
        if len(cmd_relust) == 0:
           cmd_relust = b"cmd exec success,has not output!"
        ack_msg = bytes("CMD_RESULT_SIZE#%s" % len(cmd_relust),'utf8')
        conn.send(ack_msg)
        client_ack = conn.recv(1024)
        print (client_ack)
        if client_ack.decode() == "aaaaa":
           conn.send(cmd_relust)
sk.close()
