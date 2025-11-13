import random
import time
import os

# clear whole screen after playing again to look more clean
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# ----------- #
# Instruction #
# ----------- #
def show_instructions():
    print("__        _______ _     ____ ___  __  __ _____    _____ ___  ")
    print("\ \      / / ____| |   / ___/ _ \|  \/  | ____|  |_   _/ _ \ ")
    print(" \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|      | || | | |")
    print("  \ V  V / | |___| |__| |__| |_| | |  | | |___     | || |_| |")
    print("   \_/\_/  |_____|_____\____\___/|_|  |_|_____|    |_| \___/ ")
    print("          ____  _   _ _____ _     __  __  ___  _   _ ")
    print("         |  _ \| | | | ____| |   |  \/  |/ _ \| \ | |")
    print("         | | | | | | |  _| | |   | |\/| | | | |  \| |")
    print("         | |_| | |_| | |___| |___| |  | | |_| | |\  |")
    print("         |____/ \___/|_____|_____|_|  |_|\___/|_| \_|\n")  
    time.sleep(1)
    print("HOW TO PLAY:")
    print("- Choose your starter Monster.")
    print("- Each Monster has unique stats and moves.")
    print("- Take turns attacking until one faints.")
    print("- Win by reducing your opponent’s HP to 0.")
    print("- Type only the valid numbers shown on screen.\n")

# -------------- #
# Monster Select #
# -------------- #   
def choose_monster():
    print("Choose your Monster:")
    time.sleep(1)
    print("[1] Gapido (Firebender)")
    print("[2] Evasco (Waterbender)")
    print("[3] Illumin (Earthbender)")
    print("[4] Gicalao (Airbender)\n")

    # monsters: name, type, HP, ATK, DEF, SPD, move1, type, power, PP, move2, type, power, PP
    data = {
        "1": ["Gapido", "Firebender", 53, 42, 39, 36,
              "Punch", "Normal", 40, 35,
              "Blazing rings and arcs", "Firebender", 45, 5],

        "2": ["Evasco", "Waterbender", 55, 40, 42, 33,
              "Kick", "Normal", 40, 35,
              "Maelstrom", "Waterbender", 45, 5],

        "3": ["Illumin", "Earthbender", 56, 39, 43, 35,
              "Headbutt", "Normal", 40, 35,
              "Earthquake", "Earthbender", 45, 5],

        "4": ["Gicalao", "Airbender", 51, 43, 39, 37,
              "Kick", "Normal", 40, 35,
              "Shockwave", "Airbender", 45, 5],
    }

    while True:
        choice = input("Enter number (1-4): ")
        if choice in data:
            (
                p_name, p_type, p_hp, p_attack, p_defense, p_speed,
                p_m1_name, p_m1_type, p_m1_power, p_m1_pp,
                p_m2_name, p_m2_type, p_m2_power, p_m2_pp
            ) = data[choice]
            break
        else:
            print("\nInvalid choice! Please type 1, 2, 3 or 4.\n")
    
    player = [
        p_name, p_type, p_hp, p_attack, p_defense, p_speed,
        p_m1_name, p_m1_type, p_m1_power, p_m1_pp,
        p_m2_name, p_m2_type, p_m2_power, p_m2_pp
    ]

    return player

# ---------------------------------------
# CPU Random Monster Select
# ---------------------------------------

# CPU randomly select monster using random.choice()
def cpu_choose():
    cpu_list = ["Gapido", "Evasco", "Illumin", "Gicalao"]
    choice = random.choice(cpu_list)

    if choice == "Gapido":
        return ["Gapido", "Firebender", 53, 42, 39, 36,
                "Punch", "Normal", 40, 35,
                "Blazing rings and arcs", "Firebender", 45, 5]
    elif choice == "Evasco":
        return ["Evasco", "Waterbender", 55, 40, 42, 33,
                "Kick", "Normal", 40, 35,
                "Maelstrom", "Waterbender", 45, 5]
    elif choice == "Illumin":
        return ["Illumin", "Earthbender", 56, 39, 43, 35,
                "Headbutt", "Normal", 40, 35,
                "Earthquake", "Earthbender", 45, 5]
    else:
        return ["Gicalao", "Airbender", 51, 43, 39, 37,
                "Kick", "Normal", 40, 35,
                "Shockwave", "Airbender", 45, 5]

# ---------------------------------------
# Type Effectiveness
# ---------------------------------------

    # damage multiplier
def type_effect(move_type, target_type):
    if move_type == "Firebender" and target_type == "Airbender":
        return 2
    elif move_type == "Waterbender" and target_type == "Firebender":
        return 2
    elif move_type == "Earthbender" and target_type == "Waterbender":
        return 2
    elif move_type == "Airbender" and target_type == "Earthbender":
        return 2
    elif move_type == "Firebender" and target_type == "Waterbender":
        return 0.5
    elif move_type == "Waterbender" and target_type == "Earthbender":
        return 0.5
    elif move_type == "Earthbender" and target_type == "Airbender":
        return 0.5
    elif move_type == "Airbender" and target_type == "Firebender":
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
# Dodge Mechanic
# ---------------------------------------

def dodgechance(speed):
    decider = random.randint(1, 100)  # Random number between 1 and 100
    if decider <= speed:
        return True
    else:
        return False


# ---------------------------------------
# Battle
# ---------------------------------------

def battle(player, cpu):
    print(f"\nYou chose {player[0]} ({player[1]})!")
    time.sleep(0.5)
    print(f"CPU chose {cpu[0]} ({cpu[1]})!\n")
    time.sleep(0.5)

    # Player Stats to Variable
    p_name, p_type, p_hp, p_attack, p_defense, p_speed, p_m1_name, p_m1_type, p_m1_power, p_m1_pp, p_m2_name, p_m2_type, p_m2_power, p_m2_pp = player

    # CPU Stats to Variable
    c_name, c_type, c_hp, c_attack, c_defense, c_speed, c_m1_name, c_m1_type, c_m1_power, c_m1_pp, c_m2_name, c_m2_type, c_m2_power, c_m2_pp = cpu

    # Determine who goes first based on speed
    turn_order = "player" if p_speed >= c_speed else "cpu"
    if p_speed == c_speed:
        turn_order = random.choice(["player", "cpu"])  # Randomize if speeds are equal

    while p_hp > 0 and c_hp > 0:
        print(f"{p_name} (You) HP: {p_hp} | {c_name} (CPU) HP: {c_hp}\n")

        if turn_order == "player":
            time.sleep(0.5)
            print("---------------- PLAYER TURN -----------------\n")
            # Show move info with current PP
            print(f"[1] {p_m1_name} - {p_m1_type} Power: {p_m1_power} PP: {p_m1_pp}")
            print(f"[2] {p_m2_name} - {p_m2_type} Power: {p_m2_power} PP: {p_m2_pp}\n")

            # Input validation loop
            while True:
                move_choice = input("Choose move (1 or 2): ").strip()
                if move_choice not in ["1", "2"]:
                    print("\nInvalid choice! Please enter 1 or 2.\n")
                    continue
                if move_choice == "1" and p_m1_pp <= 0:
                    print(f"\nNo PP left for {p_m1_name}! Choose another move.\n")
                    continue
                if move_choice == "2" and p_m2_pp <= 0:
                    print(f"\nNo PP left for {p_m2_name}! Choose another move.\n")
                    continue
                break

            # Apply move
            if move_choice == "1":
                p_m1_pp -= 1
                multiplier = type_effect(p_m1_type, c_type)
                dmg = calculate_damage(p_attack, c_defense, p_m1_power, multiplier)
                if dodgechance(c_speed):
                    print(f"\n{c_name} (CPU) dodged the attack!\n")
                    dmg = 0
                else:
                    c_hp -= dmg
                    print(f"\n{p_name} (You) used {p_m1_name} and dealt {dmg} damage!\n")
                    if multiplier > 1:
                        time.sleep(0.5)
                        print("It's super effective!\n")
                        time.sleep(0.5)
                    elif multiplier < 1:
                        time.sleep(0.5)
                        print("It's not very effective...\n")

            else:  # move_choice == "2"
                p_m2_pp -= 1
                multiplier = type_effect(p_m2_type, c_type)
                dmg = calculate_damage(p_attack, c_defense, p_m2_power, multiplier)
                if dodgechance(c_speed):
                    print(f"\n{c_name} (CPU) dodged the attack!\n")
                    dmg = 0
                else:
                    c_hp -= dmg
                    print(f"\n{p_name} (You) used {p_m2_name} and dealt {dmg} damage!\n")
                    if multiplier > 1:
                        time.sleep(0.5)
                        print("It's super effective!\n")
                        time.sleep(0.5)
                    elif multiplier < 1:
                        time.sleep(0.5)
                        print("It's not very effective...\n")

            if c_hp <= 0:
                print("==============================================")
                print(f"      {c_name} (CPU) fainted! You win!       ")
                print("==============================================\n")
                time.sleep(1)
                break

            turn_order = "cpu"

        else:  # CPU turn
            time.sleep(1)
            print("------------------ CPU TURN ------------------\n")
            if c_m1_pp > 0 and c_m2_pp > 0:
                #effectiveness comparison
                eff1 = type_effect(c_m1_type, p_type)
                eff2 = type_effect(c_m2_type, p_type)
                
                if eff1 > eff2:
                    cpu_move = "1"
                elif eff1 < eff2:
                    cpu_move = "2"
                else:
                    cpu_move = random.choice(["1", "2"])
            else:
                # If one move has no PP, use the other
                if c_m1_pp > 0:
                    cpu_move = "1"
                elif c_m2_pp > 0:
                    cpu_move = "2"
                else:
                    print(f"{c_name} has no moves left! You win!\n")
                    break

            if cpu_move == "1":
                c_m1_pp -= 1
                multiplier = type_effect(c_m1_type, p_type)
                dmg = calculate_damage(c_attack, p_defense, c_m1_power, multiplier)
                if dodgechance(p_speed):
                    print(f"{p_name} (You) dodged the attack!\n")
                    dmg = 0
                else:
                    p_hp -= dmg
                    print(f"{c_name} (CPU) used {c_m1_name} and dealt {dmg} damage!\n")
                    if multiplier > 1:
                        time.sleep(0.5)
                        print("It's super effective!\n")
                        time.sleep(0.5)
                    elif multiplier < 1:
                        time.sleep(0.5)
                        print("It's not very effective...\n")

            else:  # cpu_move == "2"
                c_m2_pp -= 1
                multiplier = type_effect(c_m2_type, p_type)
                dmg = calculate_damage(c_attack, p_defense, c_m2_power, multiplier)
                if dodgechance(p_speed):
                    print(f"{p_name} (You) dodged the attack!\n")
                    dmg = 0
                else:
                    p_hp -= dmg
                    print(f"{c_name} (CPU) used {c_m2_name} and dealt {dmg} damage!\n")
                    if multiplier > 1:
                        time.sleep(0.5)
                        print("It's super effective!\n")
                        time.sleep(0.5)
                    elif multiplier < 1:
                        time.sleep(0.5)
                        print("It's not very effective...\n")

            if p_hp <= 0:
                print("==============================================")
                print(f"      {p_name} (You) fainted! You lost!      ")
                print("==============================================\n")
                time.sleep(1)
                break

            turn_order = "player"

# ---------------------------------------
# Main Game Loop
# ---------------------------------------
def main():
    clear_screen()
    show_instructions()

    while True:
        player = choose_monster()
        cpu = cpu_choose()
        battle(player, cpu)

        while True:
            again = input("Play Again? (yes/no): ").strip().lower()
            if again == "yes":
                clear_screen()
                print("\n==============================================")
                print("              Starting a new game!              ")
                print("==============================================\n")
                time.sleep(1)
                break
            elif again == "no":
                clear_screen()
                print("           ________  _____    _   ____ __ __  ______  __  __")
                print("          /_  __/ / / /   |  / | / / //_/ \ \/ / __ \/ / / /")
                print("           / / / /_/ / /| | /  |/ / ,<     \  / / / / / / / ")
                print("          / / / __  / ___ |/ /|  / /| |    / / /_/ / /_/ /  ")
                print("         /_/ /_/ /_/_/  |_/_/ |_/_/ |_|   /_/\____/\____/   ")
                print("    __________  ____      ____  __    _____  _______   __________")
                print("   / ____/ __ \/ __ \    / __ \/ /   /   \ \/ /  _/ | / / ____/ /")
                print("  / /_  / / / / /_/ /   / /_/ / /   / /| |\  // //  |/ / / __/ / ")
                print(" / __/ / /_/ / _, _/   / ____/ /___/ ___ |/ // // /|  / /_/ /_/  ")
                print("/_/    \____/_/ |_|   /_/   /_____/_/  |_/_/___/_/ |_/\____(_)   ")
                return
            else:
                print("\nInvalid input! Please type 'yes' or 'no' only.\n")

# ---------------------------------------
# Run the game
# ---------------------------------------
main()
