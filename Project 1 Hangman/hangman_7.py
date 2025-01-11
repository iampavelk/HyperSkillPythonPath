import random

words = ["python", "java", "swift", "javascript"]
word = random.choice(words)
print(f"H A N G M A N \n")
hidden = ["-"] * len(word)
t = 0
while t < 8:
    print("".join(hidden))
    l = input("Input a letter: ")
    if len(l) != 1:
        print("Please, input a single letter. \n")
    elif not (l.islower() and "a" <= l <= "z"):
        print("Please, enter a lowercase letter from the English alphabet. \n")
    elif l in word:
        if l in hidden:
            t += 1
            print("You've already guessed this letter \n")
        else:
            for j in range(len(word)):
                if word[j] == l:
                    hidden[j] = l
            print("")
        if "-" not in hidden:
            print("".join(hidden))
            print(f"You guessed the word {word}!")
            print("You survived!")
            break
    else:
        t += 1
        print(f"That letter doesn't appear in the word.")
        print("")

if "-" in hidden:
    print("You lost!")
