# Your code goes import random

def display_player_status(player_health):
    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
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
    print("You strike the monster for 15 damage!")
    return monster_health - 15

def monster_attack(player_health):
    if random.random() < 0.5:
        print("The monster lands a critical hit for 20 damage!")
        player_health -= 20
    else:
        print("The monster hits you for 10 damage!")
        player_health -= 10
    return max(player_health, 0)

def combat_encounter(player_health, monster_health, has_treasure):
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
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def acquire_item(inventory, item):
    inventory.append(item)
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    for room in dungeon_rooms:
        print(room[0])
        if room[1]:
            inventory = acquire_item(inventory, room[1])
        if room[2] != "none":
            print(f"You encounter a {room[2]}!")
            action = input("Do you want to attempt the challenge? (yes/no): ").strip().lower()
            success = random.choice([True, False]) if action == "yes" else False
            print(room[3][0] if success else room[3][1])
            player_health += room[3][2] if not success else 0
            player_health = max(player_health, 0)
            if player_health == 0:
                print("You are barely alive!")
        display_inventory(inventory)
    print(f"Final Health: {player_health}")
    return player_health, inventory

def main():
    player_health = 100
    monster_health = 75
    has_treasure = random.choice([True, False])
    inventory = []
    player_health = handle_path_choice(player_health)
    treasure_obtained = combat_encounter(player_health, monster_health, has_treasure)
    check_for_treasure(treasure_obtained)
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]
    if player_health > 0:
        player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)

if __name__ == "__main__":
    main()
