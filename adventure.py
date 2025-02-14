"""
Text-based adventure game where the player explores a dungeon,
battles monsters, and collects items while managing their health.
"""

import random

def display_player_status(player_health):
    """Displays the player's current health."""
    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
    """Handles the player's path choice, modifying health based on the outcome."""
    path = random.choice(["left", "right"])
    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        player_health = min(player_health + 10, 100)
    else:
        print("You fall into a pit and lose 15 health points.")
        player_health = max(player_health - 15, 0)
        if player_health == 0:
            print("You are barely alive!")
    return player_health

def player_attack(monster_health):
    """Reduces monster health when the player attacks."""
    print("You strike the monster for 15 damage!")
    return monster_health - 15

def monster_attack(player_health):
    """Reduces player health when the monster attacks."""
    if random.random() < 0.5:
        print("The monster lands a critical hit for 20 damage!")
        player_health -= 20
    else:
        print("The monster hits you for 10 damage!")
        player_health -= 10
    return max(player_health, 0)

def combat_encounter(player_health, monster_health, has_treasure):
    """Handles the combat sequence between the player and the monster."""
    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health)
        if monster_health <= 0:
            print("You defeated the monster!")
            return has_treasure
        player_health = monster_attack(player_health)
        if player_health <= 0:
            print("Game Over!")
            return False
    return False

def check_for_treasure(has_treasure):
    """Checks if the player has obtained the treasure."""
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def acquire_item(inventory, item):
    """Adds an item to the player's inventory."""
    inventory.append(item)
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """Displays the player's inventory."""
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """Handles the player's journey through the dungeon, managing health and inventory."""
    for room in dungeon_rooms:
        print(room[0])
        if room[1]:
            print(f"You acquired a {room[1]}!")
            inventory = acquire_item(inventory, room[1])
        if room[2] == "puzzle":
            print("You encounter a puzzle!")
        elif room[2] == "trap":
            print("You see a potential trap!")
        elif room[2] == "none":
            print("There doesn't seem to be a challenge in this room.")
        
        if room[2] != "none":
            action = input("Do you want to attempt the challenge? (yes/no): ").strip().lower()
            success = random.choice([True, False]) if action == "yes" else False
            if success:
                print(room[3][0])  # Success message
            else:
                print(room[3][1])  # Failure message
                player_health += room[3][2]  # Only apply health deduction on failure
            
            player_health = max(player_health, 0)
            if player_health == 0:
                print("You are barely alive!")
        display_inventory(inventory)
    print(f"Final Health: {player_health}")
    return player_health, inventory

def main():
    """Main function to start the game and handle the gameplay loop."""
    player_health = 100
    monster_health = 75
    has_treasure = random.choice([True, False])
    inventory = []
    player_health = handle_path_choice(player_health)
    treasure_obtained = combat_encounter(player_health, monster_health, has_treasure)
    check_for_treasure(treasure_obtained)
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle", 
         ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", None, "trap", 
         ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle", 
         ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]
    if player_health > 0:
        player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)

if __name__ == "__main__":
    main()
