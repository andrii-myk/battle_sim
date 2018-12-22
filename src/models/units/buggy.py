from random import randint

from src.models.units.soldier import Soldier
from src.models.units.vehicle import Vehicle

class Buggy(Vehicle):
    def __init__(self, number, color):
        super(Buggy, self).__init__(number, color)
        self.operators = [Soldier(1, self.color),
                          Soldier(2, self.color)]

    def __repr__(self):
        return f"Buggy #{self.number} from {self.color} team"

    def set_recharge(self):
        return randint(1000, 2500) /1000