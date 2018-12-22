
from src.models.army import Army
from src.models.battlefield import Battlefield


def main():
    armies, strategy, squads = greetings()
    battlefield = Battlefield(armies, squads, strategy)
    battlefield.start_battle()
    #print('Hello')
    #greetings()
    #a1 = Army('green', 1, 'w')
    #a2 = Army('yellow', 1, 's')
    #while(not a1.is_destroyed or a2.is_destroyed()):
    #    a1.attack(a2)
    #    a2.attack(a1)


def greetings():
    """Greets user and explains what user can do"""
    print("Welcome to the greates battle simulator in the history of this third planet from the sun!")
    print ("I'm going to ask you some numbers, which are needed for computation.")

    armies_num = int(input("Please enter number of armies in range(2..8):\n"))
    attack_strategy = input("Attack strategy: 'weakest', 'strongest', 'random'\n")
    attack_strategy = attack_strategy.strip()[:1]
    number_of_squads = int(input("Please determine number of squads per each army: \n"))

    print(attack_strategy)
    return (armies_num, attack_strategy, number_of_squads)

main()
