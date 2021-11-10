# -*- coding: utf-8 -*-
import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 40000))

server = socket.create_server(('127.0.0.1', 40000))
server.listen(2)
while True:
    print('Waiting client...')
    client_socket, address = server.accept()
    data = client_socket.recv(4096).decode('utf-8').split(' ')[1]
    print('Полученные данные:\n', data, '\n-----')

    try:
        rezult = eval(data[1:])
        print(f'Переменная rezult: {rezult if rezult else None}')
        content = f'Ответ:{rezult}'.encode('utf-8')
    except ZeroDivisionError:
        content = f'Нельзя делить на ноль'.encode('utf-8')
    except NameError:
        content = f'Введите арифмитическое выражение'.encode('utf-8')
    except SyntaxError:
        content = f'Введите арифмитическое выражение'.encode('utf-8')



    HDRS = 'HTTP/1.0 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')
    client_socket.send(HDRS + content)
    client_socket.close()

