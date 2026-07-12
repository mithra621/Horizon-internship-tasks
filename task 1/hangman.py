import random

# List of predefined words
words = ["python", "apple", "computer", "orange", "school"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while attempts > 0:
    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)

# If attempts become 0
if attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)