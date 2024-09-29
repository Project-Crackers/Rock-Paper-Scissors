import random
options = ['rock' , 'paper' , 'scissors']

while True :
    user_choice = input("\n Enter Your Choice (Rock , Paper or Scissors) : ")
    comp_choice = random.choice(options)


    print("\n Your choice : ", user_choice)
    
    print(" Computer choice :" , comp_choice)

    if user_choice == comp_choice :
        print("\n <-------- It's a Tie --------->")
    elif user_choice == "rock" and comp_choice == "scissors" :
        print("\n <-------- You Win ---------->")
    elif user_choice == "paper" and comp_choice == "rock" :
        print("\n <-------- You Win ---------->")
    elif user_choice == "scissors" and comp_choice == "paper" :
        print("\n <-------- You Win ---------->")
    else :
        print("\n <--------- Computer Wins --------->")

        
    nxt_game = input("\n Do You Want To Continue The Next Game (yes or no) : ").lower()
    

    if nxt_game == "no" :
      break
