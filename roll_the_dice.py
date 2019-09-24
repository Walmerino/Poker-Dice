import random

def convert(x):				#The convert function returns a clean string without 
    d = []				#the list brackets, comas and quotes
    for i in x:
        char = str(i)
        d.append(char)
        e = ' - '. join(d)
    return e

play = input('Let\'s play? ')

all_hands = []				#Stores all hands played
dice = ['A', 'K', 'Q', 'J', '10', '9']	#The actual die figures or sides

while play == 'y':
    
    hand = []				#The hand of five figures or sides of the dice
    roll = 0				#Counts the number of figures that represents the 5 dice

    while roll < 5:
       
        side = random.choice(dice)	#Chooses a random figure
        hand.append(side)		#Appends each handom generated side
        hand.sort()			#Sorts the sides together if they are equal
        roll += 1
    print(convert(hand))		
    all_hands.append(hand)
    play = input('Another hand? ')
    
else:
    
    games = 0
    for i in all_hands:
        games += 1
        print('Hand',games,'was:', convert(i))	#Outputs all played hands

