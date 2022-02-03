#Hangman Program for user to guess a sportsperson from a sport of their choice

cricket=['Ben Stokes','Yuvraj Singh','Andre Russel','Mitchell Starc','Sachin Tendulkar','Umesh Yadav','Rohit Sharma']
    #making list of players of sport 1(cricket)

cricket2=[]
    #making empty list to append later

for i in cricket:
    #for loop to iterate through list 

    a=i.replace(' ','')
        #removing spaces in the given names
    
    b=a.lower()
        #making all characters lowecase
    
    cricket2.append(b)
        #making final new list
    
football=['Paulo Dybala','Anthony Martial','Thomas Muller','Harry Kane','Cristiano Ronaldo','Lionel Messi','Sunil Chhetri']

football2=[]
for i in football:
    c=i.replace(' ','')
    
    d=c.lower()
    
    football2.append(d)
    #repeating same process for sport 2 (football)    

basketball=['James Harden','Shaquille O Neal','Charles Barkley','Kevin Durant','Kobe Bryant','Micheal Jordan','Stephen Curry']

basketball2=[]
for i in basketball:

    e=i.replace(' ','')
    
    f=e.lower()
    
    basketball2.append(f)
  	 #repeating same process for sport 3 (basketball)

tennis=['Venus Williams','Leander Paes','Andy Roddick','Roger Federer','Novak Djokovic','Rafael Nadal','Andy Murray']

tennis2=[]
for i in tennis:

    g=i.replace(' ','')
    
    h=g.lower()
    
    tennis2.append(h)
    #repeating same process for sport 4 (tennis)

running=['Anish Sundaraman','Usain Bolt','Mohammed Adnan','Carl Lewis','Justin Gatlin','Linford Christie','Andy Murray']

running2=[]
for i in running:

    k=i.replace(' ','')
    
    l=k.lower()
    
    running2.append(l)

    #repeating same process for sport 5 (running)

import time
    #importing the time module

print()

name = input("What is your name? ")
    #welcoming the user 
    
time.sleep(0.75)
    #wait for 0.75 second
   
print()

print ("Hello, " + name, "time to play Hangman!")
    #greeting
    
time.sleep(1.25)
    #wait for 1.25 second

print("""
The rules are simple. You have 8 guesses to try and figure out the name of the
sportsperson from the sport you have chosen. If you get 8 guesses wrong, then
you lose. If you can guess the name of the sportsperson before you get 8 wrong
guesses, then you win.
Have fun! """)
    #rules

print ()

time.sleep(6)
    #wait for 6 second

import random

print('Choose a sport (cricket,football,basketball,tennis) to guess a sportsperson from.')

print()
    
sport=input('Enter sport of choice: ')

secret1=''

if sport=='cricket':
    secret1=random.choice(cricket2)

elif sport=='football':
    secret1=random.choice(football2)

elif sport=='basketball':
    secret1=random.choice(basketball2)

elif sport=='tennis':
    secret1=random.choice(tennis2)
    
elif sport=='running':
    secret1=random.choice(running2)

else:
    print('Invalid sport chosen')
    
print ("Start guessing...")
time.sleep(0.5)
    #time delay using time module
    
word = secret1
    #here we set the secret

guesses = ''
    #creates a variable with an empty value

turns = 10
    #determine the number of turns

    # Create a while loop

while turns > 0:
    #check if the turns are more than zero     
    
    failed = 0
        # make a counter that starts with zero         
       
    for char in word:
        # for every character in secret word 
   
        if char in guesses:
            # see if the character is in the players guess 
    
            print (char,end=' '),
                # print then out the character

        else:

            print ("_",end=' ')
                # if not found, print a dash
       
            failed += 1
                # and increase the failed counter with one

        # if failed is equal to zero

    if failed == 0:        
        print ()
        print ("You won! :) ")
            # print you won

        break
            # exit the script    

    print()
    print()
        
    guess = input("guess a character: ")
        # ask the user to guess a character

    time.sleep(0.25)
        #wait for 0.25 second
        
    guesses += guess
        # set the players guess to guesses                

    if guess not in word:
        # if the guess is not found in the secret word
 
        turns -= 1
            # turns counter decreases with 1 (now 9)  
    
        print ("Wrong")
            # print wrong
 
        print ("You have", + turns, 'more guesses')
            # how many turns are left
 
        if turns == 0:
            # if the turns are equal to zero     
    
            print ()
            print ("You Lost :( ")
                # print "You Lost"
