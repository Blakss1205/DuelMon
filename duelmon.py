import random

# ---------------------------------------
# Instruction
# ---------------------------------------
def show_instructions():
    print("===================================")
    print("        WELCOME TO DUELMON!        ")
    print("===================================")
    print("HOW TO PLAY:")
    print("- Choose your starter Monster.")
    print("- Each Monster has unique stats and moves.")
    print("- Take turns attacking until one faints.")
    print("- Win by reducing your opponent’s HP to 0.")
    print("- Type only the valid numbers shown on screen.")
    print("===================================\n")

# ---------------------------------------
# Monster Select
# ---------------------------------------    
def choose_monster():
    print("Choose your Manstah:")
    print("[1] Charmander (Fire)")
    print("[2] Squirtle (Water)")
    print("[3] Bulbasaur (Grass)")

    while True:
        choice = input("Enter number (1-3):")
        
        if choice == "1":
            p_name = "Charmander"
            p_type = "Fire"
            p_hp = 39
            p_attack = 52
            p_defense = 43
            p_speed = 65
            p_m1_name = "Scratch"
            p_m1_type = "Normal"
            p_m1_power = 40
            p_m1_pp = 35
            p_m2_name = "Ember"
            p_m2_type = "Fire"
            p_m2_power = 40
            p_m2_pp = 25
            break

        elif choice == "2":
            p_name = "Squirtle"
            p_type = "Water"
            p_hp = 44
            p_attack = 48
            p_defense = 65
            p_speed = 43
            p_m1_name = "Tackle"
            p_m1_type = "Normal"
            p_m1_power = 40
            p_m1_pp = 35
            p_m2_name = "Water Gun"
            p_m2_type = "Water"
            p_m2_power = 40
            p_m2_pp = 25
            break

        elif choice == "3":
            p_name = "Bulbasaur"
            p_type = "Grass"
            p_hp = 45
            p_attack = 49
            p_defense = 49
            p_speed = 45
            p_m1_name = "Tackle"
            p_m1_type = "Normal"
            p_m1_power = 40
            p_m1_pp = 35
            p_m2_name = "Vine Whip"
            p_m2_type = "Grass"
            p_m2_power = 45
            p_m2_pp = 25
            break

        else:
            print("Invalid choice! Please type 1, 2, or 3.\n")
    
    player = [p_name, p_type, p_hp, p_attack, p_defense, p_speed, p_m1_name, p_m1_type, p_m1_power, p_m1_pp, p_m2_name, p_m2_type, p_m2_power, p_m2_pp]
    return player

# ---------------------------------------
# CPU Random Monster Select
# ---------------------------------------
def cpu_choose():
    cpu_list = ["Charmander", "Squirtle", "Bulbasaur"]
    choice = random.choice(cpu_list)

    if choice == "Charmander":
        return ["Charmander", "Fire", 39, 52, 43, 65, "Scratch", "Normal", 40, 35, "Ember", "Fire", 40, 25]
    elif choice == "Squirtle":
        return ["Squirtle", "Water", 44, 48, 65, 43, "Tackle", "Normal", 40, 35, "Water Gun", "Water", 40, 25]
    else:
        return ["Bulbasaur", "Grass", 45, 49, 49, 45, "Tackle", "Normal", 40, 35, "Vine Whip", "Grass", 45, 25]

# ---------------------------------------
# Type Effectiveness
# ---------------------------------------
def type_effect(move_type, target_type):
    if move_type == "Fire" and target_type == "Grass":
        return 2
    elif move_type == "Water" and target_type == "Fire":
        return 2
    elif move_type == "Grass" and target_type == "Water":
        return 2
    elif move_type == "Fire" and target_type == "Water":
        return 0.5
    elif move_type == "Water" and target_type == "Grass":
        return 0.5
    elif move_type == "Grass" and target_type == "Fire":
        return 0.5
    else:
        return 1

# ---------------------------------------
# Damage Calculation
# ---------------------------------------
def calculate_damage(attack, defense, power, multiplier):
    base = ((attack / defense) * power) / 5 + 2
    total = int(base * multiplier)
    if total < 1:
        total = 1
    return total

# ---------------------------------------
# Battle
# ---------------------------------------
def battle(player, cpu):
    print("\nYou chose " + player[0] + "!")
    print("CPU chose " + cpu[0] + "!\n")
    
    # Unpack player
    p_name, p_type, p_hp, p_attack, p_defense, p_speed, \
    p_m1_name, p_m1_type, p_m1_power, p_m1_pp, \
    p_m2_name, p_m2_type, p_m2_power, p_m2_pp = player

    # Unpack CPU
    c_name, c_type, c_hp, c_attack, c_defense, c_speed, \
    c_m1_name, c_m1_type, c_m1_power, c_m1_pp, \
    c_m2_name, c_m2_type, c_m2_power, c_m2_pp = cpu

    while p_hp > 0 and c_hp > 0:
        print(f"{p_name} (You) HP: {p_hp} | {c_name} (CPU) HP: {c_hp}")
        print("[1]", p_m1_name, "-", p_m1_type, "Power:", p_m1_power, "PP:", p_m1_pp)
        print("[2]", p_m2_name, "-", p_m2_type, "Power:", p_m2_power, "PP:", p_m2_pp)

        move_choice = input("Choose move (1 or 2): ").strip()

        # -------------------------------
        # Player turn
        # -------------------------------
        if move_choice == "1":
            print("--------------- PLAYER TURN ----------------")
            if p_m1_pp <= 0:
                print("No PP left for that move!\n")
                continue
            p_m1_pp -= 1
            multiplier = type_effect(p_m1_type, c_type)
            dmg = calculate_damage(p_attack, c_defense, p_m1_power, multiplier)
            c_hp -= dmg
            print(f"\n{p_name} (You) used {p_m1_name} and dealt {dmg} damage!\n")
            if multiplier > 1:
                print("It's super effective!\n")
            elif multiplier < 1:
                print("It's not very effective...\n")

        elif move_choice == "2":
            print("--------------- PLAYER TURN ----------------")
            if p_m2_pp <= 0:
                print("No PP left for that move!\n")
                continue
            p_m2_pp -= 1
            multiplier = type_effect(p_m2_type, c_type)
            dmg = calculate_damage(p_attack, c_defense, p_m2_power, multiplier)
            c_hp -= dmg
            print(f"\n{p_name} (You) used {p_m2_name} and dealt {dmg} damage!\n")
            if multiplier > 1:
                print("It's super effective!\n")
            elif multiplier < 1:
                print("It's not very effective...\n")

        else:
            print("Invalid choice!\n")
            continue

        if c_hp <= 0:
            print(f"{c_name} fainted! You win!\n")
            break

        # -------------------------------
        # CPU turn
        # -------------------------------
        print("----------------- CPU TURN -----------------")
        cpu_moves = []
        if c_m1_pp > 0:
            cpu_moves.append("1")
        if c_m2_pp > 0:
            cpu_moves.append("2")
        if not cpu_moves:  # CPU has no moves
            print(f"{c_name} has no moves left! You win!\n")
            break

        cpu_move = random.choice(cpu_moves)

        if cpu_move == "1":
            c_m1_pp -= 1
            multiplier = type_effect(c_m1_type, p_type)
            dmg = calculate_damage(c_attack, p_defense, c_m1_power, multiplier)
            p_hp -= dmg
            print(f"{c_name} (CPU) used {c_m1_name} and dealt {dmg} damage!\n")
            if multiplier > 1:
                print("It's super effective!\n")
            elif multiplier < 1:
                print("It's not very effective...\n")

        elif cpu_move == "2":
            c_m2_pp -= 1
            multiplier = type_effect(c_m2_type, p_type)
            dmg = calculate_damage(c_attack, p_defense, c_m2_power, multiplier)
            p_hp -= dmg
            print(f"{c_name} (CPU) used {c_m2_name} and dealt {dmg} damage!\n")
            if multiplier > 1:
                print("It's super effective!\n")
            elif multiplier < 1:
                print("It's not very effective...\n")

        if p_hp <= 0:
            print(f"{p_name} fainted! You lost!\n")
            break

# ---------------------------------------
# Main Game Loop
# ---------------------------------------
def main():
    show_instructions()

    while True:
        player = choose_monster()
        cpu = cpu_choose()
        battle(player, cpu)

        while True:
            again = input("Play Again? (yes/no): ").strip().lower()
            if again == "yes":
                print("\n============================================")
                print("            Starting a new game!            ")
                print("============================================\n")
                break
            elif again == "no":
                print("\n============================================")
                print("           Thank You For Playing!")
                print("============================================\n")
                return
            else:
                print("Invalid input! Please type 'yes' or 'no' only.\n")

# ---------------------------------------
# Run the game
# ---------------------------------------
main()
