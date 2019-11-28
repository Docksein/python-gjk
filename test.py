values = {
    0: " ",
    1: "x",
    2: "o"
}

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def print_board():
    for i in range(3):
        print("{}|{}|{}".format(values.get(board[i][0]), values.get(board[i][1]), values.get(board[i][2])))
        print("-+-+-")

pl_input1 = input(" ")
pl_input2 = input(" ")

if 3 > int(pl_input1) >= 0 and 3 > int(pl_input2) >= 0:
    print(values.get(board[int(pl_input1)][int(pl_input2)]))
    print_board()
else:
    print("invalid value")