#pick random number
#user can guess number
#maybe hint
import random

def check_number(n, guess):
    if n == guess:
        print("YAY!! the number was ", n)
        return True
    elif guess < n:
        print("to low")
    elif guess > n:
        print("to high")

def main():
    n = random.randint(0,100)
    #pick num
    guess = int(input())
    #each guess check
    while True:
        correct = check_number(n, guess)
        guess = int(input())
        if correct:
            break

if __name__ == "__main__":
    main()
