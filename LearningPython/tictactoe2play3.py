#printSquare(xlist,olist,blanklist) 

def printRow():
	row = '+'
	for i in range(3):
		row = row+' ----- +'
	print row

def printColumn():
	row = '|'
	for i in range(3):
		row = row+'       |'
	print row

def printColumnWithCharacter(spaces_by_row): # can change so each row has diff character but not column
	row = '|'
	for i in range(3):
		row = row+'   '+spaces_by_row[i]+'   |'
	print row
		
def printSquare(all_spaces): #args will be characters_row1,characters_row2,characters_row3
		printRow()

		for i in range(3):
			printColumn()
			printColumnWithCharacter(all_spaces[i]) 
			printColumn()
			printRow()


def checkForWinner(all_spaces): #won't register ties
	global winner 
	winner = ' '

	if all_spaces[0][0] == all_spaces[0][1] == all_spaces[0][2]:
		winner = all_spaces[0][0]
	elif all_spaces[1][0] == all_spaces[1][1] == all_spaces[1][2]:
		winner = all_spaces[1][0]
	elif all_spaces[2][0] == all_spaces[2][1] == all_spaces[2][2]:
		winner =all_spaces[2][0]
	elif all_spaces[0][0] == all_spaces[1][0] == all_spaces[2][0]:
		winner =all_spaces[0][0]
	elif all_spaces[0][1] == all_spaces[1][1] == all_spaces[2][1]:
		winner =all_spaces[0][1]
	elif all_spaces[0][2] == all_spaces[1][2] == all_spaces[2][2]:
		winner =all_spaces[0][2]
	elif all_spaces[0][0] == all_spaces[1][1] == all_spaces[2][2]:
		winner =all_spaces[0][0]
	elif all_spaces[0][2] == all_spaces[1][1] == all_spaces[2][0]:
		winner =all_spaces[0][2]

	return winner

def turn(character_value, all_spaces):
	global turn_row, turn_column

	valid_entry = 0


	while valid_entry == 0:	
		print ('Please enter the ROW number (between 1-3) where youd like to drop your '+ character_value +':')
		turn_row = int(raw_input()) - 1
		print ('Please enter the COLUMN number (between 1-3):')
		turn_column = int(raw_input()) - 1

		if turn_row >= 3 or turn_row < 0:
			print 'ERROR: The ROW NUMBER you have entered is outside the given range. It must be a whole number between 1 and 3.'

		elif turn_column >= 3 or turn_column < 0:
			print 'ERROR: The COLUMN NUMBER you have entered is outside the given range. It must be a whole number between 1 and 3.'

		elif all_spaces[turn_row][turn_column] == ' ':
			all_spaces[turn_row][turn_column] = character_value
			valid_entry = 1

		else:
			print 'ERROR: A value already exists in row: '+str(turn_row)+', column: '+str(turn_column)+'.  Please enter a new move.'

def playGame():
	global turn_tracker, all_spaces, character_value
	game_active = True
	turn_tracker = 1
	all_spaces= [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	character_value = 'O'

	while game_active == True:

		printSquare(all_spaces)

		if turn_tracker%2 == 0:
			character_value = 'X'
		else:
			character_value = 'O'

		turn(character_value, all_spaces)

		winner = checkForWinner(all_spaces)
		if winner!=' ':
			printSquare(all_spaces)
			print 'The winner is player '+winner+'!'

			game_active = False
		elif turn_tracker >= 9:
			game_active = False
			printSquare(all_spaces)
			print 'Game Over: Draw!'


		turn_tracker = turn_tracker+1
		
playGame()
