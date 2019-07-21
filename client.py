# !/usr/bin/python3

import socket
import time
import threading

# определяем хост и порт клиента
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
host = socket.gethostbyname(socket.gethostname())
port = 0
s.bind((host, port))
# s.setblocking(0)

# определяем сервер на который будут отправляться сообщения
server = (socket.gethostbyname(socket.gethostname()), 8888)

join = False
escape = False
name = input('Введите ваше имя: ')


# прием сообщения от сервера
def recieve(name, sock):
    data, addr = sock.recvfrom(1024)
    print(data.decode('utf-8'))


# отправка сообщения на сервер
def send():
    text = input("[" + name + "]->")
    s.sendto(('[' + name + ']->' + text).encode('utf-8'), server)


# уведомление о присоединении
s.sendto(('[' + name + '] присоединился к чату').encode('utf-8'), server)

# rT = threading.Thread(target=recieve, args=("Thread-1", s))
# rT.start()

while escape is False:

    # TODO добавить многопоточность: выделить для функции recieve() отдельный поток для фоновой прослушки порта

    try:
        recieve(name, s)
        time.sleep(0.2)
        send()
        time.sleep(0.2)

    # уведомление об отключении
    except:
        s.sendto(('[' + name + '] покинул чат').encode('utf-8'), server)
        escape = True

# rT.join()
s.close()
