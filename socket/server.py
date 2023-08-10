import socket
import threading

host = 'localhost'
port = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
    
clients = []
aliases= []
    


def broadcast(message):
    for client in clients:
        client.send(message)
        

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room'.encode('utf-8'))
            aliases.remove(alias)
            break
        


def receive():
    while True:
        print("Server is running and listening")
        
        client ,addres = s.accept()
        print(f'Connection established with {str(addres)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)   
        aliases.append(alias)
        clients.append(client)
        print(f'Alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected chat room!'.encode('utf-8'))
        client.send(f'You are connected to chat room'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()



if __name__ == '__main__':
    receive()        
            
            
            
            
        