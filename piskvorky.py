game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def board():
	print(f"{game[0][0]}|{game[0][1]}|{game[0][2]}")
	print("-+-+-")
	print(f"{game[1][0]}|{game[1][1]}|{game[1][2]}")	
	print("-+-+-")
	print(f"{game[2][0]}|{game[2][1]}|{game[2][2]}")

def player_input():
	global x
	global y
	x = input("select x axis: ")
	y =input("select y axis: ")
	independent_variable = 0
	while independent_variable < 1:
		try:
			x = int(x) - 1
			y = int(y)- 1
			if	int(x) < 0 or int(x) > 3 or int(y) < 0 or int(y) > 3: 
				print("Not in range")
				x = input("select x axis: ")
				y =input("select y axis: ")
			else:
				independent_variable += 1
		except ValueError as errv:
			print(errv)
			x = input("select x axis: ")
			y =input("select y axis: ")
		except TypeError as errt:
			print(errt)
			x = input("select x axis: ")
			y =input("select y axis: ")
		
def win_check():
	for i in range(3):
		if game[i][0] == game[i][1] == game[i][2] == x_or_o or game[0][i] == game[1][i] == game[2][i] == x_or_o: 
			board()
			print(f"Congratulations, {x_or_o} won!")
			return True
		elif  game[0][0] == game[1][1] == game[2][2] == x_or_o or  game[0][2] == game[1][1] == game[2][0] == x_or_o:   
			board()
			print(f"Congratulations, {x_or_o} won!")
			return True
		else:
			return False
		
def board_change():
	while game[y][x]=="x" or game[y][x]=="y":
		print("That spot has already been taken")
		player_input()
	else:
		game[y][x] = x_or_o 

def main():
	for i in range(9):
		global x_or_o
		x_or_o = " "
		if i%2 == 0:
			x_or_o = "x"
		else:
			x_or_o = "o"
		board()
		player_input()
		board_change()
		if win_check():
			break

main()
