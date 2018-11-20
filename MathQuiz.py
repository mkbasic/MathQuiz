import random

play_again = "y"
operator = ""
questions = 0
correct = 0
total_correct = 0
total_questions = 0

def addition():
    global correct
    
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    
    print (num1, "+", num2)
    while True: #error handling of invalid responses
        try:
            answer = int(input())
            break
        except ValueError:
            print ("Please enter a valid answer...")
    
    if answer == num1 + num2:
        print ("Correct!")
        correct = correct + 1
    else:
        print ("Sorry!")

def subtraction():
    global correct
    
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)

    if num1 > num2:
        print (num1, "-", num2)
        while True: #error handling of invalid responses
            try:
                answer = int(input())
                break
            except ValueError:
                print ("Please enter a valid answer...")
        
        if answer == num1 - num2:
            print ("Correct!")
            correct =  correct + 1
        else:
            print ("Sorry!")
            
    else:
        print (num2, "-", num1)
        while True: #error handling of invalid responses
            try:
                answer = int(input())
                break
            except ValueError:
                print ("Please enter a valid answer...")
        
        if answer == num2 - num1:
            print ("Correct!")
            correct = correct + 1
        else:
            print ("Sorry!")

def multiplication():
    global correct
    
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)

    print (num1, "*", num2)
    while True: #error handling of invalid responses
        try:
            answer = int(input())
            break
        except ValueError:
            print ("Please enter a valid answer...")

    if answer == num1 * num2:
        print ("Correct!")
        correct = correct + 1
    else:
            print ("Sorry!")
    
def division():
    global correct

    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
	
    while num1 % num2 != 0 or num1 == num2 or num2 == 1:
	    num1 = random.randint(1,100)
	    num2 = random.randint(1,100)

    if num1 > num2:
        print (num1, "/", num2)
        while True: #error handling of invalid responses
            try:
                answer = int(input())
                break
            except ValueError:
                print ("Please enter a valid answer...")
        
        if answer == num1 / num2:
            print ("Correct!")
            correct = correct + 1
        else:
            print ("Sorry!")

print ("Welcome to Math Quiz!")#opening title

while play_again == "y":
    print ("Select Addition(A), Subtraction(S), Multiplication(M), or Division(D)")
    operator = input().lower()
    print ("")#skip line after user's choice
    
    while operator != "a" and operator != "s" and operator != "m" and operator != "d":
        print ("Please enter a valid option.")
        print ("Select Addition(A), Subtraction(S), Multiplication(M), or Division(D)")
        operator = input().lower()
        print ("")#skip line after user's choice
    
    while questions < 5:#limits the number of questions per round
        if operator == "a":
            addition()
            print ("")
            questions = questions + 1
            
        elif operator == "s":
            subtraction()
            print ("")
            questions = questions + 1
            
        elif operator == "m":
            multiplication()
            print ("")
            questions = questions + 1
            
        elif operator == "d":
            division()
            print ("")
            questions = questions + 1
            
    print ("You got", correct, "out of 10!")
    
    total_correct = total_correct + correct
    total_questions = total_questions + questions
    
    print ("Total:", total_correct, "out of", total_questions)
    
    questions = 0
    correct = 0
    
    print ("Would you like to play again? N for No, Y for Yes: ")
    play_again = input().lower()
    
print ("Thank you for playing!")
input()
