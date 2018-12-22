from time import sleep

from src.models.units.buggy import Buggy
from src.models.units.soldier import Soldier
from src.models.units.tank import Tank


class Squad():
    "Represents units squad"
    def __init__(self, unit_type: str, color: str, att_strategy, number: int):
        self.unit_type = unit_type
        self.color = color
        self.att_strategy = att_strategy
        self.number = number
        self.is_ready = True
        self.is_alive = True
        self.units = self.create_squad()
        self.att_succ_prob = None
        self.recharge_time = self.get_squad_avg_recharge()

    def create_squad(self)-> list:
        l = []
        if self.unit_type == "soldier":
            for i in range(1, 11):
                l.append(Soldier(i, self.color))
        elif self.unit_type== "tank":
            for i in range(1, 5):
                l.append(Tank(i, self.color))
        else:
            for i in range(1, 6):
                l.append(Buggy(i, self.color))
        return l

    def compute_att_succ_prob(self):
        multiple_att_prob = 1
        #avg_att_prob = 0
        for unit in self.units:
            multiple_att_prob *= unit.compute_att_succ_prob()
            #avg_att_prob += unit.compute_att_succ_prob()
        return multiple_att_prob ** 1 / len(self.units) #GAVG works really bad for different size squads
        #return avg_att_prob / len(self.units) # avg works worse

    def attack(self, enemy_squad):
        if self.compute_att_succ_prob() > enemy_squad.compute_att_succ_prob():
            enemy_squad.under_attack(self.damage())
            self.increment_experience()
            print(f"{self} has attacked {enemy_squad}")
        else:
            print(f"{self} has failured to attack {enemy_squad}")
        self.squad_ready = False
        self.recharging()

    def increment_experience(self):
        for unit in self.units:
            unit.increment_experience()

    def recharging(self):
        sleep(self.recharge_time)
        self.squad_ready = True

    def damage(self):
        tot_damage = 0
        for unit in self.units:
            tot_damage += unit.damage()
        return tot_damage

    def under_attack(self, damage):
        self.is_alive = self.is_active()
        if self.is_alive:
            damage_to_unit = damage / len(self.units)
            for unit in self.units:
                unit.under_attack(damage_to_unit)

    def is_active(self):
        temp = None
        for unit in self.units:
            if unit.is_active():
                temp = True
                break
            else:
                temp = False
        return temp

    def get_squad_avg_recharge(self):
        avg_recharge = 0
        for unit in self.units:
            avg_recharge += unit.recharge
        return avg_recharge / len(self.units)

    def get_readiness(self):
        return self.is_ready

    def __repr__(self):
        return f"{self.units[0].__class__.__name__} squad #{self.number} for {self.color} army"

