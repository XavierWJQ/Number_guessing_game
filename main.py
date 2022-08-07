
from art import logo
from random import randint
print(logo)

easy_mode = 10
hard_mode = 5

def difficulty():
  level = input("Choose a difficulty.'easy' or 'hard'? pick one of them: ")
  if level == "easy":
    return easy_mode
  else:
    return hard_mode

def compare(guess, target, attempt):
  if guess > target:
    print("Too High")
    return attempt -1
  elif guess < target:
    print("Too Low")
    return attempt -1
  elif guess == target:
    print(f"You got it, the number is {target}.")

def Guess_Game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  attempt = difficulty()
  target = randint(1,101)
  
  guess = 0
  while guess != target:
    print(f"You have {attempt} chance to guess.")
    guess = int(input("Make a guess: \n"))
    attempt = compare(guess, target, attempt)
    if attempt == 0:
      print(f"You've ran out of chance, Game Over, the answer is {target}.")
      return
    elif guess != target:
      print("Guess again.")
  
Guess_Game()
