#!/usr/local/bin/python3.2
import math
#Welcome to Lab 4 by Daniel Safford
#Choose your own adventure story!!

print("Welcome to The Black Void!!!")
name = input("What is your name space traveler?: ")
print("Welcome to The Black Void traveler", name, "!!! Enjoy")
print("CTRL- C to exit at anytime")

dest = "return"
while dest == "return":
	print("Enter the red or blue ship?")
	ship = input("Ship?: ")

	#Choice block for blue ship
	if ship == "blue":
		print("You are going to planet Roberson!")
		dest = input("proceed or return?: ") #dest = destination
		if dest == "proceed":
			print("You are now on planet Roberson. Talk to the alians, yes or no?")
			talk = input("yes or no: ") #need no options
			if talk == "yes":
				print("You are needed for a special quest", name)
				print("Accept the quest? What say you?!?!")
				quest = input("Join quest, yes or no?: ")
				if quest == "yes": 
					print("Choose your weapon axe or bow") 
					weapon = input("axe or bow?: ")
					if weapon == "axe":
						print(name, "you must use your axe to fight the Daleks!")
						print("Make peace or give them pie")
						dalek = input("peace or pie: ") 
						if dalek == "peace":
							print("WE WILL EXTERMINATE YOU!!!!!")
							print("The Daleks have killed you!")
							dest = input("Type return to play again!: ")
						elif dalek == "pie":
							print("The Daleks have accepted your gift of pie!")
							print("you are now free from The Black void!")
							dest = input("You Win! Type return to play again!: ")
					elif weapon == "bow":
						print("We need you to go seek the space jackalope!")
						print("Shall you seek the space jackalope traveler", name, "?")
						seek = input("Seek, yes or no?: ")
						if seek == "yes":
							print("This was a trap! you have entered a time rift!")
							print("You have been zapped to the red ship")
							ship = input("Go to the red ship, type red: ")	
						elif seek == "no":
							print("The jackalope has found you instead!!")
							print("You are now friends and have defeated the alians!!")
							dest = input("You Win! Type return to play again!: ")
				elif quest == "no":
					print("You are now a slave traveler", name) #add more here
					print("You now have to spend the rest of your life careing for their pet frogs!!")
					frog = input("Care for the frogs? yes or no?: ") #needs a no option
					if frog == "yes":
						print("Are you an idiot? Why would you condem your life to careing for frogs?")
						print("The president has sent a ship to save you!")
						save = input("Be saved? yes or no?: ")
						if save == "yes":
							print("You have been saved by the president!!")
							print("Although, you know too much!! The FBI killed you!")
							dest = input("Type return to play again!: ")
						elif save == "no":
							print(name, "You find a spaceship that can bring you back to Earth")
							print("Steal the Super Awesome Ship 7500!! Or no?")
							awesome = input("Steal? yes or no?: ")
							if awesome == "yes":
								print("free at last!! free at last!!")
								print("Hold on, you're not even a pilot!!")
								print("You didn't evenget off the groud. You blew up")
								dest = input("Type return to play again!: ")
							elif awesome == "no":
								print("The heck? If you really want to stay then make it so!")
								print("You lived to the age of 107 careing for the frogs you were forever worsiped!")
								dest = input("You kind of won! Type return to play again!: ")
					elif frog == "no":
						print("I am so so sorry traveler", name, "You will now be burned alive")
						print("The alians don't take no for an answer, nor does the games creator!!")
						print("WORSIP THE CREATOR!!! WORSHIP HIM!!")
						print("Welcome to the time rift!!")
						ship = input("Enter red to continue through the rift!: ")	
																				
		else: 
			print("You are now going back", name)
			dest = input("Type return to play again!: ")
			
	#Choice block for red ship
	if ship == "red":
		print("You are going to planet Unix!")
		dest = input("proceed or return?: ")
		if dest == "proceed":
			print("You are now on planet Unix go left or right?")
			go = input("Turn left or right?: ")
			if go == "left": #left option
				print(name, "The Unixmen want you to become their king, yes or no?")
				king = input("Become king? yes or no?: ")
				if king == "yes": #yes option
					print("The Unixmen now worship you king", name)
					print("Continue to be king? Run away? Eat the cake?")
					plan = input("king, run, or cake?: ") 
					if plan == "king": #king option
						print("The Unixmen will worship you until the end of time!!!")
						print("The universe collapsed due to the end of time")
						dest = input("Type return to play again!: ")
					elif plan == "run": #run option
						print("You have run for days upon days.")
						print("You have escaped the Unixmen and The Black Void!!")
						win = input("You win!!, ok or secret?: ")
						if win == "ok": #ok option
							print("The End traveler", name)
							dest = input("Type return to play again!: ")
						elif win == "secret": #secret option
							print("Daniel Safford wrote the code for this program in Python 3!!")
							print("What a nifty fact!!!")
							dest = input("Type return to play again!:")
					elif plan == "cake": #cake option
						print("The Unixmen have left you a yummy cake!")
						print("You use the cake to poison the Unixmen ane exit The Black Void")
						print("YOU ARE A WINNER!")
						dest = input("Type return to play again!: ")												
				elif king == "no": #no option
					print("The Unixmen have decided to eat you instead!!")
					eat = input("fight or hide?: ")
					if eat == "fight": #fight option
						print("Since you have decided to fight!!!!! Our army will hunt you down!!")
						print("The Unixmen army killed you!")
						dest = input("Type return to play again: ")
					elif eat == "hide": #hide option
						print("You fell into their trap!!!")
						print("You're burning alive!! SCREAM!!!")
						dest = input("Type return to play again!: ")
			elif go == "right": #This is a dead end to the red ship red option
				print("You fell into an endless pit of lava!!")
				dest = input("Type return to play again!: ")
		else:
			print("You are now going back", name)
			dest = input("Type return to play again!: ")
		

