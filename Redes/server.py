import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("", 12040))

while True:
    msg_bytes, ip_cliente = servidor.recvfrom(2048)
    msg_resposta = msg_bytes.decode().upper()
    servidor.sendto(msg_resposta.encode(), ip_cliente)
    print(msg_resposta)
