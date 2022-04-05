from weapon import Weapon
import random


class Robot:
    def __init__(self, name):
        self.weapon_choice = ['Energy Sword', 'Dash Attack', 'Rocket Fist', 'Energy Blast']
        self.name = name
        self.health = 300
        self.active_weapon = Weapon(self.weapon_choice[random.randrange(0, 3)], random.randrange(10,20))

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacked {dinosaur.name} with a {random.choice(self.weapon_choice)} for {self.active_weapon.attack_power} damage!')
        print(f'{dinosaur.name} has {dinosaur.health} health remaining!')
