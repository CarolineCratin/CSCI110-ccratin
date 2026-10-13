def sum(list):
    #make things to add things to
    a = 0
    for i in list:
        #add everythin in list
        a += i
    #yay
    return a

def main():
    #inputs and defining
    n = int(input())
    list = [int(n) for n in input().split()]

    print(sum(list))

#Make pytest ignore inputs
if __name__ == "__main__":
    main()