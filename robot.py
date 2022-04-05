from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.active_weapon = Weapon("Energy Sword", 50)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacked {dinosaur.name} with an {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
        print(f'{dinosaur.name} has {dinosaur.health} health remaining!')
