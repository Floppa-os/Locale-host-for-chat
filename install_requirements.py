#!/usr/bin/env python3
"""
Скрипт для установки зависимостей мессенджера.
В текущей реализации мессенджера сторонние библиотеки не требуются.
Скрипт приведён на случай будущего расширения.
"""

import subprocess
import sys
import os



def check_python_version():
    """Проверяет версию Python (минимум 3.6)."""
    major, minor = sys.version_info.major, sys.version_info.minor
    if major < 3 or (major == 3 and minor < 6):
        print(f"[ОШИБКА] Требуется Python 3.6+, у вас {major}.{minor}.")
        sys.exit(1)
    print(f"[ОК] Python {major}.{minor} — подходит.")



def install_packages(packages):
    """Устанавливает список пакетов через pip."""
    if not packages:
        print("[INFO] Нет пакетов для установки.")
        return

    print("[INSTALL] Устанавливаю пакеты: " + ", ".join(packages))
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", *packages
        ])
        print("[ОК] Все пакеты установлены.")
    except subprocess.CalledProcessError as e:
        print(f"[ОШИБКА] Не удалось установить пакеты: {e}")
        sys.exit(1)



def main():
    print("=== Установка зависимостей мессенджера ===\n")

    # Проверка Python
    check_python_version()

    # Список пакетов для возможных расширений
    # (в текущей версии мессенджера они НЕ нужны)
    recommended_packages = ['colorama']
        # 'tkinter' — встроен, не устанавливается через pip
        # 'pyqt5' or 'pyside6' — для GUI
        # 'loguru' — для логирования
        # 'python-dotenv' — для переменных окружения

    # Если вы добавите GUI или другие зависимости — внесите их сюда
    # Пример:
    # recommended_packages = ['pyqt6', 'loguru']

    if recommended_packages:
        install_packages(recommended_packages)
    else:
        print("[INFO] Сторонние пакеты не требуются (используются встроенные модули).")

    print("\n=== Готово ===")



if __name__ == "__main__":
    main()
