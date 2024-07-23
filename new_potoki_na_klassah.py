from threading import Thread
from time import sleep

# Класс Knight ведёт сражение. Будет 2 потока. Всего 100 врагов.
# Каждый день количество врагов уменьшается на power. Каждый день длится 1 сек.

INVADERS = 100
day = 0


class Knight(Thread):
    '''Здесь описываем атрибуты'''
    def __init__(self, name, power, *args, **kwargs):
        super(Knight, self).__init__(name, power)
        self.name = name  # имя
        self.power = power  # на сколько будет уменьшаться количество врагов каждый день

    def run(self):
        """При запуске метода выводится надпись с именем рыцаря и что на нас напали"""

        print(f"{self.name}, на нас напали!")

        self.INVADERS = 100
        self.day = 0
        while self.INVADERS > 0:
            self.day = self.day + 1
            self.INVADERS = self.INVADERS - self.power
            print(f"{self.name} сражается {self.day} дней, осталось {self.INVADERS} воинов")







knight1 = Knight(name='Sir Lanselot', power=10)
knight2 = Knight(name='Sir Galahad', power=20)


knight1.start()
knight2.start()


knight1.join()
knight2.join()