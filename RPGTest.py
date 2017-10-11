import random
import time

class Character():

    def __init__(self, character_name):
        self.name = character_name
        self.health = random.randint(18,22)
        self.armor_class = random.randint(14, 20)
        self.strength = random.randint(8, 24)
        self.dexterity = random.randint(8, 24)
        self.constitution = random.randint(8, 24)
        self.intelligence = random.randint(8, 24)
        self.wisdom = random.randint(8, 24)
        self.charisma = random.randint(8, 24)
        print("Name:", self.name, "Health:", self.health, "Armor Class:", self.armor_class, "Strength:", self.strength, "dexterity:", self.dexterity, "constitution:", self.constitution, \
              "intelligence:", self.intelligence, "wisdom:", self.wisdom, "charisma:", self.charisma)

def modifier_check(ability_score):
    if ability_score < 2:
        return -5
    elif ability_score < 4:
        return -4
    elif ability_score < 6:
        return -3
    elif ability_score < 8:
        return -2
    elif ability_score < 10:
        return -1
    elif ability_score < 12:
        return 0
    elif ability_score < 14:
        return 1
    elif ability_score < 16:
        return 2
    elif ability_score < 18:
        return 3
    elif ability_score < 20:
        return 4
    elif ability_score < 22:
        return 5
    elif ability_score < 24:
        return 6
    elif ability_score < 26:
        return 7
    else:
        return 8

def roll_d20():
    roll = random.randint(1,20)
    print("Die came up", roll)
    return roll

def roll_d6():
    return random.randint(1,6)

def Attack(attacker, defender):
    attacker_strength = attacker.strength
    defender_defense = defender.armor_class
    attack_roll = roll_d20() + modifier_check(attacker_strength)
    if attack_roll >= defender.armor_class:
        print("Hit! Rolled a", attack_roll, "vs. defender's", defender.armor_class)
        damage = roll_d6()
        defender.health -= damage
        print ("Dealt", damage, "damage! defender health:", defender.health)
    else:
        print("Missed! Rolled a", attack_roll, "vs. defender's", defender.armor_class)

def Fight(user, enemy):
    character_taking_turn = user
    character_defending = enemy
    while user.health and enemy.health > 0:
        print("It's", character_taking_turn.name + "'s", "turn!")
        Attack(character_taking_turn, character_defending)
        new_defender = character_taking_turn
        character_taking_turn = character_defending
        character_defending = new_defender
        time.sleep(2)
    if user.health <= 0:
        print(user.name, "died! Fight over!")
    elif enemy.health <= 0:
        print(enemy.name, "died! Fight over!")




new_player = Character("Spencer")
orc = Character("Orc")

Fight(new_player, orc)


