# client.py
import socket
import threading
import sys
from colorama import init, Fore, Back, Style

from config import HOST, PORT, BUFFER_SIZE

class MessengerClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = input("Имя клиента: ")

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"[CLIENT] Подключён к {self.host}:{self.port}")
            # Отправляем никнейм на сервер
            self.client_socket.send(self.nickname.encode('utf-8'))

            # Потоки: приём и отправка сообщений
            threading.Thread(target=self.receive_messages, daemon=True).start()
            self.send_messages()
        except ConnectionRefusedError:
            print(Fore.RED + "[CLIENT] Не удалось подключиться к серверу. Проверьте, запущен ли сервер.")
        except Exception as e:
            print(Fore.RED + f"[CLIENT] Ошибка: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(BUFFER_SIZE).decode('utf-8')
                if message:
                    print(message)
            except:
                print(Fore.RED + "[CLIENT] Соединение разорвано.")
                break

    def send_messages(self):
        while True:
            message = input()
            if message.lower() == '/exit':
                self.client_socket.close()
                sys.exit()
            full_message = f"{self.nickname}: {message}"
            self.client_socket.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    client = MessengerClient(HOST, PORT)
    client.connect()
