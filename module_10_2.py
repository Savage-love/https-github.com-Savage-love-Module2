import threading
import time

class Knight(threading.Thread):
    enemies = 100  # Общее количество врагов для всех рыцарей
    lock = threading.Lock()  # Блокировка для синхронизации доступа к общему ресурсу

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies_2 = self.enemies

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies_2 > 0:
            with Knight.lock:
                if self.enemies_2 > 0:
                    self.enemies_2 -= self.power
                    self.days += 1
                    remaining_enemies = max(self.enemies_2, 0)
                    print(f"{self.name} сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")
            time.sleep(1)  # Задержка в 1 секунду
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

# Создание и запуск потоков
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")