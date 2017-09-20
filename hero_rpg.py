#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__ (self, name):
        self.name = name

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Hero(Character):
    def __init__ (self, name):
        super().__init__(name)
        self.health = 10
        self.power = 5
        super().alive()

    def attack(self, enemy):
        super().attack(enemy)
        print("You do {} damage to the goblin.".format(self.power))

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    def __init__ (self, name):
        super().__init__(name)
        self.health = 6
        self.power = 2
        super().alive()

    def attack(self, enemy):
        super().attack(enemy)
        print("The goblin does {} damage to you.".format(self.power))

    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

class Zombie(Character):
    def __init__ (self):
        self.power = 1

    def attack(self, enemy):
        super().attack(enemy)
        print("The zombie does {} damage to you.".format(self.power))

def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    hero = Hero('Hero')
    goblin = Goblin('Goblin')
    zombie = Zombie()

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            zombie.attack(hero)
            if goblin.health <= 0:
                hero.print_status()
                print("The goblin is dead.")
        elif raw_input == "2":
            if hero.alive():
                zombie.attack(hero)
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()
