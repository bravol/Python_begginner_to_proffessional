import random

stages = [
    r'''      
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
  ''', r'''     
     _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___
 ''', r'''     
     _______
     |/      |
     |      (_)
     |      
     |       
     |     
     |
    _|___ 
 ''', r'''     
     _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
 '''
]

word_list=['aardvark','baboon', 'camel', 'donkey', 'man']

print(r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

''')

# todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it
# todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase
# todo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. print "Right" if it is, "Wrong" if it is not
# todo-4 - change the loop so that you keep the previous correct letter in display
lives = 4
chosen_word = random.choice(word_list)
placeholder = ''
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)




game_over = False
correct_letters = [] # storing the correct letter guessed

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} which is not in the chosen word, You lose a life!.")
        if lives == 0:
            game_over = True
            print("You loose! Hanged and Killed completely.")
            print(f".................The word was {chosen_word}.......................")
        print(stages[lives])

    if "_" not in  display:
        game_over = True
        print("you win!. You have escaped to be killed")
        print(f"....................{chosen_word}..............................................")
    # todo-5 print the ASCII art from 'stages' that corresponds to the current number of lives the user has remaining
