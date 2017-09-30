# create Enemy class
class Enemy:
    life = 3

    def attack(self):
        print('Ouch!')
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life) + ' life left')


# create an object Enemy
enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.check_life()
enemy2.check_life()
