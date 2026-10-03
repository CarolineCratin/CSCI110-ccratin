def switches(word):
    #set intial spot
    ball = 1
    #go through all the switches wanted
    for letter in word:
        #give instructions on what to do for each switch
        if letter == "A":
            #check current cup its under
            if ball == 1:
                #make the position switch
                ball +=1
            #the rest is repeated plz dont make me do all the rest of them
            elif ball == 2:
                ball -= 1
        elif letter == "B":
            if ball == 2:
                ball +=1
            elif ball == 3:
                ball -=1
        elif letter == "C":
            if ball == 1:
                ball +=2
            elif ball == 3:
                ball -=2
    #return end position after finishing all asked switched
    return ball

def main():
    #get input
    word = input()
    #go through the process and print what position the ball is in
    #i didn't read the question fully so if im wrong on the items oops
    print(switches(word))

if __name__ == "__main__":
    main()

