def check_letter(word, guess):
    if guess == word:
        print("YOU DID IT!!")
        return True
    else:
        for letter in word:
            if letter =


def main():
    word = "known"
    guess = input()
    while True:
        correct = check_letter(word, guess)
        guess = input()
        if correct:
            break

#Make pytest ignore this and main
if __name__ == "__main__":
    main()