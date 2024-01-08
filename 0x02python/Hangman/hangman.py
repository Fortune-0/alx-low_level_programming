
import random

words = ["apple", "orange", "game", "coco", "fish", "play"]

random_word = random.choice(words)

guess = input("Guess a letter from the secret word: ").lower()

n = len(random_word)
# for char in random_word:
    #print (char)
for i in range (n):
    if guess in random_word.lower():
        print("Correct!")
    # guess = input("Guess a letter from the secret word: ").lower()
    # if guess in random_word.lower():
    #     print("keep going")
else:
    print("Wrong")
#print(char)
print(random_word)
