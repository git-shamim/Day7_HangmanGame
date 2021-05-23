
import random
from art import Logo, Stages
from words import WordList

print(Logo)

chosen_word = random.choice(WordList)

display = []

for letter in chosen_word:
    display += "_"

print(display)

lives = 0
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You have already guessed letter {}".format(guess))

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print("Good job, keep going!")
    print(display)

    if guess not in chosen_word:
        lives += 1
        print("You guessed letter {0}, that's not right. You lose a life, you have {1} chances left ".
              format(guess, (7 - lives)))
        print(Stages[lives - 1])
        if lives == 7:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You Win!")
