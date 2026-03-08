# main
import sys
import colorama
from colorama import Fore


def main():
    print("Добро пожаловать в локальный мессенджер!")
    print("1. Запустить сервер")
    print("2. Подключиться к серверу")

    choice = input("Выберите действие (1 или 2): ").strip()

    if choice == "1":
        print("Запускаем сервер...")
        import server
        server.MessengerServer(HOST, PORT).start()
    elif choice == "2":
        print("Подключаемся к серверу...")
        import client
        client.MessengerClient(HOST, PORT).connect()
    else:
        print(Fore.RED + "Неверный выбор. Завершаем работу.")
        sys.exit(1)


if __name__ == "__main__":
    from config import HOST, PORT

    main()
