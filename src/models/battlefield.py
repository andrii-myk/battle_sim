import threading
from random import choice
from src.models.army import Army

class Battlefield():
    def __init__(self, num_armies: int, num_squads: int, att_mode: str):
        self.num_armies = num_armies
        self.num_squads = num_squads
        self.att_mode = att_mode
        self.colors = ('green', 'blue', 'yellow', 'red', 'violet', 'black', 'brown', 'pink')
        self.armies = self.create_armies()

    def create_armies(self):
        armies = []
        for i in range(0, self.num_armies):
            if i > 8:
                break
            armies.append(Army(self.colors[i], self.num_squads, self.att_mode))
        return armies

    def start_battle(self):
        while(len(self.armies) > 1):
            for army in self.armies:
                t = threading.Thread(target=army.attack, args=((army.choice_army_to_attack(self.armies),)))
                t.start()




