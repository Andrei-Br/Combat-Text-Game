import random

#base class
class Creature():
    """base class"""
    def __init__(self, name, health, strength, defence, speed, luck):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.luck = luck

    #  return True if Creature has no health left
    def isDead(self):
        return self.health <= 0

    #  reduce the Creature's health
    def reduceHealth(self, strength):
        # calculate the damage done with the formula:
        # Damage = Attacker_strength – Defender_defence
        self.health = self.health - (strength - self.defence)

    #  access function for printing the remaining health
    def getHealth(self):
        print(self.name, 'has', self.health, 'health remaining.\n')

    #  return True if the Creature got lucky
    def gotLucky(self):
        return random.randint(0, 100) < self.luck

    #  function for attacking once
    def single_attack(self, attacked):
        attacked.reduceHealth(self.strength)
        print(self.name, 'hit', attacked.name, 'for', (self.strength
              - attacked.defence), 'damage.')

    #  function for handling the dodging
    def dodge(self, attacker):
        print(self.name, 'got lucky and dodged the attack of', attacker.name
              + '.\n')
        return

    #  rapid strikes means the attacker gets to attack the target twice
    def rapid_strike(self, attacked):
        print(self.name, 'got lucky! He used Rapid Strike and attacked twice!')
        attacked.reduceHealth(self.strength)
        print(self.name, 'hit', attacked.name, 'for', (self.strength
              - attacked.defence), 'damage.')
        attacked.reduceHealth(self.strength)
        print(self.name, 'hit', attacked.name, 'for', (self.strength
              - attacked.defence), 'damage.')

    #  magic shield means the attacked creature receives half damage
    def magic_shield(self, attacker):
        print(self.name, 'got lucky! He used Magic Shield and took half the '
                         'damage!')
        self.health = self.health - ((attacker.strength - self.defence) / 2)
        print(attacker.name, 'hit', self.name, 'for', ((attacker.strength
              - self.defence) / 2), 'damage.')