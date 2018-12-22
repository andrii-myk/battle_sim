from random import randint

class Unit():
    """Base class for all units"""
    def __init__(self, number, color):
        self.health = 100
        self.recharge = self.set_recharge()
        self.number = number
        self.color = color
        self.attack_success_prob = None

    def set_recharge(self):
        return randint(100, 2000)/1000

    def under_attack(self, damage):
        self.health -= damage
