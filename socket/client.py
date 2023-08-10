import socket
import threading

host = 'localhost'
port = 65432

alias = input("choose aliases >> ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def client_receive():
    while True:
        try:
            message  = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error")
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}:{input("")}'
        client.send(message.encode('utf-8'))
        


receive_thread = threading.Thread(target=client_receive)

send_thread = threading.Thread(target=client_send)


receive_thread.start()
send_thread.start()