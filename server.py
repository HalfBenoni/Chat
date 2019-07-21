#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
host = socket.gethostbyname(socket.gethostname())
port = 8888
s.bind((host, port))
print('сервер запущен')

# список подключенных клиентов
clients = []

while True:
    data, addr = s.recvfrom(1024)

    if addr not in clients:
        clients.append(addr)
        # msg = 'Вы присоединились к чату'
        # s.sendto(msg.encode('utf-8'), addr)

    # print(data.decode('utf-8'))
    print(clients)

    # отправка сообщений всем участникам чата, кроме отправителя
    for client in clients:
        if client != addr:
            s.sendto(data, client)

s.close()
