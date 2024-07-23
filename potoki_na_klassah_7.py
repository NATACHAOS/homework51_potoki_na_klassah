from time import sleep
from threading import Thread

"""Сражение двух рыцарей:
Создадим 2 потока для 2 рыцарей.
На каждого рыцаря нападают 100 врагов.
У каждого рыцаря есть умение (skills) убить определенное количество врагов в день.
На консоль выведется сколько дней сражается каждый рыцарь,
через сколько дней одержал победу.
Прошествие 1 секунды означает, что прошёл 1 день"""
class Knight(Thread):
    INVADERS = 100 # количество врагов у рыцарей одинаковое и равно 100
    day = 0 # это для счёта дней


# Задаём атрибуты
    def __init__(self, name, skills, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skills = skills

    # Прописываем метод для рыцарей
    def run(self):
        print(f"{self.name}, на нас напали!") # Надпись при запуске потока
        while self.INVADERS > 0: # пока количество врагов больше нуля:
            self.day = self.day + 1 # прибавляется день
            self.INVADERS = self.INVADERS - self.skills # и уменьшается количество врагов на
                                                        # умение (skills) убить определенное количество врагов в день
            print(f"{self.name} сражается {self.day} дней, "
                  f"осталось {self.INVADERS} воинов",
                  flush=True) # Пример Вывода на консоль: Sir Galahad сражается 5 дней, осталось 50 воинов
            sleep(1) # Прошествие 1 секунды означает, что прошёл 1 день
        print(f"{self.name} одержал победу спустя"
              f" {self.day} дней", flush=True) # Пример Вывода на консоль: Sir Lanselot одержал победу спустя 5 дней


t1 = Knight(name='Sir Lanselot', skills=20) # Первый поток для первого рыцаря
t2 = Knight(name='Sir Galahad', skills=10) # Второй поток для второго рыцаря

t1.start()
t2.start()

t1.join()
t2.join()

print("Все битвы закончились!") # Надпись в конце