import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg_envio = input("Digite: ")
    cliente.sendto(msg_envio.encode(), ("192.168.36.13", 12040))
    msg_bytes, ip_cliente = cliente.recvfrom(2048)
    print(msg_bytes.decode())