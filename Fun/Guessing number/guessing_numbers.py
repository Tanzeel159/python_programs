import random
print("Welcome to Number guessing game.")
name = input("Your name: ")
print("Hello ",name,", I have chosen a number between 1 and 10 in mind.\nYou have five guesses.\nGoodluck.")
random_number = random.randint(1,10)
i = 0
while(i < 5):
 answer = int(input(":"))
 if answer == random_number:
  print("Great, you have guessed the number in ",i + 1,"guesses\nanswer= ",answer)
  break
 else:
  print(5 - i - 1,"chances left")
 i += 1
else:
 print("sorry Sherlock, your guesses havent been accurate this time.\nThe answer is ",random_number)

print("bye ",name," until next time")
