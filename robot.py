from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.active_weapon = Weapon('Energy Sword', 50)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon