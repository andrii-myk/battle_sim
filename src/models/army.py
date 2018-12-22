from random import randint, choice
from src.models.squad import Squad

class Army():
    def __init__(self, color: str, number_of_squads: int, att_type: str):
        self.color = color
        self.number_of_squads = number_of_squads
        self.att_type = att_type
        self.unit_types = ('soldier', 'tank', 'buggy')
        self.squads = self.create_army()

    def create_army(self):
        army = []
        for i in range(1, self.number_of_squads + 1):
            army.append(Squad(choice(self.unit_types), self.color, self.att_type, i))
        return army

    def get_strongest_squad(self):
        best_squad = self.squads[0]
        for squad in self.squads:
            if squad.damage() > best_squad.damage():
                best_squad = squad
        return self.squads.index(best_squad)

    def get_weakest_squad(self):
        weakest_squad: Squad = self.squads[-1]
        for squad in self.squads:
            if squad.damage() < weakest_squad.damage():
                weakest_squad = squad
        return self.squads.index(weakest_squad)

    def choice_army_to_attack(self, armies: list):
        target_army = None
        listt = armies[:]
        listt.pop(armies.index(self))
        listt.sort(key= lambda x: x.army_power())
        if self.att_type == 'w':
            target_army = armies[0]
        elif self.att_type == 's':
            target_army = armies[-1]
        else:
           target_army = choice(armies)
        return target_army


    def choice_target(self, enemy_army):
        target = None
        if self.att_type == 'w':
            target = enemy_army.get_weakest_squad()
        elif self.att_type == 's':
            target = enemy_army.get_strongest_squad()
        else:
            target = enemy_army.squads[randint(0, len(enemy_army.squads))]
        return target

    def attack(self, enemy_army):
        for squad in self.squads:
            if squad.is_alive:
                if squad.get_readiness():
                    squad.attack(enemy_army.squads[self.choice_target(enemy_army)])
                else:
                    continue
            else:
                print(f"{squad} was totally destroyed")
                self.squads.pop(self.squads.index(squad))

    def is_destroyed(self):
        if not self.squads:
            print(f"{self} was totally destroyed")
        return True

    def army_power(self):
        power = 0
        for squad in self.squads:
            power += squad.damage()
        return power

    def __repr__(self):
        return f"{self.color.capitalize()} army"







