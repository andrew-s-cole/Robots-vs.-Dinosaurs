from dinosaur import Dinosaur
from robot import Robot
import random


class Battlefield:
    def __init__(self):
        self.robot = Robot('RX-78-2')

        self.dinosaur = Dinosaur('Greymon', random.randrange(10,20))

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs!')

    def battle_phase(self):
        while (self.robot.health) > 0 and (self.dinosaur.health) > 0:

            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)

            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)

    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} crushed {self.robot.name}!')
            print(f'{self.dinosaur.name} wins!')

        elif self.dinosaur.health <= 0:
            print(f'{self.robot.name} obliterated {self.dinosaur.name}!')
            print(f'{self.robot.name} wins!')
