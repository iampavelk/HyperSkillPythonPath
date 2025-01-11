"""
Objectives
Players start the game with eight lives. In other words, they can make a mistake only eight times.

When players input a valid letter, uncover it in the word, and carry on;
Print That letter doesn't appear in the word. and reduce the number of attempts if the word doesn't contain the letter, even if this particular letter has already been suggested before;
Print No improvements. and reduce the attempt' counter when players input a letter that has been successfully uncovered before;
When players win, print the uncovered word, You guessed the word! , and the winning message. Each one should be on a new line.

------------------------------------------
Example 1: note how the attempts are decreased when the player inputs the same letter twice or thrice

H A N G M A N  # 8 attempts

------
Input a letter: > t

--t---
Input a letter: > z
That letter doesn't appear in the word.  # 7 attempts

--t---
Input a letter: > t
No improvements.  # 6 attempts

--t---
Input a letter: > t
No improvements.  # 5 attempts

--t---
Input a letter: > y

-yt---
Input a letter: > x
That letter doesn't appear in the word.  # 4 attempts

-yt---
Input a letter: > y
No improvements.  # 3 attempts

-yt---
Input a letter: > p

pyt---
Input a letter: > p
No improvements.  # 2 attempts

pyt---
Input a letter: > q
That letter doesn't appear in the word.  # 1 attempt

pyt---
Input a letter: > p
No improvements.  # 0 attempts

You lost!
Example 2: success

H A N G M A N  # 8 attempts

----
Input a letter: > j

j---
Input a letter: > i
That letter doesn't appear in the word.  # 7 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 6 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 5 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 4 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 3 attempts

j---
Input a letter: > a

ja-a
Input a letter: > v

java
You guessed the word!
You survived!
"""

import random

words = ["python", "java", "swift", "javascript"]
word = random.choice(words)
print(f"H A N G M A N \n")
hidden = ["-"] * len(word)
t = 0
while t < 8:
    print("".join(hidden))
    l = input("Input a letter: ")
    if l in word:
        if l in hidden:
            t += 1
            print("No improvements. \n")
        else:
            for j in range(len(word)):
                if word[j] == l:
                    hidden[j] = l
            print("")
        if "-" not in hidden:
            print("".join(hidden))
            print("You guessed the word!")
            print("You survived!")
            break
    else:
        t += 1
        print(f"That letter doesn't appear in the word.")
        print("")

if "-" in hidden:
    print("You lost!")
