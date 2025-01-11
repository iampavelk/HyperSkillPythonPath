import random

words = ["python", "java", "swift", "javascript"]
print(f"H A N G M A N \n")
wins, loses = 0, 0
while True:
    game = input(
        'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
    )
    if game == "play":
        word = random.choice(words)
        hidden = ["-"] * len(word)
        t = 0
        used = []
        while t < 8:
            print("\n" + "".join(hidden))
            l = input("Input a letter: ")
            if len(l) != 1:
                print("Please, input a single letter.")
            elif not (l.islower() and "a" <= l <= "z"):
                print("Please, enter a lowercase letter from the English alphabet.")
            elif l in used:
                print("You've already guessed this letter")
            elif l in word:
                used.append(l)
                for j in range(len(word)):
                    if word[j] == l:
                        hidden[j] = l
                if "-" not in hidden:
                    print("".join(hidden))
                    print(f"You guessed the word {word}!")
                    print("You survived!")
                    wins += 1
                    break
            else:
                print(f"That letter doesn't appear in the word.")
                used.append(l)
                t += 1
        if "-" in hidden:
            print("You lost!")
            loses += 1
    elif game == "results":
        print(f"You won: {wins} times. \nYou lost: {loses} times")
    else:
        break
