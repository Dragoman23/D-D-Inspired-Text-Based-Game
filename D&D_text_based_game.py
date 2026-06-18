import os
import subprocess

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

#def create_character():


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
