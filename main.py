# Hangman Python script
from hangman_words import hangman_words
from hangman_art import logo, stages
from game_over import game_end
import random

# function call to get remaining lives
def guess_not_in_chosen_word(user_guess, lives_left, chosen_word_from_list):
    if user_guess not in chosen_word_from_list.lower():
        print(f"you guessed {user_guess}, that is not in the word. If you miss a letter for each attempt, you lose a life.")
        lives_left -= 1
        print(f"************  {lives_left}/6 lives left  ************")
    return lives_left

# Create am empty string with "_"
def placeholder_for_the_secret_word(chosen_word_from_list):
    blank_line = ""
    for i in range(len(chosen_word_from_list)):
        blank_line += "-"
    return blank_line

# function to update display string
def fill_in_missing_letters(display_string, user_guess, chosen_word_from_list, correct_letter_list):
    for letter in chosen_word_from_list.lower():
        if letter == user_guess:
            display_string += user_guess
            correct_letter_list.append(letter)
        elif letter in correct_letter_list:
            display_string += letter
        else:
            display_string += "_"
    return display_string

def you_lose(lives_left, chosen_word_list):
    if lives_left == 0:
        print("The correct word was", chosen_word_list)
        print("You Lose!")
        print(game_end)
    return lives_left


def you_win(correct_guessed_letters):
    if "_" not in correct_guessed_letters:
        print("You Won!")
        return True
    return False

def play_game():
    lives = 6
    chosen_word = random.choice(hangman_words.words_list)
    display = ""
    correct_letter = []
    game_over = False
    print(logo)
    print("Welcome to Hangman - Word Guessing Game!")
    print(placeholder_for_the_secret_word(chosen_word))
    print(f"************  {lives}/6 lives left  ************")

    while not game_over:
        guess = input("Please enter your guess:").lower()

        if guess in correct_letter:
            print(f"You've already guessed {guess}")

        # function call to update display string
        correct_guessed_letters = fill_in_missing_letters(display, guess, chosen_word, correct_letter)
        print(correct_guessed_letters)

        # function call to get remaining lives
        lives = guess_not_in_chosen_word(guess, lives, chosen_word)

        # lives_left = 0
        if you_lose(lives, chosen_word) == 0:
            game_over = True

        # User guessed all the letters
        if you_win(correct_guessed_letters):
            game_over = True

        print(stages[lives])
    play_game()

if __name__ == '__main__':
    play_game()

