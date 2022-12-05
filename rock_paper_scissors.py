import random

print("Welcome to rock/paper/scissors game. Play as long as you want and quit when done.")

user_wins = 0
compuer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit game: ").lower()
    if user_input == 'q':
        break

    if user_input not in choices:
       user_input = input("Type rock/paper/scissors or Q to quit game: ").lower()
         
    
    random_number = random.randint(0,2) 
    # rock is 0, paper is 1, scissors is 2
    computer_input = choices[random_number]
    print("Computer chose", computer_input)
    if user_input== "scissors" and computer_input == "paper":
        print("You win")
        user_wins +=1
    elif user_input== "paper" and computer_input == "rock":
        print("You win")
        user_wins +=1
    elif user_input== "rock" and computer_input == "scissors":
        print("You win")
        user_wins +=1
    elif user_input== computer_input:
        print("You tie!")    
    else:
       print("You loose")  
       compuer_wins += 1 
         
print("You win", user_wins, "times.")
print("Computer wins", compuer_wins, "times." )
print("Bye")
        
