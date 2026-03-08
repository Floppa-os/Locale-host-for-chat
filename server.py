# server.py
import socket
import threading
from config import HOST, PORT, BUFFER_SIZE
from colorama import init, Fore, Back, Style
print(HOST)
class MessengerServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []  # Список подключённых клиентов (сокетов)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"[SERVER] Запущен на {self.host}:{self.port}")

        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"[SERVER] Подключение от {client_address}")
                self.clients.append(client_socket)
                # Запускаем поток для каждого клиента
                thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket,)
                )
                thread.start()
        except KeyboardInterrupt:
            print("[SERVER] Сервер остановлен.")
        finally:
            self.shutdown()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
                if message:
                    print(f"[CLIENT] {message}")
                    self.broadcast(message, client_socket)
                else:
                    break
            except:
                break
        # Клиент отключился
        self.clients.remove(client_socket)
        client_socket.close()

    def broadcast(self, message, sender_socket):
        """Отправляет сообщение всем клиентам, кроме отправителя"""
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()
                    self.clients.remove(client)

    def shutdown(self):
        for client in self.clients:
            client.close()
        self.server_socket.close()

if __name__ == "__main__":
    server = MessengerServer(HOST, PORT)
    server.start()
