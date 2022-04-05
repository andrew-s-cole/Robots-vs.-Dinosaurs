import random


class Dinosaur:
    def __init__(self, name, attack_power):
        self.attack_choice = ['Tail smash', 'Head bash', 'Bite']
        self.name = name
        self.attack_power = attack_power
        self.health = random.randrange(350, 500)

    def attack(self, robot):
        robot.health -= self.attack_power
        print(
            f'{self.name} attacked {robot.name} with a {self.attack_choice[random.randrange(0,3)]} for {self.attack_power} damage!')
        print(f'{robot.name} has {robot.health} health remaining!')
