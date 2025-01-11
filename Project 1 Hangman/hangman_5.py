"""
Your game should work as follows:

Players have exactly eight attempts to guess the word by entering letters one by one. Asking for a letter, print: Input a letter:.
If a player uncovered all the letters, but some attempts are still left, the program must continue to ask for input until all the tries are exhausted;
If the letter doesn't appear in the word, the computer takes one try away – even if a user has already suggested this letter – and prints That letter doesn't appear in the word.;
If the letter does appear in the word but a user has already suggested this letter and it's open, no need to print any messages;
If all attempts are exhausted, the game ends; the program shows a final message (Thanks for playing!). Otherwise, players can continue to input letters;
We continue to stick with the word list from the previous stage: python, java, swift, javascript. It ensures that your program is tested reliably. Don't worry about javascript.
Yes, it's longer than 8 characters, but we'll keep it in the list for consistency since we're not done with developing the game yet and for now there is no win or lose.
"""

"""
H A N G M A N  # 8 attempts

----
Input a letter: > j  # 7 attempts

j---
Input a letter: > i
That letter doesn't appear in the word.  # 6 attempts

j---
Input a letter: > g
That letter doesn't appear in the word.  # 5 attempts

j---
Input a letter: > o
That letter doesn't appear in the word.  # 4 attempts

j---
Input a letter: > a  # 3 attempts

ja-a
Input a letter: > v  # 2 attempts

java
Input a letter: > a  # 1 attempt

java
Input a letter: > j  # 0 attempts

Thanks for playing!"""

import random

words = ["python", "java", "swift", "javascript"]
word = random.choice(words)
print(f"H A N G M A N \n")
hidden = ["-"] * len(word)
print("".join(hidden))
for i in range(8):
    l = input(f"Input a letter: ")
    if l in word:
        for j in range(len(word)):
            if word[j] == l:
                hidden[j] = l
        print("\n" + "".join(hidden))
    else:
        print(f"That letter doesn't appear in the word.")
        print("\n" + "".join(hidden))
print(f"Thanks for playing!")
