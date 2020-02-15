game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def board():
	print(f"{game[0][0]}|{game[0][1]}|{game[0][2]}")
	print("-+-+-")
	print(f"{game[1][0]}|{game[1][1]}|{game[1][2]}")	
	print("-+-+-")
	print(f"{game[2][0]}|{game[2][1]}|{game[2][2]}")

def player_input():
	x = input("select x axis: ")
	y =input("select y axis: ")
	while 4 < int(x) > 0 or  4 < int(y) > 0 :
		print("not in range")
		x = input("select x axis: ")
		y =input("select y axis: ")
	else:
		try:
			x = int(x) - 1
			y = int(y)- 1
		except ValueError as errv:
			print(errv)
		except TypeError as errt:
			print(errt)

def main():
	board()
	player_input()

main()
