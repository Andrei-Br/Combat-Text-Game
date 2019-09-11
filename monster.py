import random
from creature import Creature

#derived monster class
class Monster(Creature):
    """constructor for Monster class"""
    def __init__(self, name):
        self.name = name
        """generate random stats each fight for the Monster"""
        self.health = random.randrange(90, 121)
        self.strength = random.randrange(80, 96)
        self.defence = random.randrange(30, 46)
        self.luck = random.randrange(25, 41)

# function handling the Monster attacking the Player
def attackPlayer(player, monster):
    print("Monster's turn: ", end="")
    # if the Monster is dead, he cannot attack
    if monster.isDead():
        return

    #  If the Player gets lucky, he has a chance of dodging the attack
    if player.gotLucky():
        player.dodge(monster)
        return

    # if the Player didn't dodge, the fight will continue
    # The Player has a 20% chance of blocking half of the incoming damage
    if random.randint(0, 100) < 20:
        player.magic_shield(monster)
    # else, the Player takes full damage
    else:
        monster.single_attack(player)

    if player.isDead():
        print(monster.name, 'won the fight.\n')
        return

    # print the remaining health of the Player
    player.getHealth()