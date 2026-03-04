import random
import os
import pickle
import time

def display_title():
    print("SHADOWS RISING")


def display_main_menu():
    print("\nMain Menu")
    print("1. Start Game")
    print("2. Load Game")
    print("3. End Credits")
    print("4. Quit")

class Mage:
    def __init__(self, name, min_damage, max_damage, deck_name, health_points, mana, accuracy, decks):
        self.name = name
        self.deck = decks[deck_name]
        self.spells = {}
        for spell in self.deck["spells"]:
            if "min_damage" in spell and "max_damage" in spell:
                spell_name = spell["name"]
                spell_data = (spell["min_damage"], spell["max_damage"])
                self.spells[spell_name] = spell_data
        self.healing_cards = self.deck["healing_cards"]
        self.health_points = health_points
        self.max_health_points = health_points
        self.mana = mana
        self.max_mana = mana
        self.accuracy = accuracy
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.status_effects = []
        self.level = 1

    def attack_damage(self):
        return random.randint(self.min_damage, self.max_damage)

    def level_up(self):
        if self.level < 5:
            self.level += 1
            self.health_points += 250
            self.max_health_points += 250
            self.mana += 10
            self.max_mana += 10
            self.health_points = self.max_health_points
            self.mana = self.max_mana
            print(f"{self.name} leveled up to level {self.level}! Health increased to {self.health_points}, mana increased to {self.mana}.")
        else:
            print(f"{self.name} is already at the maximum level!")

class Enemy:
    def __init__(self, name, health_points, min_damage, max_damage):
        self.name = name
        self.health_points = health_points
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack_damage(opponent):
        return random.randint(self.min_damage, self.max_damage)
        
class Encounter:
    def __init__(self, opponent):
        self.opponent = opponent

decks = {
    "Pyromancer": {
        "spells": [
            {"name": "Firecat", "min_damage": 80, "max_damage": 120},
            {"name": "Flame Elf", "min_damage": 150, "max_damage": 150},
            {"name": "Sunbird", "min_damage": 295, "max_damage": 355},
            {"name": "Fire Dragon", "min_damage": 395, "max_damage": 460},
            {"name": "Phoenix", "min_damage": 515, "max_damage": 595},
            {"name": "Helephant", "min_damage": 625, "max_damage": 705},
            {"name": "Sun Serpent", "min_damage": 850, "max_damage": 950}, 
        ],
        "healing_cards": {
            "Fairy": 250,
            "Fairy": 250,
            "Satyr": 500
        }
    },
    "Thaumaturge": {
        "spells": [
            {"name": "Frost Beetle", "min_damage": 65, "max_damage": 105},
            {"name": "Snow Serpent", "min_damage": 155, "max_damage": 195},
            {"name": "Blizzard", "min_damage": 210, "max_damage": 210},
            {"name": "Evil Snowman", "min_damage": 240, "max_damage": 300},
            {"name": "Ice Wyvern", "min_damage": 335, "max_damage": 395},
            {"name": "Snow Angel", "min_damage": 410, "max_damage": 480},
            {"name": "Colossus", "min-damage": 500, "max_damage": 580},
        ],
        "healing_cards": {
            "Fairy": 250,
            "Fairy": 250,
            "Satyr": 500
        }
    },
    "Diviner": {
        "spells": [
            {"name": "Thunder Snake", "min_damage": 105, "max_damage": 145},
            {"name": "Lightning Bats", "min_damage": 245, "max_damage": 285},
            {"name": "Storm Shark", "min_damage": 375, "max_damage": 435},
            {"name": "Kraken", "min_damage": 520, "max_damage": 580},
            {"name": "Stormzilla", "min_damage": 650, "max_damage": 730},
            {"name": "Leviathan", "min_damage": 800, "max_damage": 900},
            {"name": "Insane Bolt", "min_damage": 999, "max_damage": 999},
        ],
        "healing_cards": {
            "Fairy": 250,
            "Fairy": 250,
            "Satyr": 500
        }
    },
    "Theurgist": {
        "spells": [
            {"name": "Imp", "min_damage": 65, "max_damage": 105},
            {"name": "Leprechaun", "min_damage": 155, "max_damage": 195},
            {"name": "Seraph", "min_damage": 335, "max_damage": 395},
            {"name": "Earth Walker", "min_damage": 420, "max_damage": 500},
            {"name": "Centaur", "min_damage": 515, "max_damage": 595},
        ],
        "healing_cards":{
            "Fairy": 250,
            "Fairy": 250,
            "Satyr": 500,
            "Satyr": 500,
            "Angel's Breath": 1000
        }
    },
    "Conjurer": {
        "spells": [
            {"name": "Blood Bat", "min_damage": 70, "max_damage": 105},
            {"name": "Troll", "min_damage": 170, "max_damage": 210},
            {"name": "Cyclops", "min_damage": 265, "max_damage": 325},
            {"name": "Humongfrog", "min_damage": 300, "max_damage": 355},
            {"name": "Minotaur", "min_damage": 445, "max_damage": 510},
            {"name": "Medusa", "min_damage": 600, "max_damage": 685},
            {"name": "Baba Yaga", "min_damage": 750, "max_damage": 800},
        ],
        "healing_cards":{
            "Fairy": 250,
            "Fairy": 250,
            "Satyr": 500
        }
    },
    "Necromancer": {
        "spells": [
            {"name": "Dark Sprite", "min_damage": 65, "max_damage": 105},
            {"name": "Ghoul", "min_damage": 160, "max_damage": 160},
            {"name": "Banshee", "min_damage": 245, "max_damage": 305},
            {"name": "Vampire", "min_damage": 350, "max_damage": 350},
            {"name": "Wraith", "min_damage": 510, "max_damage": 510},
            {"name": "Scarecrow", "min_damage": 600, "max_damage": 645},
            {"name": "Reaper", "min_damage": 700, "max_damage": 750},
        ],
        "healing_cards":{
            "Fairy": 250,
            "fairy": 250,
            "Satyr": 500
        }
    },
}

starting_stats = {
    "Pyromancer": {
        "health_points": 1250,
        "mana": 50,
        "accuracy": 0.75,
        "min_damage": 1,
        "max_damage": 950,
        "description": "Most Beginner friendly, Specializing in fire spells with Balanced offense and modest health. Accuracy is 75%"
    },
    "Thaumaturge": {
        "health_points": 1750,
        "mana": 55,
        "accuracy": 0.85,
        "min_damage": 1,
        "max_damage": 580,
        "description": "Specializes in ice-based spells, Highest health but weak offensively. Accuracy is 85%"
    },
    "Diviner": {
        "health_points": 1200,
        "mana": 55,
        "accuracy": 0.7,
        "min_damage": 1,
        "max_damage": 999,
        "description": "Specializes in powerful storm attacks, Most powerful damage class but lowest health and hardest to control. Accuracy is 70%"
    },
    "Theurgist": {
        "health_points": 1650,
        "mana": 60,
        "accuracy": 0.9,
        "min_damage": 1,
        "max_damage": 595,
        "description": "Utilizes Life magic to specialize in healing and support spells, Most stable magic. Accuracy is 90%"
    },
    "Conjurer": {
        "health_points": 1350,
        "mana": 50,
        "accuracy": 0.8,
        "min_damage": 1,
        "max_damage": 800,
        "description": "Spirit magic users with balanced accuracy and mana usage to control the battlefield. Accuracy is 80%"
    },
    "Necromancer": {
        "health_points": 1400,
        "mana": 60,
        "accuracy": 0.85,
        "min_damage": 1,
        "max_damage": 999,
        "description": "Specializes in draining spells that sap the life. Deals direct damage but returns half the damage as health. Accuracy is 85%"
    },
}

spell_effects = {
    "Firecat": (80, 120),
    "Flam Elf": (100, 100),
    "Sunbird": (295, 355),
    "Fire Dragon": (395, 460),
    "Phoenix": (515, 595),
    "Helephant": (625, 705),
    "Sun Serpent": (850, 950),
    "Frost Beetle": (65, 105),
    "Snow Serpent": (155, 195),
    "Blizzard": (210, 210),
    "Evil Snowman": (240, 300),
    "Ice Wyvern": (335, 395),
    "Snow Angel": (410, 480),
    "Colossus": (500, 580),
    "Thunder Snake": (105, 145),
    "Lightning Bats": (245, 285),
    "Storm Shark": (375, 435),
    "Kraken": (520, 580),
    "Stormzilla": (650, 730),
    "Leviathan": (800, 900),
    "Insane Bolt": (999, 999),
    "Imp": (65, 105),
    "Leprechaun": (155, 195),
    "Seraph": (335, 395),
    "Earth Walker": (420, 500),
    "Centaur": (515, 595),
    "Blood Bat": (70, 110),
    "Troll": (170, 210),
    "Cyclops": (265, 325),
    "Humongfrog": (300, 355),
    "Minotaur": (445, 510),
    "Medusa": (600, 685),
    "Baba Yaga": (750, 800),
    "Dark Sprite": (65, 105),
    "Ghoul": (160, 160),
    "Banshee": (245, 305),
    "Vampire": (350, 350),
    "Wraith": (510, 510),
    "Scarecrow": (600, 645),
    "Reaper": (700, 750),
}

spells = {
    "Firecat": (80, 120),
    "Flame Elf": (100, 100),
    "Sunbird": (295, 355),
    "Fire Dragon": (395, 460),
    "Phoenix": (515, 595),
    "Helephant": (625, 705),
    "Sun Serpent": (850, 950),
    "Frost Beetle": (65, 105),
    "Snow Serpent": (155, 195),
    "Blizzard": (210, 210),
    "Evil Snowman": (240, 300),
    "Ice Wyvern": (335, 395),
    "Snow Angel": (410, 480),
    "Colossus": (500, 580),
    "Thunder Snake": (105, 145),
    "Lightning Bats": (245, 285),
    "Storm Shark": (375, 435),
    "Kraken": (520, 580),
    "Stormzilla": (650, 730),
    "Leviathan": (800, 900),
    "Insane Bolt": (999, 999),
    "Imp": (65, 105),
    "Leprechaun": (155, 195),
    "Seraph": (335, 395),
    "Earth Walker": (420, 500),
    "Centaur": (515, 595),
    "Blood Bat": (70, 110),
    "Troll": (170, 210),
    "Cyclops": (265, 325),
    "Humongfrog": (300, 355),
    "Minotaur": (445, 510),
    "Medusa": (600, 685),
    "Baba Yaga": (750, 800),
    "Dark Sprite": (65, 105),
    "Ghoul": (160, 160),
    "Banshee": (245, 305),
    "Vampire": (350, 350),
    "Wraith": (510, 510),
    "Scarecrow": (600, 645),
    "Reaper": (700, 750),
}
    
spell_mana = {
    "Firecat": 1,
    "Flam Elf": 2,
    "Sunbird": 3,
    "Fire Dragon": 5,
    "Phoenix": 6,
    "Helephant": 8,
    "Sun Serpent": 10,
    "Frost Beetle": 1,
    "Snow Serpent": 2,
    "Blizzard": 3,
    "Evil Snowman": 5,
    "Ice Wyvern": 6,
    "Snow Angel": 8,
    "Colossus": 10,
    "Thunder Snake": 1,
    "Lightning Bats": 2,
    "Storm Shark": 3,
    "Kraken": 5,
    "Stormzilla": 6,
    "Leviathan": 8,
    "Insane Bolt": 10,
    "Imp": 1,
    "Leprechaun": 2,
    "Seraph": 3,
    "Earth Walker": 6,
    "Centaur": 8,
    "Blood Bat": 1,
    "Troll": 2,
    "Cyclops": 3,
    "Humongfrog": 5,
    "Minotaur": 6,
    "Medusa": 8,
    "Baba Yaga": 10,
    "Dark Sprite": 1,
    "Ghoul": 2,
    "Banshee": 3,
    "Vampire": 5,
    "Wraith": 6,
    "Scarecrow": 8,
    "Reaper": 10,
}

spell_accuracy = {
    "Firecat": 0.75,
    "Flam Elf": 0.75,
    "Sunbird": 0.75,
    "Fire Dragon": 0.75,
    "Phoenix": 0.75,
    "Helephant": 0.75,
    "Sun serpent": 0.75,
    "Frost Beetle": 0.85,
    "Snow Serpent": 0.85,
    "Blizzard": 0.85,
    "Evil Snowman": 0.85,
    "Ice Wyvern": 0.85,
    "Snow Angel": 0.85,
    "Colossus": 0.85,
    "Thunder Snake": 0.7,
    "Lightning Bats": 0.7,
    "Storm Shark": 0.7,
    "Kraken": 0.7,
    "Stormzilla": 0.7,
    "Leviathan": 0.7,
    "Insane Bolt": 0.7,
    "Imp": 0.9,
    "Leprechaun": 0.9,
    "Seraph": 0.9,
    "Earth Walker": 0.9,
    "Centaur": 0.9,
    "Blood Bat": 0.8,
    "Troll": 0.8,
    "Cyclops": 0.8,
    "Humongfrog": 0.8,
    "Minotaur": 0.8,
    "Medusa": 0.8,
    "Baba Yaga": 0.8,
    "Dark Sprite": 0.85,
    "Ghoul": 0.85,
    "Banshee": 0.85,
    "Vampire": 0.85,
    "Wraith": 0.85,
    "Scarecrow": 0.85,
    "Reaper": 0.85,
}

healing_cards = {
        "Fairy": 250,
        "Satyr": 500,
        "Angels Breath": 1000,
}

healing_card_mana = {
        "Fairy": 2,
        "Satyr": 4,
        "Angels Breath": 6,
}     

def select_class():
    print("\nSelect a class:\n")
    for class_name, stats in starting_stats.items():
        type_text(f"{class_name}: {stats['description']}\n")

    while True:
        chosen_class = input("Enter the name of the class you want to play as: ").strip()
        if chosen_class in starting_stats:
            return chosen_class
        else:
            print("Invalid class name. Please try again.")

def start_game():
    player_class = select_class()
    if player_class:
        player = Mage(
            "Wizard",
            player_class,
            starting_stats[player_class]["health_points"],
            starting_stats[player_class]["mana"],
            starting_stats[player_class]["accuracy"],
            decks
        )
        return player
    else:
        return None


def load_game():
    try:
        with open("game_save.pickle", "rb") as file:
            game_data = pickle.load(file)
            return game_data["player"], game_data["player_position"], game_data["enemy_positions"]
    except FileNotFoundError:
        print("No saved game found.")
        return None, None, None


def save_game(player, player_position, enemy_positions):
    game_data = {
        "player": player,
        "player_position": player_position,
        "enemy_positions": enemy_positions
    }
    with open("game_save.pickle", "wb") as file:
        pickle.dump(game_data, file)

def end_credits():
    type_text("\nEnd Credits\n")
    type_text("Created by: Jack Watson\n")
    type_text("Thank you for playing Shadows Rising!\nYou have saved the kingdom and the world is forever in your debt.\n")
    type_text("Now go adventurer to adventure more adventures!")

def apply_status_effects(mage):
    new_status_effects = []
    for status_effect in mage.status_effects:
        status_effect["duration"] -= 1
        mage.health_points -= status_effect["damage"]
        print(f"{mage.name} took {status_effect['damage']} damage from {status_effect['source']}!")
        if status_effect["duration"] > 0:
            new_status_effects.append(status_effect)
    mage.status_effects = new_status_effects

def encounter(player, enemy):
    def enemy_turn():
        if enemy.health_points <= 0:
            print(f"{enemy.name} has been defeated!")
            if enemy.name == "Malistaire the Undying":
                end_credits()
            return False

        damage = enemy.attack_damage()
        player.health_points -= damage
        print(f"{enemy.name} attacks you for {damage} damage! You now have {player.health_points} HP left.")
        if player.health_points <= 0:
            print("You have been defeated!")
            return False

        return True

    healing_spells = ["ghoul", "vampire", "wraith"]

    print(f"A {enemy.name} has appeared!")
    while enemy.health_points > 0 and player.health_points > 0:
        print(f"Your health: {player.health_points}, Your mana: {player.mana}")
        print(f"The {enemy.name}'s health: {enemy.health_points}")

        print("Available spells:")
        for spell_name in player.spells:
            min_damage, max_damage = player.spells[spell_name]
            mana_cost = spell_mana[spell_name]
            print(f"- {spell_name}: {min_damage}-{max_damage} damage, {mana_cost} mana")

        print("Available healing cards:")
        for healing_card in player.healing_cards:
            healing_amount = player.healing_cards[healing_card]
            print(f"- {healing_card}: {healing_amount} HP")

        player_move = input("Enter a spell name to cast or a healing card to use: ")

        if player_move in player.spells:
            if player.mana >= spell_mana[player_move]:
                if random.random() < spell_accuracy[player_move]:
                    min_damage, max_damage = player.spells[player_move]
                    damage = random.randint(min_damage, max_damage)
                    enemy.health_points -= damage
                    player.mana -= spell_mana[player_move]
                    print(f"Your {player_move} deals {damage} damage to the {enemy.name}.")

                    if player_move.lower() in healing_spells:
                        healing_amount = damage // 2
                        player.health_points += healing_amount
                        if player.health_points > player.max_health_points:
                            player.health_points = player.max_health_points
                        print(f"Your {player_move} heals you for {healing_amount} HP.")
                else:
                    print(f"Your {player_move} misses the {enemy.name}.")
            else:
                print("You don't have enough mana to cast this spell. Try again.")
        elif player_move in player.healing_cards:
            healing_amount = player.healing_cards[player_move]
            player.health_points += healing_amount
            if player.health_points > player.max_health_points:
                player.health_points = player.max_health_points
            print(f"Your {player_move} heals you for {healing_amount} HP.")
        else:
            print("Invalid move. Try again.")
            continue

        if not enemy_turn():
            break

    if player.health_points > 0:
        player.level_up()
        return True
    else:
        return False

def type_text(text, delay=0.04):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(delay)
    print() 
    
def display_map(player_position, enemy_positions):
    for i in range(8):
        for j in range(8):
            if (i, j) == player_position:
                print("P", end=" ")
            elif (i, j) in enemy_positions:
                print("E", end=" ")
            else:
                print(".", end=" ")
        print()

def move(player_pos, direction):
    x, y = player_pos

    if direction.lower() == "up" and x > 0:
        x -= 1
    elif direction.lower() == "down" and x < 7:
        x += 1
    elif direction.lower() == "left" and y > 0:
        y -= 1
    elif direction.lower() == "right" and y < 7:
        y += 1
    else:
        print("Invalid direction or movement not allowed.")

    return x, y

def check_for_encounter(player_position, enemy_positions):
    for enemy in enemy_positions:
        if player_position == enemy["position"]:
            return enemy
    return None

def main():
    def play_again_query():
        while True:
            response = input("Do you want to play again? (yes/no): ").lower()
            if response in ["yes", "no"]:
                if response == "no":
                    print("Exiting the game. Come back any time!")
                    return False
                elif response == "yes":
                    return True
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    display_title()

    play_again = True
    while play_again:
        game_in_progress = False
        display_main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            game_in_progress = True
            type_text("\nWelcome to Shadows Rising\n")
            type_text("In a land far, far, away. Their lives a prospering kingdom known as Etheria.\n")
            type_text("It was a truly beautiful kingdom filled with busy streets and happy civilians as far as the eye could see.\n")
            type_text("Everything seemed perfect and like nothing could ever go wrong, but just as life shows us, nothing last forever...\n")
            type_text("What seemed like a nice normal day with birds singing and blue skies turned into darkness in a flash!\n")
            type_text("At the center of this darkness was a figure clad in dark robes and a menacing staff that made everyone quiver in fear.\n")
            type_text("This wizard was Malistaire the Undying! A dark scourge that ravaged the kingdom 200 years ago and has risen again to seek his revenge and take over the throne.\n")
            type_text("Will a hero rise up to bring this monster down, or will the land be ruled by shadow for an eternity.\n")
            type_text("This is for you to decide!")

            player_class = select_class()
            if player_class:
                player = Mage(
                    "Wizard",
                    starting_stats[player_class]["min_damage"],
                    starting_stats[player_class]["max_damage"],
                    player_class,
                    starting_stats[player_class]["health_points"],
                    starting_stats[player_class]["mana"],
                    starting_stats[player_class]["accuracy"],
                    decks
                )

                player_position = (0, 0)
                enemies_data = [
                    {"name": "Triton", "deck": "Diviner", "health_points": 300, "mana": 40, "accuracy": 0.7},
                    {"name": "Fire Giant", "deck": "Pyromancer", "health_points": 600, "mana": 40, "accuracy": 0.75},
                    {"name": "Elden Beast", "deck": "Conjurer", "health_points": 1000, "mana": 40, "accuracy": 0.85},
                    {"name": "Frost Queen", "deck": "Thaumaturge", "health_points": 1250, "mana": 40, "accuracy": 0.85},
                    {"name": "Malistaire the Undying", "deck": "Necromancer", "health_points": 2750, "mana": 40, "accuracy": 1.0},
                ]

                enemy_positions = [
                    {"position": (random.randint(0, 7), random.randint(0, 7)), "data": enemy}
                    for enemy in enemies_data[:-1]
                ]

                enemy_positions.append({"position": (7, 7), "data": enemies_data[-1]})
        elif choice == "2":
            player, player_position, enemy_positions = load_game()
            if player and player_position and enemy_positions:
                game_in_progress = True
        elif choice == "3":
            end_credits()
        elif choice == "4":
            play_again = play_again_query()
        else:
            print("Invalid input. Please try again.")

        while game_in_progress:
            display_map(player_position, [enemy["position"] for enemy in enemy_positions])
            move_input = input("Enter move direction (up, down, left, right), 'save' to save the game, or 'quit' to return to the main menu: ").lower()
            if move_input in ["up", "down", "left", "right"]:
                player_position = move(player_position, move_input)
                encountered_enemy_data = check_for_encounter(player_position, enemy_positions)
                if encountered_enemy_data:
                    enemy_data = encountered_enemy_data["data"]
                    enemy = Mage(
                        enemy_data["name"],
                        starting_stats[enemy_data["deck"]]["min_damage"],
                        starting_stats[enemy_data["deck"]]["max_damage"],
                        enemy_data["deck"],
                        enemy_data["health_points"],
                        enemy_data["mana"],
                        enemy_data["accuracy"],
                        decks
                    )
                    won_encounter = encounter(player, enemy)
                    if won_encounter:
                        enemy_positions.remove(encountered_enemy_data)
                        if encountered_enemy_data["data"]["name"] == "Malistaire the Undying":
                            game_in_progress = False
                            play_again = play_again_query()
            elif move_input == "save":
                save_game(player, player_position, enemy_positions)
                print("Game saved!")
            elif move_input == "quit":
                game_in_progress = False
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
