import string #gets the letters for guesses
from random_word import RandomWords

def print_known(known_letters):
    shown = ''
    for letters in known_letters:
        shown += letters + ' ' 
    print(shown)

def get_guess():
    guess = 'null'
    asking = True
    while asking:
        try: 
            guess = input('\nGuess a letter! ')
            if guess == 'hint' or guess == 'Hint':
                return 'HINT'
            for i in letters:
                if guess.lower() != i:
                    continue
                else:
                    guessed_letters.append(i) #for future use possibly with hints
                    asking = False
                    return guess
        except:
            print('Guess a letter!')
    return guess

def end_game(knownlets, lives):
    if lives == 0:
        return True
    for lets in knownlets:
        if lets == '_':
            return False
    return True

def update_knownlets(theguess):
    #reveal letters in knownlets
    letter_pos = 0
    for letters in word:
        if letters == theguess:
            knownlets[letter_pos] = letters  
        letter_pos += 1

def check_guess(guess, word):
    #see if the guess is correct
    #take away lives if needed
    if guess in word:
        return True
    return False

def free_space():
    print('\n'* 100)

def get_word():
    r = RandomWords()
    getting_word = True
    # Return a single random word
    while getting_word:
        word = r.get_random_word()
        try:
            for i in word:
                if i =='-':
                    pass
                else:
                    getting_word = False
                    return word
        except:
            print('---GENERATING WORD---')
     
            

print('Welcome to Hangman\nBy TullyE\n')
possible_words = ['animals', 'happy', 'stop', 'terminal', 'entering', 'infinite', 'because', 'stopping', 'hangman']
word = get_word()
knownlets = []
for i in word:
    knownlets.append('_')

lives = 7
hints = 3
letters = string.ascii_lowercase
guessed_letters = [] #Not used unless I add hints


playing = True
while playing:
    print(f'lives: {lives}')
    print_known(knownlets)
    guess = get_guess()
    if check_guess(guess, word): #if the guess is correct
        update_knownlets(guess)
    else:
        lives = lives - 1
    if end_game(knownlets, lives):
        update_knownlets(guess)
        print_known(knownlets)
        #free_space()
        break
    #free_space()
if lives == 0:
    print(f'YOU LOST! THE WORD WAS: {word}')
else:
    print(f'\nYOU WON! THE WORD WAS: {word}')