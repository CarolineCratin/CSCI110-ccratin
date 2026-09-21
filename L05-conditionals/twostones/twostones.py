def two_stones(n):
    #check if odd
    if n % 2 == 0:
        return("Bob")
    else:
        return("Alice")

if __name__ == "__main__":
    print(two_stones(int(input())))