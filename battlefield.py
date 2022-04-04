from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
