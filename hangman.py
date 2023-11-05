import random

def choose_word():
    words = ['mowlood','python', 'hangman', 'developer', 'programming', 'engineer', 'teapot' ]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word_to_guess = choose_word().lower()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Adjust this value for difficulty

    print("Welcome to Hangman!")

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nCurrent Word: ", current_display)
        print("Guessed Letters: ", ', '.join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess!")
                guessed_letters.append(guess)
                incorrect_guesses += 1
        else:
            print("Please enter a valid single letter.")

        if incorrect_guesses == max_incorrect_guesses:
            print("Sorry, you ran out of guesses. The word was:", word_to_guess)
            break

        if '_' not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
