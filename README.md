Hangman Flowchart:

![HangmanFlowchart](../PythonProject/flowchart.png)

TODOs:

I
1. Import the words list from hangman_words.py
2. Import stages, logo from hangman_art.py
3. Print the logo at the start of the game
4. Randomly choose a word from the hangman_words and assign it to a variable chosen_word.
5. Ask user to guess a letter and assign their answer to a variable called guess.
Make guess lowercase
6. Check if the letter the user guessed (guess) is one of the letters in the chosen_word

II
1. Create an empty string called placeholder. For each letter in the chosen_word add a "-" to a placeholder so if the chosen_word was "apple", placeholder should be "-----"
with 5 "-" representing each letter to guess

III
1. Create an empty string called "display". Loop through each letter in the chosen_word. If the letter at that position matches guess, then reveal letter in the display at that position
e.g. if the user guessed "p" and the chosen_word was "apple". then display should be 
.pp..
2. Print display, and you should see the guessed letter in the correct position
but every letter that is not a match is represented by a "_"

IV
1. Use a While loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word. At that point display has no more blanks("_"), then you can tell the user they have won.
2. Update the for loop so that previous guesses are added to the display string. At that moment, when the user makes a new guess, the previous guess gets replaced by a "_". we need to fix that by updating the for loop

V
1. Create a variable called lives to keep track of the number of lives left. Set lives equal to 6
2. If guess is not a letter in the chosen word, then reduce lives by 1. if lives goes down to 0, then the game should end. it should print "You Lose!"
3. Print the ASCII art from the list stages that corresponds to the current number of lives that user has remaining

VI
1. If the user has entered a letter they have already guessed, print the letter
and let them know. we should not deduct a life for this 
e.g.you have already guessed
2. If the letter is not in the chosen_word, print out the letter and let them know
e.g. you guessed d, that is not in the word. you lose a life.

VII
1. Update the code below to tell the user how many lives they have left
e.g. print(f"************  {lives}/6 lives left  ************")