time_6 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''

time_5 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''

time_4 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''

time_3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''

time_2 =  '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''

time_1 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''

time_0 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

import random
import time
words = ["good","bad","ugly"]
random_word = random.choice(words)
guessed_letters = []
distances = ["_"] * len(random_word)
print(" ".join(distances))
print(time_6)
times = 6
while "_" in distances:
  if times > 0:
    guessed = input("Please guess a letter: ")
    while guessed in guessed_letters:
      print("You guessed this letter before")
      guessed = input("Please guess a letter: ")
    guessed_letters.append(guessed)
    for position in range(len(random_word)):
      if random_word[position] == guessed:
        distances[position] = guessed
    if guessed in random_word:
      print(" ".join(distances))
      print(f"You have {times} times left")
    else:
      times -= 1
      print(" ".join(distances))
      print(f"You have {times} times left")
    if times == 6:
      print(time_6)
    elif times == 5:
      print(time_5)
    elif times == 4:
      print(time_4)
    elif times == 3:
      print(time_3)
    elif times == 2:
      print(time_2)
    elif times == 1:
      print(time_1)
  else:
    print(time_0)
    print("You lose")
    time.sleep(2)
    break
if "_" not in distances:
  print("""
       ***************
          You Win
       ***************
       """)
  time.sleep(2)