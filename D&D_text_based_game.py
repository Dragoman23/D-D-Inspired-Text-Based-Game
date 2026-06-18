import os
import subprocess
import random

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

def create_character():
    print("First, we need to create your character.")
    name = input("What will your character's name be: ")
    print(f"Welcome, {name}! Now you need to choose your character's class.")
    character_class = input("Choose your class (to see the options, type classes): ")
    if character_class.lower() == 'classes':
        print("Here are the available classes:")
        print("-Barbarian:A rage-fueled front-liner with immense health who excels at brutal, straightforward combat.")
        print("-Fighter: A master of weapons and armor. They are highly adaptable and can fit almost any combat style.")
        print("-Monk: A disciplined martial artist who uses speed, agility, and supernatural Ki to stun enemies.")
        print("-Paladin: A holy warrior who combines heavy armor, melee strikes, divine healing, and protective spells.")
        print("-Ranger: A skilled survivalist who excels in wilderness tracking, archery, and nature-themed support magic.")
        
        print("-Bard: A musical, charismatic jack-of-all-trades. They are incredibly versatile and excel at both magic and party support.")
        print("-Cleric: An armored divine caster. While they are the ultimate party healer, they can also pack a serious magical punch.")
        print("-Druid: A nature-wielding caster who can harness the elements and shapeshift into wild beasts.")
        print("-Sorcerer:An innate magic user who can warp and alter their spells on the fly using metamagic.")
        print("-Warlock:A spellcaster who made a pact with an otherworldly patron, granting them unique, customizable magical abilities.")
        print("-Wizard:An academic spellcaster who learns the most complex arcane spells by studying a vast spellbook.")

        print("-Rogue: The ultimate stealth and utility class. They excel at lockpicking, disarming traps, and dealing massive surprise damage.")
        print("-Artificer:A brilliant inventor and tinkerer who crafts magical items and infuses weapons with special properties.")
        character_class = input("Now that you know the options, choose your class: ")

        print("Now you have to roll your character's stats. You will roll 1d18 for each stat: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma.")
        strength = random.randint(1, 18)
        dexterity = random.randint(1, 18) 
        constitution = random.randint(1, 18)
        intelligence = random.randint(1, 18)
        wisdom = random.randint(1, 18)
        charisma = random.randint(1, 18)
        print(f"Your character's stats are: Strength: {strength}, Dexterity: {dexterity}, Constitution: {constitution}, Intelligence: {intelligence}, Wisdom: {wisdom}, Charisma: {charisma}")


    print(f"Great choice! You have chosen to be a {character_class}.")
    return name, character_class

def start():
    clear_screen()
    print("Welcome to our D&D based text adventure game")
    print("In this game, you will embark on a thrilling adventure filled with quests, battles, and mysteries.")
    print("You will create your own character, choose your class, and explore a vast world full of danger and excitement.")
    print("To play the game, simply follow the prompts and make choices that will shape your character's journey.")
    print("Are you ready to begin your adventure? (yes/no)")
    choice = input("> ").lower()
    if choice == 'yes':
        print("Great! Let's get started!")
        print("There are a couple commands you need to know before we start:")
        print("- 'help' - shows a list of available commands")
        print("- 'quit' - exits the game")
        print("-'inventory' - shows your current inventory")
        print("-'stats' - shows your current stats")
    else:     
        print("No worries! Take your time and come back when you're ready to embark on your adventure.")
