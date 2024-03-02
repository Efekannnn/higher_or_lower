from game_data import data
import art
import random

random_data_number = random.randint(0, 49)


def computer(random_data_number):
    print("\n")

    print(data[random_data_number]["name"])
    print(data[random_data_number]["follower_count"])
    print(data[random_data_number]["description"])
    print(data[random_data_number]["country"])

    follower = (data[random_data_number]["follower_count"])
    return follower


def player():

    random_data_number = random.randint(0, 49)

    print(data[random_data_number]["name"])
    print(data[random_data_number]["description"])
    print(data[random_data_number]["country"])

    follower = (data[random_data_number]["follower_count"])
    return follower


def comparison():
    decision = input("Higher or lower:  ").lower()

    if computer_follower > player_follower and decision == "lower":
        print("The answer is right")
        return True
    elif computer_follower < player_follower and decision == "higher":
        print("The answer is right")
        return True
    else:
        print("The answer is false")
        return False


again = True


print(art.logo)

while again:
    computer_follower = computer(random_data_number)

    print(art.vs)

    player_follower = player()

    again = comparison()

    print("---------------------------------------------------------")