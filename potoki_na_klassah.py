""" Два потока - рыцаря"""



from threading import Thread
from time import sleep


INVADERS = 100
day = 0


class Knight(Thread):

    def __init__(self, name, skills, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skills = skills

    def run(self):
        while INVADERS > 0:
            day = day + 1
            INVADERS = INVADERS - self.skills
            print(day)
            print(INVADERS)


knight1 = Knight(name='Sir Lanselot', skills=10)
knight2 = Knight(name='Sir Galahad', skills=20)


knight1.start()
knight2.start()


knight1.join()
knight2.join()


