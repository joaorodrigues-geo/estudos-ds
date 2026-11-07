import random
import hangman_words as hw
from hangman_art import stages, logo


lives = 6


print(logo)
chosen_word = random.choice(hw.word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(guess)
        print("Letter already guessed")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print("This letter is not in the word. You lose a life.")


        if lives == 0:
            game_over = True

          
            print(f"The correct word is '{chosen_word}!!\nNow you are out of lives...")
            print(f"***********************YOU LOSE**********************")


    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

   
    print(stages[lives])
