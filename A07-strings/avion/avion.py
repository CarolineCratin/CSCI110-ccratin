def find(list):
    a = ''
    for i in list:
        if  "FBI" in i:
            a = a + " " + str(int(list.index(i))+1)
    if a == '':
        a = "HE GOT AWAY!"
    return a
    
        
#used geek for geek
def main():
    #get the list of blimp id
    list = [input() for i in range(5)]
    print(find(list))

#Make pytest ignore this and main
if __name__ == "__main__":
    main()