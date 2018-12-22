from random import randint, choice

from src.models.units.unit import Unit

class Vehicle(Unit):
    """Class which represents base vehicle object"""
    def __init__(self, number, color):
        super(Vehicle, self).__init__(number, color)
        self.operators = []
        self.total_health = self.compute_health()
        self.is_alive = True

    def compute_health(self):
        temp_health = 0
        for operator in self.operators:
            temp_health += operator.health
        return (self.health + temp_health) / (len(self.operators) + 1)

    def get_alive_oper(self):
        return [x for x in self.operators if x.is_active()]

    def alive(self):
        if not self.is_active():
            self.is_alive = False

    def is_active(self):
        if self.health > 0:
            temp_value = False
            for operator in self.operators:
                temp_value = temp_value or operator.is_active()
            return temp_value
        else:
            for operator in self.operators:
                operator.health = 0
            return False

    def compute_att_succ_prob(self):
        mult_atack_success = 1
        for operator in self.get_alive_oper():
            mult_atack_success *= operator.compute_att_succ_prob()
        return 0.5 * (1 + self.compute_health() / 100) * (mult_atack_success ** 1/len(self.operators)) # GAVG


    def attack(self, enemy_unit: Unit):
        if self.compute_att_succ_prob() > enemy_unit.attack_success_prob():
            enemy_unit.under_attack(self.damage())

    def increment_experience(self):
        for operator in self.get_alive_oper():
            operator.increment_experience()

    def damage(self):
        sum_oper_exp = 0
        for operator in self.get_alive_oper():
            sum_oper_exp += (operator.experience /100)
        return 1.1 + sum_oper_exp

    def under_attack(self, damage):
        self.alive()
        if self.is_alive:
            self.health -= damage * 0.6
            alive_operators = self.get_alive_oper()
            temp_operator = choice(alive_operators)
            temp_operator.under_attack(damage * 0.2)
            for operator in alive_operators:
                if temp_operator is operator:
                    continue
                else:
                    operator.under_attack(damage * 0.1)


#v = Vehicle(1, 'green')
#print(v)