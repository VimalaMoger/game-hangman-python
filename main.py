# Hangman Python script
from hangman_words import hangman_words
from hangman_art import logo, stages
import random

def play_game():
    lives = 6
    print(logo)

    chosen_word = random.choice(hangman_words.words_list)
    game_over = False
    correct_letter = []

    placeholder = ""
    for i in range(len(chosen_word)):
        placeholder += "_"
    print(placeholder)

    while not game_over:
        print(f"************  {lives}/6 lives left  ************")
        guess = input("Please enter your guess:").lower()
        display = ""
        for letter in chosen_word.lower():
            if letter == guess:
                display += guess
                correct_letter.append(letter)
            elif letter in correct_letter:
                display += letter
            else:
                display += "_"
        print(display)

        if guess in correct_letter:
            print(f"You've already guessed {guess}")

        if guess not in chosen_word.lower():
            print(f"you guessed {guess}, that is not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                game_over = True
                print("The correct word was", chosen_word)
                print("You Lose!")

        if "_" not in display:
            game_over = True
            print("You Won!")

        print(stages[lives])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_game()

