import random


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)
        print(random.randrange(self.atkl, self.atkh))

    def getHp(self):
        print(self.hp)


enemy1 = Enemy(60, 80)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(45, 70)
enemy2.getAtk()



playerhp = 260
enemyatkl = 60
enemyatkh = 80


# while playerhp > 0:





