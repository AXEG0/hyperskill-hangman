import random

def open(var, data):
    for var_loop in range(len(var)):
        if var[var_loop] not in data:
            var = var.replace(var[var_loop], "-")
        else:
            continue
    return var

def lowercase(x):
    if x.islower():
        return True
    else:
        return False

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']

while True:
    
    start = input('Type "play" to play the game, "exit" to quit:')
    if start == "exit":
        break
    elif start != "play":
        continue
    
    random.shuffle(words)
    hint = "-" * len(words[0])
    a_set = set()
    all_set = set()
    lives = 8

    while True:
        print()
        print(hint)
        attempt = input("Input a letter:")

        if len(attempt) > 1:
            print("You should input a single letter")
            continue
        elif lowercase(attempt) == False:
            print("Please enter a lowercase English letter")
            continue

        if attempt in all_set:
            print("You've already guessed this letter")
            continue

        all_set.add(attempt)

        if attempt not in words[0]:
            print("That letter doesn't appear in the word")
            lives -= 1
            if lives == 0:
                print("You lost!")
                break
            continue

        a_set.add(attempt)
        res = open(words[0], a_set)
        hint = res

        if res == words[0]:
            print("You guessed the word!")
            print("You survived!")
            break

