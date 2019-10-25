import time
name = input("What is your name? ")
print ("Hello, " + str({name}), "Time to play hangman!")
print ("")
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)
word = "amanpatil"
guesses = ''
turns = len(word)+5
while turns > 0:         


    failed = 0             

    
    for char in word:      


        if char in guesses:    
            print (char,sep="")    
        else:   
            print ("_")
            failed += 1    
    if failed == 0:        
        print ("You won")  
        break              
    print()
    guess = input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
 
        print("Wrong")    
        print ("You have" + str({turns})+ 'more guesses') 
 
        if turns == 0:
            print ("You Loose")  

