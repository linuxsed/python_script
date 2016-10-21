import socket
ip_port = ('10.21.168.218',9999)
client = socket.socket()

client.connect(ip_port)

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )

    data = client.recv(1024)
    print("来自服务器:",str(data,'utf8'))

client.close()
