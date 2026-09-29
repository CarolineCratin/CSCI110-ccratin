def low(huh):
    #this is so we can count
    a = int(0)
    #check all the numbers
    for i in huh:
        #is it negative?
        if i < 0:
            #if so add 1 to the counter
            a += 1
    #we have a final count after goint through all numbers in list
    return a

def main():
    #number of numbers in list
    n = int(input())
    #actualy list the numbers :D
    huh = [int(n) for n in input().split()]
    #call and print
    print(low(huh))

if __name__ == "__main__":
    #go to main to get imputs
    main()