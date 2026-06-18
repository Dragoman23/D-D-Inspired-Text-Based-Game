import os
import subprocess
import random
from turtle import up

inventory = ["small dagger"]
gold = 0
level = 1
experience = 0
weapon = None   

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

def check_level_up():
    global level, experience
    xp_needed = level * 100
    if experience >= xp_needed:
        level += 1
        experience -= xp_needed
        print(f"Congratulations! You've leveled up to level {level}!")

def start():
    clear_screen()
    print("Welcome to our D&D based text adventure game")
    print("In this game, you will embark on a thrilling adventure filled with quests, battles, and mysteries.")
    print("You will create your own character, choose your class, and explore a vast world full of danger and excitement.")
    print("To play the game, simply follow the prompts and make choices that will shape your character's journey.")
    print("Are you ready to begin your adventure? (yes/no)")
    choice1 = input("> ").lower()
    if choice1 == 'yes':
        print("Great! Let's get started!")
        print("There are a couple commands you need to know before we start:")
        print("- 'help' - shows a list of available commands")
        print("- 'quit' - exits the game")
        print("-'inventory' - shows your current inventory")
        print("-'stats' - shows your current stats")
    else:     
        print("No worries! Take your time and come back when you're ready to embark on your adventure.")

clear_screen()

def create_character():
    print("First, we need to create your character.")
    name = input("What will your character's name be: ")
    print(f"Welcome, {name}! Now you need to choose your character's class.")
    character_class = input("Choose your class (to see the options, type classes): ")
    if character_class.lower() == 'classes':
        print("Here are the available classes:")
        print("-Barbarian: A rage-fueled front-liner with immense health who excels at brutal, straightforward combat.")
        print("-Fighter: A master of weapons and armor. They are highly adaptable and can fit almost any combat style.")
        print("-Monk: A disciplined martial artist who uses speed, agility, and supernatural Ki to stun enemies.")
        print("-Paladin: A holy warrior who combines heavy armor, melee strikes, divine healing, and protective spells.")
        print("-Ranger: A skilled survivalist who excels in wilderness tracking, archery, and nature-themed support magic.")
        
        print("-Bard: A musical, charismatic jack-of-all-trades. They are incredibly versatile and excel at both magic and party support.")
        print("-Cleric: An armored divine caster. While they are the ultimate party healer, they can also pack a serious magical punch.")
        print("-Druid: A nature-wielding caster who can harness the elements and shapeshift into wild beasts.")
        print("-Sorcerer: An innate magic user who can warp and alter their spells on the fly using metamagic.")
        print("-Warlock: A spellcaster who made a pact with an otherworldly patron, granting them unique, customizable magical abilities.")
        print("-Wizard: An academic spellcaster who learns the most complex arcane spells by studying a vast spellbook.")

        print("-Rogue: The ultimate stealth and utility class. They excel at lockpicking, disarming traps, and dealing massive surprise damage.")
        print("-Artificer: A brilliant inventor and tinkerer who crafts magical items and infuses weapons with special properties.")
        character_class = input("Now that you know the options, choose your class: ")
        print(f"Great choice! You have chosen to be a {character_class}.")

    print("Now you have to roll your character's stats. You will roll 1d18 for each stat: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma.")
    strength = random.randint(1, 18)
    dexterity = random.randint(1, 18) 
    constitution = random.randint(1, 18)
    intelligence = random.randint(1, 18)
    wisdom = random.randint(1, 18)
    charisma = random.randint(1, 18)
    print(f"Your character's stats are: Strength: {strength}, Dexterity: {dexterity}, Constitution: {constitution}, Intelligence: {intelligence}, Wisdom: {wisdom}, Charisma: {charisma}")
    return name, character_class, strength, dexterity, constitution, intelligence, wisdom, charisma
def use_item(item):
    global weapon
    if item == 'small dagger':
        weapon = "small dagger"
        print("You have equipped the small dagger to your weapon slot. It is a basic weapon that can be used for close combat. It has a damage of 1d4.")

def describe_item(item):
    if item == 'small dagger':
        print("The small dagger is a basic melee weapon. It is lightweight and easy to handle, making it ideal for quick strikes and surprise attacks. It has a damage of 1d4 and can be used for close combat. It is a common weapon among adventurers and can be found in most shops. Value: 1 gold piece.")
def enter_shop():
    global gold, inventory
    print("You enter the shop and see a variety of items for sale. The shopkeeper greets you and asks if you need any help finding anything. You see a small dagger for sale for 1 gold piece, a short sword for 5 gold pieces, a longsword for 10 gold pieces, a greatsword for 20 gold pieces, a bow for 5 gold pieces, and a staff for 5 gold pieces. To buy an item, type 'buy item', to sell an item, type 'sell item', or to leave the shop, type 'leave shop'.")
    shop_action = input("> ").lower()
    if shop_action == 'buy item':
        print("Which item would you like to buy?")
        item_to_buy = input("> ").lower()
        if item_to_buy == 'small dagger':   
            if gold >= 1:
                inventory.append('small dagger')
                gold -= 1
                print("You have bought a small dagger and added it to your inventory.")
            else:
                print("You don't have enough gold to buy that item.")
        elif item_to_buy == 'short sword':
            if gold >= 5:
                inventory.append('short sword')
                gold -= 5
                print("You have bought a short sword and added it to your inventory.")
            else:
                print("You don't have enough gold to buy that item.")
        elif item_to_buy == 'longsword':
            if gold >= 10:
                inventory.append('longsword')
                gold -= 10
                print("You have bought a longsword and added it to your inventory.")
            else:
                print("You don't have enough gold to buy that item.")
        elif item_to_buy == 'greatsword':
            if gold >= 20:
                inventory.append('greatsword')
                gold -= 20
                print("You have bought a greatsword and added it to your inventory.")
            else:
                print("You don't have enough gold to buy that item.")
        elif item_to_buy == 'bow':
            if gold >= 5:
                inventory.append('bow')
                gold -= 5
                print("You have bought a bow and added it to your inventory.")
            else:
                print("You don't have enough gold to buy that item.")
        elif item_to_buy == 'staff':
            if gold >= 5:
                inventory.append('staff')
                gold -= 5
                print("You have bought a staff and added it to your inventory.")
            else:
                print("You don't have enough gold to buy that item.")
        else:
            print("That item is not for sale in the shop.")

def game_main(name, character_class, strength, dexterity, constitution, intelligence, wisdom, charisma):
    global gold, inventory, level, experience, complete_quest6, weapon
    complete_quest6 = False
    print(f"Now that you have created your character, {name} the {character_class}, it's time to start your adventure!")
    print("You find yourself in the corner of a small alleyway. The sun is setting, and the city streets are filling with the sounds of adventurers and merchants. You see a group of adventurers standing around a notice board, looking at the various quests posted on the board. You only remember a few things: your name, class, stats, and the fact that you are an adventurer. You have no memory of how you got here or what your past is. You have no items in your inventory beside a small dagger.")
    while True:
        print("What do you do? (type 'stats' to check your stats, 'inventory' to check your inventory,'notice board' to approach the notice board to see the quests available, or 'shop' to go to the shop to buy items.)")
        action = input("> ").lower()
        if action == "shop":
            enter_shop()
        if action == 'stats':
            print(f"Your stats are: Strength: {strength}, Dexterity: {dexterity}, Constitution: {constitution}, Intelligence: {intelligence}, Wisdom: {wisdom}, Charisma: {charisma}, and you have {gold} gold pieces.")
        if action == 'inventory':
            if len(inventory) == 0:
                print("Your inventory is currently empty.") 
            else:
                print("Your inventory contains:")
                for items in inventory:
                    print(f"-{items}")
                print("To use an item, type 'use item', to read the item description, type 'item description'.")
                inventory_action = input("> ").lower()
                if inventory_action == 'use item':
                    print("Which item would you like to use?")
                    item_to_use = input("> ").lower()
                    if item_to_use in inventory:
                        use_item(item_to_use)
                        # Add item effects here
                    else:
                        print("You don't have that item in your inventory.")
                elif inventory_action == "item description":
                    print("Which item would you like to read the description of?")
                    item_to_describe = input("> ").lower()
                    if item_to_describe in inventory:
                        describe_item(item_to_describe)
                    else:
                        print("You don't have that item in your inventory.")
        if action == 'notice board':
            print("You approach the notice board and see several quests posted on it:")
            print("- Quest 1: Retrieve the lost artifact from the ancient ruins(S-Tier).")
            print("- Quest 2: Defeat the bandit leader terrorizing the nearby village(A-Tier).")
            print("- Quest 3: Escort a merchant caravan through dangerous territory(B-Tier).")
            print("- Quest 4: Investigate the mysterious disappearances in the haunted forest(C-Tier).")
            print("- Quest 5: Kill five rabbits for the local butcher(D-Tier).")
            print("- Quest 6: Gather rare herbs for a local alchemist(F-Tier).")

            print("Which quest do you want to take? (type the quest number)")
            current_quest = input("> ").lower()
            if current_quest == '1':
                if level < 10:
                    print("You are not high enough level to take this quest. You need to be at least level 10 to take this quest.")
                else:
                    print("You have chosen to retrieve the lost artifact from the ancient ruins. This is a S-Tier quest, which means it is very difficult and will require a lot of skill and preparation. You will need to gather information about the ruins, find a way to get there, and prepare for the dangers that await you inside.")

            if current_quest == '2':
                if level < 8:
                    print("You are not high enough level to take this quest. You need to be at least level 8 to take this quest.")
                else:
                    print("You have chosen to defeat the bandit leader terrorizing the nearby village. This is an A-Tier quest, which means it is difficult and will require a good amount of skill and preparation. You will need to gather information about the bandits, find their hideout, and prepare for the battle against the bandit leader and his minions.")

            if current_quest == '3':
                if level < 6:
                    print("You are not high enough level to take this quest. You need to be at least level 6 to take this quest.")
                else:
                    print("You have chosen to escort a merchant caravan through dangerous territory. This is a B-Tier quest, which means it is moderately difficult and will require some skill and preparation. You will need to gather information about the route, prepare for potential ambushes, and protect the merchant caravan from any threats that may arise.")
            
            if current_quest == '4':
                if level < 4:
                    print("You are not high enough level to take this quest. You need to be at least level 4 to take this quest.")
                else:
                    print("You have chosen to investigate the mysterious disappearances in the haunted forest. This is a C-Tier quest, which means it is somewhat difficult and will require some skill and preparation. You will need to gather information about the disappearances, find the source of the supernatural activity, and prepare for the challenges that await you in the forest.")

            if current_quest == '5':
                if level < 2:
                    print("You are not high enough level to take this quest. You need to be at least level 2 to take this quest.")
                else:
                    print("You have chosen to kill five rabbits for the local butcher. This is a D-Tier quest, which means it is relatively easy and will require minimal skill and preparation. You will need to find the rabbits, kill them, and bring them back to the butcher.")
            
            if current_quest == '6':
                if complete_quest6 == True:
                    print("You have completed this quest already. Please choose a different quest.")
                else:
                    print("You have chosen to gather rare herbs for a local alchemist. This is an F-Tier quest, which means it is very easy and will require no skill or preparation. You will need to find the herbs, gather them, and bring them back to the alchemist.")
                    complete_quest6 = False
                    print("To get more information about the quest, type 'find the alchemist'. To see the quest requirements, type 'quest requirements'.")
                    action_quest6 = input("> ").lower()
                    if action_quest6 == 'quest requirements':
                        quest_requirements_6 = ["Find the alchemist", "Gather 5 rare herbs", "Bring the herbs back to the alchemist"]
                        print("The quest requirements are:")
                        for requirements in quest_requirements_6:
                            print(f"-{requirements}")
                    if action_quest6 == 'find the alchemist':
                        print("You find the alchemist in his shop, which is located in the middle of the city. He is an old man with a long white beard and wise eyes. He tells you that the herbs you need to gather can be found in the forest outside of the city, but they are guarded by dangerous creatures. He gives you a map of the forest and some advice on how to find the herbs.")
                        print("What do you do? (type 'go to forest' to go to the forest, 'ask for more information' to ask the alchemist for more information about the quest, or 'go to shop' to go to the shop to buy supplies for the quest.)")
                        quest6_action = input("> ").lower()
                        if quest6_action == 'go to forest':
                            print("You follow the map and make your way to the forest. As you enter the forest, you can feel the danger lurking around you. You see a group of goblins guarding the herbs you need to gather. They are armed with crude weapons and are ready to attack you if you get too close.")
                            print("What do you do? (type 'attack goblins' to attack the goblins, 'sneak past goblins' to try to sneak past the goblins, or 'run away' to run away from the goblins.)")
                            goblin_action = input("> ").lower()
                            if goblin_action == 'attack goblins':
                                if weapon is None:
                                    print("You don't have a weapon equipped, so you are at a disadvantage in combat. The goblins easily overpower you and you are forced to retreat. You fail the quest and don't gain any experience.")
                                else: 
                                    print("You decide to attack the goblins head-on. You draw your small dagger and charge at them. The goblins are caught off guard by your sudden attack and are quickly defeated. You gather the herbs and make your way back to the alchemist.")
                                    if random.randint(1, 4) + strength > 10:
                                        complete_quest6 = True
                                        experience += 100
                                        gold += 5
                                        check_level_up()
                            
                            elif goblin_action == 'sneak past goblins':
                                print("You decide to try to sneak past the goblins. You carefully make your way around them, trying to stay hidden in the shadows. The goblins are focused on their task and don't notice you as you sneak past them. You successfully gather the herbs and make your way back to the alchemist.")
                                if random.randint(1, 6) + dexterity > 10:  
                                    complete_quest6 = True
                                    experience += 50
                                    check_level_up()
                            elif goblin_action == 'run away':
                                print("You decide that it's too dangerous to fight or sneak past the goblins, so you run away from them. You manage to escape safely, but you fail the quest and don't gain any experience.")
                    if complete_quest6 == True:
                        print("You have completed the quest and returned to the alchemist with the herbs. He thanks you for your help and gives you 5 gold pieces as a reward. You also gain 100 experience points for completing the quest.")
                        complete_quest6 = True
                        experience += 100
                        gold += 5
                        check_level_up()





start()
name, character_class, strength, dexterity, constitution, intelligence, wisdom, charisma = create_character()
game_main(name, character_class, strength, dexterity, constitution, intelligence, wisdom, charisma)