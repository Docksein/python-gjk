pole = [6, 1, 2, 3, 8, 20, 50, 6, 4, -3, 5]

def bubble_sort(neco):
	if len(neco) < 2:
		print(neco)
	else:
		index1 = 0
		index2 = 1
		final_list = neco
		short_mem = []
		
		while index2 <= len(neco)-1:
			if final_list[index1] <= final_list[index2]:
				index1 += 1
				index2 += 1
			else:
				short_mem.append(final_list[index2])
				short_mem.append(final_list[index1])
				final_list[index1] = short_mem[0]
				final_list[index2] = short_mem[1]
				short_mem = []
				index1 = 0
				index2 = 1
		else:
			print(final_list)

if __name__ = "__main__":
	bubble_sort(pole)
