from random import randint

from src.models.units.soldier import Soldier
from src.models.units.vehicle import Vehicle


class Tank(Vehicle):
    def __init__(self, number, color):
        super(Tank, self).__init__(number, color)
        self.operators = [Soldier(1, self.color),
                          Soldier(2, self.color),
                          Soldier(3, self.color)]

    def __repr__(self):
        return f"Tank #{self.number} from {self.color} team"

    def set_recharge(self):
        return randint(1000, 5000) / 1000

