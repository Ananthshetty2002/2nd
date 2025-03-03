import random
rock="hard"
paper="light"
scissor="cutting"
game=[rock,paper,scissor]
users_choice=int(input("enter rock has 0 paper has 1 and scissor has 2:"))
if users_choice>=3 or users_choice<0:
        print("invalid number,you lose")
else:
        print(game[users_choice]) 
comp_choice=random.randint(0,2)
print("computers choice")
print(game[comp_choice])
if(users_choice==comp_choice):
        print("draw")
elif(comp_choice>users_choice):
        print("you lose")
elif(users_choice>comp_choice):
        print("you win")
elif(users_choice==0 and comp_choice==2):
        print("you win")
elif(comp_choice==0 and users_choice==2):
        print("you lose")

        
        
     






