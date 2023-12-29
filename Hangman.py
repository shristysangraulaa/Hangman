import random
import hangman_art as ha
import hangman_word

print(ha.logo)
word_list = hangman_word.word_list
stages = 0
lives = 6
end_of_game = False

chosen_word = random.choice(word_list)
print(ha.stages[stages])

chosen_word_list = list(chosen_word)
display = ["_" for _ in chosen_word]
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word_list:
        for index, letter in enumerate(chosen_word_list):
            if letter == guess:
                display[index] = guess
                print(display)
    else:
        lives -= 1
        stages += 1
        print(ha.stages[stages])

        if lives == 0:
            print(f'You lose. The word was "{chosen_word}"')

            end_of_game = True



    if "_" not in display:
        print("You win!")
        print(display)
        end_of_game = True




