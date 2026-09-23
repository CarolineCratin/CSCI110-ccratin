def adding(a,b,c):
    d = a + b
    if d == c:
        return "correct!"
    else:
        return "wrong!"

def main():
    a, b, c = map(int,input().split())
    print(adding(a,b,c))

if __name__ == "__main__":
    main()