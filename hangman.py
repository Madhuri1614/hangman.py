import random
import time

print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)

def main():
    global count, display, word, already_guessed, length, play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game.lower() not in ["y", "n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game.lower() == "y":
        main()
    elif play_game.lower() == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

def hangman():
    global count, display, word, already_guessed
    limit = 5
    print(display)
    guess = input("Enter your guess: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in already_guessed:
        print("Letter already guessed. Try another letter.\n")
        hangman()
    elif guess in word:
        already_guessed.append(guess)
        for i in range(length):
            if word[i] == guess:
                display = display[:i] + guess + display[i+1:]
    else:
        count += 1
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
    if count < limit and '_' in display:
        hangman()
    elif '_' not in display:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    else:
        print("Sorry, you've run out of guesses. The word was:", word)
        play_loop()
