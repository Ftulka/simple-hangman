import random

lives = 8
print("H A N G M A N\n")
hid_words = ["python", "kotlin", "java", "javascript"]
hid_word = random.choice(hid_words)
pub_word = list(len(hid_word) * '-')
chars_set = set(hid_word)
used_sym = set()


def check_valid(used_sym, guess_str):
    if len(guess_str) != 1:
        print('You should input a single letter')
    elif not (guess_str.isalpha() and guess_str.islower()):
        print('Please enter a lowercase English letter')
    elif guess_str in used_sym:
        print("You've already guessed this letter")
    else:
        return True
    return False


def lucky_shot(guess, chars_set, hid_word, pub_word):
    chars_set.remove(guess)
    indexes = [i for i in range(len(hid_word)) if hid_word[i] == guess]
    for i in indexes:
        pub_word[i] = guess


while True:
    start_word = input('Type "play" to play the game, "exit" to quit: ')
    if start_word == 'play':
        while lives > 0:
            print(f"\n{''.join(pub_word)}")
            guess = input('Input a letter: ')
            if check_valid(used_sym, guess):
                used_sym.add(guess)
                if guess in chars_set:
                    lucky_shot(guess, chars_set, hid_word, pub_word)
                else:
                    print("That letter doesn't appear in the word")
                    lives -= 1
            if not chars_set:
                break

        if '-' in pub_word:
            print('You lost!\n')
        else:
            print(f"You guessed the word {hid_word}!")
            print('You survived!\n')
    elif start_word == 'exit':
        break
