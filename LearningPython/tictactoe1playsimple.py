from random import randint 


def printHorizontalLine():
	row = '+'
	for i in range(3):
		row = row+' ----- +'
	print row

def printVerticalLine():
	row = '|'
	for i in range(3):
		row = row+'       |'
	print row

def printVerticalLineWithCharacter(spaces_by_row): # can change so each row has diff character but not column
	row = '|'
	for i in range(3):
		row = row+'   '+spaces_by_row[i]+'   |'
	print row
		
def printSquare(all_spaces): #args will be characters_row1,characters_row2,characters_row3
		printHorizontalLine()

		for i in range(3):
			printVerticalLine()
			printVerticalLineWithCharacter(all_spaces[i]) 
			printVerticalLine()
			printHorizontalLine()


def checkForWinner(all_spaces): #won't register ties

	#win if 3 spaces with equal row value are equal,  
	#if 3 spaces where each value (1-3) is used once as row and once in column

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

def checkWinningCombos(all_spaces):
	winning_combos = list()

	#assign each place on the tic tac toe board a value of 'O', 'X' or 'r,c'
	one_one = all_spaces[0][0] if all_spaces[0][0] != ' ' else '0,0'
	one_two = all_spaces[0][1] if all_spaces[0][1] != ' ' else '0,1'
	one_three = all_spaces[0][2] if all_spaces[0][2] != ' ' else '0,2'
	two_one = all_spaces[1][0] if all_spaces[1][0] != ' ' else '1,0'
	two_two = all_spaces[1][1] if all_spaces[1][1] != ' ' else '1,1'
	two_three = all_spaces[1][2] if all_spaces[1][2] != ' ' else '1,2'
	three_one = all_spaces[2][0] if all_spaces[2][0] != ' ' else '2,0'
	three_two = all_spaces[2][1] if all_spaces[2][1] != ' ' else '2,1'
	three_three = all_spaces[2][2] if all_spaces[2][2] != ' ' else '2,2'

	winning_combos.append([one_one, one_two, one_three])
	winning_combos.append([two_one, two_two, two_three])
	winning_combos.append([three_one, three_two, three_three])
	winning_combos.append([one_one, two_one, three_one])
	winning_combos.append([one_two, two_two, three_two])
	winning_combos.append([one_three, two_three, three_three])
	winning_combos.append([one_one, two_two, three_three])
	winning_combos.append([three_one, two_two,one_three])

	return winning_combos


def checkFor2(all_spaces, check_character):
	play_space = list()
	winning_combos = list()
	play_space_str = list()
	winning_combos = checkWinningCombos(all_spaces)

	for winning_combo in winning_combos:
		character_count = winning_combo.count(check_character)
		if character_count >= 2:
			for space in winning_combo:
				if space != 'X' and space != 'O':
					play_space_str = space.split(',')

	if play_space_str:
		for index_value in play_space_str:
			play_space.append(int(index_value))

	return play_space 


def playRandomSpace(all_spaces):

	all_open_spaces = list()
	play_space = list()
	play_space_str = list()

	for row in all_spaces:
		for space in row:
			if space == ' ':
				all_open_spaces.append(str(all_spaces.index(row))+','+str(row.index(space)))

	random_open_space = randint(0,len(all_open_spaces) - 1)

	play_space_str = all_open_spaces[random_open_space].split(',')

	if play_space_str:
		for index_value in play_space_str:
			play_space.append(int(index_value))

	return play_space 

def turn_AI(all_spaces, character_value):
	if character_value == 'X':
		opponent_value = '0'
	else:
		opponent_value = 'X'
	play_offence = checkFor2(all_spaces, character_value)
	if not not play_offence: 
		all_spaces[play_offence[0]][play_offence[1]] = character_value
	else: 
		play_defence = checkFor2(all_spaces, opponent_value)
		if not not play_defence: 
			all_spaces[play_defence[0]][play_defence[1]] = character_value
		else: 
			play_random = playRandomSpace(all_spaces)
			all_spaces[play_random[0]][play_random[1]] = character_value


def playGame():

	print 'Please enter "1" to play a single player game, or "2" to play a two player game:'
	playercount = int(raw_input())

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

		if (turn_tracker%2 != 0 or playercount != 1):
			turn(character_value, all_spaces)
		else:
			print 'AI turn'
			turn_AI(all_spaces, character_value)

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


