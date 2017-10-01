# create Enemy class
class Enemy:
    life = 3

    # similar with constructor in Java
    def __init__(self, power):
        self.power = power
        print('Enemy ready')

    def attack(self):
        print('Ouch!')
        self.life -= 1

    def show_power(self):
        print('my power on level ' + str(self.power))

    def check_life(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life) + ' life left')


# create an object Enemy
enemy1 = Enemy(1)
enemy2 = Enemy(5)

enemy1.attack()
enemy1.attack()
enemy1.check_life()
enemy2.check_life()
enemy1.show_power()
enemy2.show_power()


# inheritance
class Parent:

    # PyCharm suggest 'static' coz the method didn't use 'self' attributes
    def print_last_name(self):
        print('Indra')


class Child(Parent):

    def print_first_name(self):
        print('Happy')


happy = Child()
happy.print_first_name()
happy.print_last_name()


# Multiple inheritance
class Mario:

    def move(self):
        print('I am move')


class Shroom:

    def eat_shroom(self):
        print('Now I am big!')


class BigMario(Mario, Shroom):
    pass    # Use 'pass' if you want just declare an empty class

bm = BigMario()
bm.move()
bm.eat_shroom()
