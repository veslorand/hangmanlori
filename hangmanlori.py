import random
import os
import string

def space(word):
    space_picked = ""
    for i in range(len(word)):
        if word[i] == " ":
            space_picked += ""
        if i != range(len(word))[-1]:
            space_picked += word[i] + " "
        else:
            space_picked += word[i]
    return space_picked.upper()



def pick_capital():
    '''
    Picks a random European capital
    Returns:
    str: The name of European capital
    '''
    capitals = ["Rome", "Los Angeles"]
    picked = random.choice(capitals)
    space(picked)
    return space(picked.upper())

def get_hashed(password):
    '''
    Generates a password based on the word with dashes instead of letters
    Keeps whitespaces undashed.
    Args:
    str: The word to hash
    Returns:
    str: The hashed password
    '''
    hashed = ""
    for i in range(len(password)):
        if password[i] == " ":
            hashed += password[i]
        else:
            hashed += "_"
    return hashed


def uncover(hashed_password, password, letter):
    '''
    Uncovers all occurences of the given letter in the hashed password based on the password
    Args:
    str: The hashed password
    str: The password
    str: The letter to uncover
    Returns:
    str: The hashed password with uncovered letter
    '''
    uncovered_password = ""
    for i in range(len(password)):
        if password[i] == letter:
            uncovered_password += letter
        elif password[i] == " ":
            uncovered_password += " "
        else:
            uncovered_password += "_"
    print(uncovered_password)
    hashed_password == uncovered_password


def update(used_letters, letter):
    '''
    Appends the letter to used_letters if it doesn't occur
    Args:
    list: The list of already used letters
    str: The letter to append
    Returns:
    list: The updated list of already used letters
    '''
    pass
    for i in letter:
        if i not in used_letters:
            pass


def is_win(hashed_password, password):
    '''
    Checks if the hashed password is fully uncovered
    Args:
    str: The hashed password
    str: The password
    Returns:
    bool:
    '''
    if hashed_password == password:
        print("YOU WON THE GAME!")
        quit()


def is_loose(life_points, password):
    '''
    Checks if life points is equal 0
    Args:
    int: The life life_points
    Returns:
    bool: True if life point is equal 0, False otherwise
    '''
    if life_points == 0:
        print("You lost the game!")
        print("Your word was: " + str(password))
        quit()

def input_check(letter, password):
    is_win(letter, password)

def get_input(password, used_letters, life_points, hashed_password):
    while True:
        letter = input("Enter your letter -->").upper()
        letter = space(letter)
        input_check(letter, password)
        if letter == " " or letter == "":
            print("It was just a whitespace or nothing. Try again!")
        elif len(letter) > 1:
            print("Enter only one character at a time")
        elif letter in used_letters:
            print("You already guessed this letter. Try again!")
        elif letter not in string.ascii_letters:
            print("Not a valid character")
        else:
            return letter.upper()

def printing(hashed_password, used_letters, life_points):
    password_letters = 0
    for i in hashed_password:
        if i != " ":
            password_letters += 1
    if len(used_letters) == 0:
        print("LET'S START!")
        print("Your word contains: " + str(password_letters) + " letters.")
        print("You have " + str(life_points) + " life points.")
    else:
        print("HANGMAN")
        print(hashed_password)
        for i in range(len(used_letters) -1):
            print(used_letters[i] + ", ")
        print("Your life points: " + str(life_points))


def main():
    password = pick_capital()
    hashed_password = get_hashed(password)
    used_letters = []
    life_points = 1
    while True:
        is_win(hashed_password, password)
        is_loose(life_points, password)
        printing(hashed_password, used_letters, life_points)
        letter = get_input(password, used_letters, life_points, hashed_password)
        uncover(hashed_password, password, letter)


if __name__ == '__main__':
    main()