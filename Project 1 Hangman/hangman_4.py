"""
Stage 4
Description
The game is now more difficult to beat; your chances of guessing the word depend on the list size. If there are four words in the list, you have a 25% chance.
Let's show a little mercy and add hints for our players.

Objectives
As in the previous stage, use the following word list: python, java, swift, javascript;
Once the computer has chosen a word from the list, show its first three letters. Replace the hidden letters with hyphens (-).
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

H A N G M A N
Guess the word jav-: > java
You survived!
Example 2:

H A N G M A N
Guess the word pyt---: > pythia
You
"""

import random

words = ["python", "java", "swift", "javascript"]

word = random.choice(words)
print(f"H A N G M A N")
iword = input(f"Guess the word {word[:3]}{'-' * len(word[3:])} : ")
if iword == word:
    print("You survived!")
else:
    print("You lost!")
