import random

secret = random.randint(1,100)
attempt = 0
print("I'm thinking a number between 1 and 100...")

while True:
    guess_txt = input("Your guess ... ")
    if not guess_txt.isdigit():
        print("Enter a whole number")
        continue
    guess= int(guess_txt)
    attempt += 1
    if guess > secret:
        print("Value  is too high")
    elif guess < secret:
        print("Value is too low")
    else:
        print(f"Correct!! You took {attempt}  attempts")
        break

