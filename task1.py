import random

# Small list of 5 predefined words
words = ["python", "computer", "game", "code", "fun"]

# Select a random word
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("You have 6 incorrect guesses allowed.")
print("Word to guess: " + "_ " * len(word))

# Main game loop
while incorrect_guesses < max_incorrect:
    # Display current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print(f"\nCurrent word: {display}")
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
    
    if guessed_letters:
        print(f"Letters guessed: {', '.join(guessed_letters)}")
    
    # Check if word is complete
    word_complete = True
    for letter in word:
        if letter not in guessed_letters:
            word_complete = False
            break
    
    if word_complete:
        print(f"\nCongratulations! You guessed the word: {word}")
        break
    
    # Get player input
    guess = input("Enter a letter: ").lower()
    
    # Check if letter already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    # Add to guessed letters
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Sorry, '{guess}' is not in the word.")

# Check if game ended due to too many incorrect guesses
if incorrect_guesses >= max_incorrect:
    print(f"\nGame over! The word was: {word}")

print("Thanks for playing!")