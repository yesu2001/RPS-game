from random import *
import string
human_point = 0
computer_point = 0
RPS = ["rock", "scissor", "paper"]
print("welcome to the  RPS game (ROck Paper Scissor) ")
print()
print("****_______     Lets start     ______******")
print()
choice_robot = RPS[randint(0,2)]
name=(input("Enter your Name : ").upper())

print()
turn=int(input("How many times do you want to play :  "))
print()
for i in range(turn):
	choice_human = input("Enter your choice (Rock or Paper or Scissor) : ")
	print("Computer has chosen : {}".format(choice_robot))
	if(choice_human==choice_robot):
		print("Both chose same")
		print("Its a tie")
		print("")
	elif(choice_human=="rock" or choice_robot=="paper"):
		print("{} chooses :  {}".format(name,choice_human))
		print("")
		print("rock is covered by paper")
		print("computer gains a point")
		computer_point+=1
		print("")
	elif(choice_human=="rock" or choice_robot=="scissor"):
		print("human chooses :  {}".format(name,choice_human))
		print("")
		print("rock crushes scissors")
		print("{}  gains a point".format(name))
		human_point+=1
		print("")        
	elif(choice_human=="paper" and choice_robot=="rock"):
		print("human chooses :  {}".format(name,choice_human))
		print("")
		print("paper covers the rock")
		print("{}  gains a point".format(name))
		human_point+=1
		print("")        
	elif(choice_human=="paper" and choice_robot=="scissor"):
		print("human chooses :  {}".format(name,choice_human))
		print("")
		print("paper is cut by scissors")
		print("computer gains a point")
		computer_point+=1
		print("")
	elif(choice_human=="scissor" and choice_robot=="rock"):
		print("human chooses :  {}".format(name,choice_human))
		print("")
		print("rock crushes scissor ")
		print("computer gains a point")
		computer_point+=1
		print("")
	elif(choice_human=="scissor" and choice_robot=="paper"):
		print("human chooses :  {}".format(name,choice_human))
		print("")    
		print("scissor cuts the paper")
		print("{}  gains a point".format(name))
		human_point+=1        
		print("")
	else:
		print("enter a correct choice")
		print("")
	i+=1	

print("")
print("{} has scored,  points : {}".format(name,human_point))    
print("computer has scored,  points : {}".format(computer_point))   
print("")
if human_point > computer_point:
	print("{} WINS !!! ".format(name))
else:
	print("COMPUTER WINS !!!")	


	
