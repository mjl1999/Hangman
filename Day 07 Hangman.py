from Day_07_Hangman_words import word_list
from random import choice

# select a random word for the user to guess
target = choice(word_list)
print(target)
display_word = []
for letter in target:
    display_word += "_"
lives = 7
guessed_letters = ""

while lives != 0:
    print(display_word)
    print(f"Guessed letters: {guessed_letters}")
    guess = input("Please guess a letter: ").lower()
    if guess == target:
        display_word = target
        break

    if guess in guessed_letters:
        print("This letter has already been guessed")
        continue
    else:
        guessed_letters += guess

    if guess in target:
        print("Correct!")
        for index in range(len(target)):
            if guess == target[index]:
                display_word[index] = guess
        if display_word == target:
            break
    else:
        lives -= 1
        print(f"Wrong guess: {lives} lives remaining \n")


if lives == 0:
    print(f"\nYou lose! word was: {target.capitalize()}")
else:
    print(f"\nYou win! You had {lives} lives remaining")
