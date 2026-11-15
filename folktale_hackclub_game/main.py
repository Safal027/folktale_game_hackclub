
# folktale_hackclub


# Roadmap:

# Forest -> Cave -> 2 Entrances
# 1st entrance -> Initially unlocked, games: number guessing game and a randomized math puzzle (each giving 1 magic crystal)
# 2nd entrance -> Initially locked, requires at least 2 magic crystals, has a boss fight where user has to defeat the boss in 3 games of rock paper scissors


import random
import sys

initial_inp = None

room = None
magic_crystals = 0

registered_1 = False
registered_2 = False
registered_3 = False
registered_4 = False

should_play = None

game_1_done = False
game_2_done = False

played_games_count = 0


def play_game():
    global initial_inp, room, magic_crystals, registered_1, registered_2, registered_3, registered_4, should_play, game_1_done, game_2_done, played_games_count

    while True:
        if registered_1 == False:
            print("\nYou are lost in a forest. You are trying to find your way out. \nBut you suddenly stumble upon a cave. Inside the cave you see something is glowing.")
            registered_1 = True

        if initial_inp != "y":
            initial_inp = input("\nEnter the cave? (y/n): ").lower().strip()

        if initial_inp == "n":
            print("\nYou are lost anyway.")
            continue

        elif initial_inp == "y":
            room = "cave"

        else:
            print("You have to make a decision.")
            continue

        while room == "cave":
            if registered_2 == False:
                print(
                    "\nJust after you entered the cave, the entrance is closed with heavy gates.")
                print(
                    "You see two glowing gates in front of you. \n1st one is open while the other gate is closed.")
                registered_2 = True

            entrance_input = input(
                "\nWhich gate to enter? (1/2): ").lower().strip()

            if entrance_input == "1":
                room = "1"
            elif entrance_input == "2":
                if magic_crystals >= 2:
                    room = "2"
                else:
                    print(
                        f"\nIt says: You need 2 magic crystals to enter the second gate. But you have {magic_crystals}.")
                    continue
            else:
                print("\nYou have to make a decision.")

            while room == "1":
                if registered_3 == False:
                    print("\n || Welcome, Player! ||")
                    print("\nIf you want to exit this cave, you must have to play my games and collect magic crystals which is used to open the other gate. \nAfter which you should defeat the boss inside the gate 2.")
                    registered_3 = True

                if should_play not in ["y", "n"]:
                    should_play = input(
                        "\nSo Player, are you willing to play these games? (y/n): ").lower().strip()

                if should_play == "y":
                    while True:
                        current_game = input(
                            "\nMake a decision (1 for a number guessing game / 2 for a math puzzle / 3 to exit this room): ").lower().strip()

                        if current_game not in ["1", "2", "3"]:
                            print("\nMake a valid decision.")
                            continue

                        else:
                            break

                elif should_play == "n":
                    print("\nYou exited gate 1.")
                    print(f"\nYou have [{magic_crystals}] magic crystal/s.")
                    registered_3 = False
                    room = "cave"
                    should_play = None
                    break

                else:
                    print("Make a decision!")
                    continue

                if current_game == "1":
                    print("\nYou have to guess the correct number in upto 7 tries.")

                    n = random.randint(1, 100)
                    c = 0

                    while True:
                        try:
                            choosen = int(
                                input("\nChoose a number from 1 to 100: "))
                        except ValueError:
                            print("\nGive a valid answer!")
                            continue

                        if choosen == n:
                            c += 1
                            if c < 8:
                                print(f"\nCorrect answer! In {c} tries!")
                                if game_1_done == False or played_games_count >= 2:
                                    print(
                                        "You have been awarded with a magic crystal!")
                                    magic_crystals += 1
                                    game_1_done = True
                                    played_games_count += 1
                                else:
                                    print(
                                        f"Since you have already completed this game, you obtain no extra crystal. \nTry another game.")
                            if c >= 8:
                                print(f"\nCorrect answer! In {c} tries!")
                                if game_1_done == False:
                                    print(
                                        f"Sorry, you completed this game at most 7 tries, but you had {c} tries. So you obtain no extra crystal. Try again!")
                                else:
                                    print(
                                        f"Since you have already completed this game, you obtain no extra crystal. \nTry another game.")
                            break

                        else:
                            c += 1
                            if choosen < n:
                                print("Too Low!")
                            elif choosen > n:
                                print("Too High!")

                if current_game == "2":
                    while True:
                        n1 = random.randint(1, 10)
                        n2 = random.randint(1, 10)
                        n3 = random.randint(1, 10)

                        print(
                            f"\nWhat is the answer of: {n1} + {n2} * {n3}?: ")
                        try:
                            user_ans = int(input("").strip())
                        except ValueError:
                            print("That is not a number! Give a numeric answer!")
                            continue
                        actual_ans = n1+(n2*n3)

                        if user_ans == actual_ans:
                            if game_2_done == False or played_games_count >= 2:
                                print("\nCorrect answer!")
                                print("You have been awarded with a magic crystal!")
                                magic_crystals += 1
                                game_2_done = True
                                played_games_count += 1
                                break
                            else:
                                print(
                                    "\nCorrect answer! \nSince you already completed this game, you obtain no extra crystal. \nTry another game.")
                                break
                        else:
                            print("\nWrong answer! \nTry again!")
                            continue

                if current_game == "3":
                    room = "cave"
                    print("\nYou exited gate 1.")
                    print(f"\nYou have [{magic_crystals}] magic crystal/s.")
                    should_play = None
                    break

                print(f"\nYou have [{magic_crystals}] magic crystal/s.")

            while room == "2":
                if registered_4 == False:
                    print("\n || Welcome Again, Player! || ")
                    print("\nYou have unlocked gate 2!")
                    print(
                        "\nI am the boss here, if you want to exit this cave, you must score at least 2 points in three games of rock paper scissors against me.")
                    registered_4 = True

                user_inp_to_start = input(
                    "\nAre you ready? (y/n): ").lower().strip()

                if user_inp_to_start == "y":

                    list_of_choices = ("🪨",  "📃", "✂️")
                    dictionary_of_choices = {"r": "🪨", "p": "📃", "s": "✂️"}

                    program_has_ran = False

                    user_score = 0
                    count = 0

                    def choices(user_inp, opp_inp):
                        try:
                            print(
                                f"You chose: {dictionary_of_choices[user_inp]}")
                        except (IndexError, TypeError, ValueError, KeyError) as e:
                            return e

                        print(f"Opponent chose: {opp_inp}")

                    while True:
                        if program_has_ran == True:
                            print()
                            count += 1

                            if count == 3:
                                if user_score >= 2:
                                    print(
                                        "\nFine, Player! \nYou have won! \nYou are free to go now.")
                                    sys.exit(
                                        "\nPOV: You are teleported out of the forest.\n")
                                else:
                                    print(
                                        f"You Lost! Your score is {user_score}/3.")
                                    program_has_ran = False
                                    count = 0
                                    user_score = 0
                                    break

                        while True:
                            print()
                            random_value = random.randint(0, 2)
                            user_inp = (
                                input("\nRock, paper or scissors? (r/p/s): ")).lower().strip()
                            opp_inp = list_of_choices[random_value]

                            if user_inp == "r":
                                choices(user_inp, opp_inp)
                                if random_value == 0:
                                    print("Draw!")
                                elif random_value == 1:
                                    print("You Lose!")
                                elif random_value == 2:
                                    print("You Win!")
                                    user_score += 1
                                print(f"Your Score: {user_score}/3")
                                break
                            elif user_inp == "p":
                                choices(user_inp, opp_inp)
                                if random_value == 0:
                                    print("You Win!")
                                    user_score += 1
                                elif random_value == 1:
                                    print("Draw!")
                                elif random_value == 2:
                                    print("You Lose!")
                                print(f"Your Score: {user_score}/3")
                                break
                            elif user_inp == "s":
                                choices(user_inp, opp_inp)
                                if random_value == 0:
                                    print("You Lose!")
                                elif random_value == 1:
                                    print("You Win!")
                                    user_score += 1
                                elif random_value == 2:
                                    print("Draw!")
                                print(f"Your Score: {user_score}/3")
                                break
                            else:
                                print("Invalid Choice!")
                                print(f"Your Score: {user_score}/3")

                        program_has_ran = True

                elif user_inp_to_start == "n":
                    print("\nWhat? You scared?")
                    print("\nYou exited gate 2.")
                    room = "cave"

                else:
                    print("\nWhat are you saying? \nAnswer in (y/n)")


play_game()
