from player import Player
from player import attackMonster
from monster import Monster
from monster import attackPlayer

# Function for printing the stats at the beginning of the fight
def printStats(player, monster):
    print('\n\t\t\t', player.name, '\t\t', monster.name)
    print('Health:\t\t  ', player.health, '\t\t\t\t', monster.health)
    print('Strength:\t  ', player.strength, '\t\t\t\t', monster.strength)
    print('Defence:\t  ', player.defence, '\t\t\t\t', monster.defence)
    print('Luck:\t\t  ', player.luck, '\t\t\t\t', monster.luck)

# Function for handling the fight between the Player and the Monster
def fighting(player, monster):
    turns = 0

    # as long as the Player and the Monster are not dead, the fight continues
    while (not monster.isDead()) and (not player.isDead()):
        attackMonster(player, monster)
        attackPlayer(player, monster)
        turns += 1
        #the game ends if nobody won after 20 turns
        if turns == 20:
            print('The game ended, it reached 20 turns!')
            return

# main function
def main():
    player = Player('Player')
    monster = Monster('Monster')

    printStats(player, monster)
    print()

    fighting(player, monster)

if __name__ == '__main__':
    main()