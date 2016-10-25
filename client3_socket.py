import socket
ip_port = ('10.21.168.218',9999)
client = socket.socket()

client.connect(ip_port)

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )
    server_res_msg = client.recv(1024)
    cmd_res_msg = str(server_res_msg.decode()).split("#")
    print ("server response:",cmd_res_msg)
#    if cmd_res_msg[0] == "MD_RESULT_SIZE":
    cmd_res_size = int(cmd_res_msg[1])
#       print (cmd_res_size)
    client.send(b"aaaaa")
    res=''
    recv_size = 0
    while recv_size < cmd_res_size:
          data = client.recv(1024)
          recv_size += len(data)
          res +=str(data.decode())
    else:
        print (str(res))     
        print ('--------recv done--------') 


client.close()
