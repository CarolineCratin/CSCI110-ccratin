#calling a function syntax:fun_name(thing1, thing2, ect)

#print() is a function that takes any number of arguments of any type
#/n for new line
#input() takes 0 or 1 argument (like a prompt) ex: input("hows your day? ") and it still lets you input

#casting functions take one argument
#a = int(-3.9) #would be -3, just get rid of desimals
#b = int("2") #works
# c = int("2.4") #doesn't work

#d = float(3) #includes the decimal
#e = float("5.3") #works

#f = str(5.1)

#g = bool(" ")

# len() (lenth) takes one argument (string) gives # of characters
#h = len("10") #needs to take string
#i = len(10) #doesnt work

#abs() takes one argument (number) and gives the absolute value
#max() takes two arguments (#) and gives the bigger one
#j = max(1, 3) #print(j) gives 3

#round() takes one or two arguments
#k = round(2.5) #with .5 it rounds to the nearest even value
#l = round(1.347586, 3) #number you want to round, the digits you want to round to

a = input("do you feel more yippee or yahoo? ")

def yahoo(): 
    print(a, "I mean, I guess")
    print("unfortunate")
    print (a, a, a, a, a, a, a, a, a, a)
def yippee():
    print("You Yippee?")
    print("YIPPEE YIPPEE YIPPEE YIPPEE YIPPEE YIPPEE YIPPEE YIPPEE mayhaps even a yahoo")

if a = str("yahoo"):
    yahoo()
else:
    print "huh"
if a = str("yippee"):
    yippee()
else:
    print("not it :(")

age = int(input())
#if a8 or older you can vote
#syntax: if boolean:
if age >= 18:
    print ("you can vote")
#you dont need else if
elif age < 0:
    print("nuhuh not possible")
#you dont NEED an else but after else you cant do anymore elfi
else:
    print("you can't vote :(")

#a=a+2 is the same as a+=2 its a condenced version
#% modulo - 5%2 = 1 or 9%5 = 4