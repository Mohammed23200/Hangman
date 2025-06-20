import random
import hangman_words
import hangManArt
print(hangManArt.logo)
life = 6
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
placeholder = ''
for i in range(0, len(chosen_word)):
    placeholder += '_'
print(f"word to guess {placeholder}")
print(f"****************************6/6 LIVES LEFT****************************")

gameOver = False
display = ''
correct_letters = []

while not gameOver:
    display = ''
    guess = input("guess a letter :")

    for word in chosen_word:
        if guess == word:
            correct_letters.append(guess)
        if word in correct_letters:
            display += word
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        life -=1
        if life == 0:
            gameOver = True
            print(hangManArt.stages[life])
            print("you lose !")
            print(f"****************************{life}/6 LIVES LEFT****************************")
        elif life == 1:
            print(
                hangManArt.stages[life])
            print(f"****************************{life}/6 LIVES LEFT****************************")
        elif life == 2:
            print(hangManArt.stages[life])
            print(f"****************************{life}/6 LIVES LEFT****************************")
        elif life == 3:
            print(hangManArt.stages[life])
            print(f"****************************{life}/6 LIVES LEFT****************************")
        elif life == 4:
            print(hangManArt.stages[life])
            print(f"****************************{life}/6 LIVES LEFT****************************")
        elif life == 5:
            print(hangManArt.stages[life])
            print(f"****************************{life}/6 LIVES LEFT****************************")
        elif life == 6:
            print(hangManArt.stages[life])
            print(f"****************************{life}/6 LIVES LEFT****************************")

    if "_" not in display:
        gameOver = True
        print("you win 🎉")