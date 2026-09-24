def has_let(word, a):
    for letter in word:
        if letter == a:
            print(f"this word has an" [a])

def main():
    word = input()
    a = input()
    has_let(word)

if __name__ == "__main__":
    main()