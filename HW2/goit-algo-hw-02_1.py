import queue
import random
import time
import threading
import keyboard


class RequestProcessor:
    def __init__(self):
        self.queue = queue.Queue()
        self.request_id = 0
        self.running = True

    def generate_request(self):
        """Генерує нову заявку та додає її до черги."""
        self.request_id += 1
        new_request = f"Request-{self.request_id}"
        self.queue.put(new_request)
        print(f"Заявка {new_request} додана до черги.")

    def process_request(self):
        """Обробляє заявку з черги, якщо вона не пуста."""
        if not self.queue.empty():
            current_request = self.queue.get()
            print(f"Обробка заявки: {current_request}")
            time.sleep(random.uniform(0.5, 1.5))  # Імітація часу обробки
            print(f"Заявка {current_request} оброблена.")
        else:
            print("Черга порожня, немає заявок для обробки.")

    def check_exit(self):
        """Перевіряє натискання Esc у окремому потоці."""
        while self.running:
            if keyboard.is_pressed("esc"):
                self.running = False
                print("\nСистема обробки заявок завершується...")
                break
            time.sleep(0.1)  # Уникнення надмірного використання процесора

    def run(self):
        """Основний цикл програми."""
        print("Система обробки заявок запущена. Натисніть Esc для виходу.")
        # Запуск потоку для перевірки натискання Esc
        exit_thread = threading.Thread(target=self.check_exit, daemon=True)
        exit_thread.start()

        try:
            while self.running:
                # Генерація нових заявок з випадковим інтервалом
                if random.choice([True, False]):
                    self.generate_request()

                # Обробка наявних заявок
                self.process_request()

                # Затримка перед наступним циклом
                time.sleep(1)
        finally:
            self.cleanup()

    def cleanup(self):
        """Очищення черги перед завершенням програми."""
        print("Очищення черги...")
        while not self.queue.empty():
            discarded_request = self.queue.get()
            print(f"Заявка {discarded_request} вилучена з черги.")
        print("Програма завершена.")


if __name__ == "__main__":
    processor = RequestProcessor()
    processor.run()
