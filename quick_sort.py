
def seperate_and_sort(list0):
	if len(list0)==0:
		return []
	
	pivot = list0[0]
	part1 = []
	part2 = []
	for x in list0[1:]:
		if x<pivot:
			part1.append(x)
		else:
			part2.append(x)
	part1 = seperate_and_sort(part1)
	part2 = seperate_and_sort(part2)
							
	return part1 + [pivot,] + part2 


def quick_sort(list0):
	
	new_list = seperate_and_sort(list0)

	return new_list


def main():

	list0 = [0, 1, 19, 2, 37, 5, 8, 7, 16, 9, 1, 2, 5, 4, 100, 3]

	new_list = quick_sort(list0)

	print(new_list)

if __name__ == '__main__':
	main()
	print("\nDone!\n")