import random, hangman_art, hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo + "\n")

# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
 
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed the letter {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"The letter {guess} isn't in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lose.")
            end_of_game = True

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
