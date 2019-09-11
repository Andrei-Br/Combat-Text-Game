import random
from creature import Creature

#derived player class
class Player(Creature):
    """constructor for Player class"""
    def __init__(self, name):
        self.name = name
        """generate random stats each fight for the Player"""
        self.health = random.randrange(100, 151)
        self.strength = random.randrange(70, 81)
        self.defence = random.randrange(35, 46)
        self.luck = random.randrange(10, 31)

# function handling the Player attacking the Monster
def attackMonster(player, monster):
    print("Player's turn: ", end="")
    # if the Player is dead, he cannot attack
    if player.isDead():
        return

    #  If the Monster gets lucky, he has a chance of dodging the attack
    if monster.gotLucky():
        monster.dodge(player)
        return

    #  If the Player gets lucky, he has a 10% chance of hitting Rapid Strike
    if random.randint(0, 100) < 10:
        player.rapid_strike(monster)
    else:
        # Else, the Player attacks the Monster only once
        player.single_attack(monster)

    if monster.isDead():
        print(player.name, 'won the fight.\n')
        return

    # print the remaining health of the Monster
    monster.getHealth()
