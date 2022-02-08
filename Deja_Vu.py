import time
import random
import enum


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def print_pause(message_to_print, delay=2):
    print(Color.get_color() + message_to_print)
    time.sleep(delay)


def valid_input(prompt, choices):
    while True:
        choice = input(prompt).lower()
        if choice in choices:
            return choice
        print_pause(f"I'm sorry, love. That isn't an option.")


def character():
    person = ["man", "woman"]
    height = ["tall", "short"]
    hair_color = ["red", "orange", "green", "blue", "purple", "pink",
                  "black", "brown", "blonde", "white", "gray"]
    eye_color = ["brown", "green", "hazel", "blue", "gray", "amber"]
    print_pause(
        "You see a " + (random.choice(height)) + " "
        + (random.choice(person)) + " with" + " "
        + (random.choice(hair_color)) + " hair and " +
        random.choice(eye_color) + " eyes."
        )


def intro(items):
    print_pause("You find yourself in the middle of a dark abyss.")
    print_pause("You can't remember anything about your life or this place.")
    print_pause("You see an illuminated pathway stretching a vast distance.")
    print_pause("Suddenly, a white mist appears in front of you.")
    print_pause("The mist condenses and takes the shape of a human")
    character()
    print_pause("They exclaim: 'Oh my, love, aren't you the early bird!'")
    print_pause("'You are here far too soon. You must return home at once!'")
    print_pause("The guide motions to your sides before asking:")
    guide(items)


def guide(items):
    choice = valid_input("'Which hall shall you choose?'\n"
                         "1 for Past \n"
                         "2 for Present\n", ["1", "2"])
    if choice == "1":
        past(items)
    elif choice == "2":
        present(items)


def past(items):
    print_pause("The path rotates around you and stops, aiming left.")
    print_pause("At the end of the path, you see a large white room.")
    print_pause("You enter the room, which only contains a mirror.")

    if "Memory" in items:
        print_pause("There is nothing left to do here.")
        print_pause("You stare at your reflection before turning back.")
    else:

        print_pause("In the mirror, a silhouette is staring back at you.")
        print_pause("The being's eyes are familiar to you as you gaze ahead.")
        print_pause("Without breaking eye contact, the being morphs.")
        character()
        print_pause("You recognize it as yourself and memories come")
        print_pause("flooding back into your mind.")
        items.append("Memory")
        print_pause("The last thing that you remember before coming to this")
        print_pause("strange place is walking to work Friday morning.")
        print_pause("You saw a bright light and then felt an immense force...")
        print_pause("The bus! You forgot to look before crossing! Oh, no...")
        print_pause("You mourn your life for a moment before turning back.")

    print_pause("You walk back to the guide")
    guide(items)


def present(items):
    print_pause("The path rotates around you and stops, aiming right.")
    print_pause("At the end of the path, you see a large white room.")
    print_pause("You enter the room, which only contains a doorframe.")
    print_pause("You walk through the door into a blinding light.")
    print_pause("You awake to the sound of an alarm clock.")
    print_pause("You feel odd, like you've forgotten something important.")
    print_pause("You look around and realize that you are home...")
    print_pause("And late for work! You rush to get dressed and leave.")
    print_pause("You run out of your house and down the block full-speed.")
    print_pause("You run through a crowd gathered by a crosswalk.")
    if "Memory" in items:
        print_pause("A sudden intense feeling of Deja Vu causes the hair")
        print_pause("on your neck to stand up and you slam to a halt.")
        print_pause("You see a bus barrelling down the road toward you.")
        print_pause("The bus flies by, narrowly missing you.")
        print_pause("You remain frozen for a moment until the shock fades.")
        print_pause("You say some words of gratitude and head to work.")
        print_pause("You feel lucky to be alive; you're divinely protected.")
        print_pause("Your gratitude for this day lasts for decades to come.")
        print_pause("CONGRATULATIONS, YOU WON!")
        play_again()
    else:
        print_pause("You run through the crosswalk and see a bright light.")
        print_pause("An immense force hits you, tossing you to the ground.")
        print_pause("You wake up in the abyss once more.")
        print_pause("GAME OVER")
        play_again()


def play_again():
    print_pause("Would you like to play again?")
    restart = input("Y for yes \n"
                    "N for no\n").lower()
    if restart == "y":
        play_game()

    if restart == "n":
        print_pause("Thanks for playing! Have a great day!")
        exit()

    else:
        print_pause("I'm sorry, these are your only options.")
        play_again()


def play_game():
    items = []
    intro(items)
    guide(items)


def game():
    while True:
        play_game()
        play_again()


if __name__ == '__main__':
    game()
