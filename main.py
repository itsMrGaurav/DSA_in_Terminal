import curses
from curses import wrapper
from random import randint
from views.maxheap import MaxHeapView
from views.linkedlists import SinglyLinkedListView
from views.insertionsort import InsertionSortView
from views.binarysearch import BinarySearchView


def check_terminal_size(h, w):
	if w < 101 and h < 26:
		print('Please maximize your terminal and try again !!')
		exit(0)
	return True


def max_heap(w):
	options = ['1. Enter array manually (n<128, 0 <= val <= 9, space-sep)', '2. Get Random Values upto n(<128)', '3. Return']
	print(' ' * (w//2) + 'MAX HEAP\n\n')
	print(' ' * (w//4) + 'ENTER: ')
	for opt in options:
		print(' ' * (w//4) + opt)
	while True:
		ch = input('\nChoice (Enter any other key to exit): ')
		if ch == '1':
			try:
				values = list(map(int, input("Enter Values: ").split(' ')))
				if len(values) > 128:
					values = values[:128]
				values = list(filter(lambda x: x > -1 and x < 10, values))
			except Exception as e:
				print('Incorrect input values.')
				return
			else:
				break
		elif ch == '2':
			try:
				n = abs(int(input("Enter size: ")))
				n = min(127, n)
				values = [randint(0,9) for _ in range(n)]
			except Exception as e:
				print('Incorrect input value.')
				return
			else:
				break
		elif ch == '3':
			return
		else:
			exit(0)
	mxv = MaxHeapView()
	mxv.insert_all(values)


def linked_lists(w):
	options = ['1. Enter array manually (n<16, 10 <= val <= 99, space-sep)', '2. Get Random Values upto n(<15)', '3. Return']
	print(' ' * (w//2) + 'LINKED LISTS\n\n')
	print(' ' * (w//4) + 'ENTER: ')
	for opt in options:
		print(' ' * (w//4) + opt)
	while True:
		ch = input('\nChoice (Enter any other key to exit): ')
		if ch == '1':
			try:
				values = list(map(int, input("Enter Values: ").split(' ')))
				if len(values) > 16:
					values = values[:16]
				values = list(filter(lambda x: x > 9 and x < 99, values))
			except Exception as e:
				print('Incorrect input values.')
				return
			else:
				break
		elif ch == '2':
			try:
				n = abs(int(input("Enter size: ")))
				n = min(16, n)
				values = [randint(10,99) for _ in range(n)]
			except Exception as e:
				print('Incorrect input value.')
				return
			else:
				break
		elif ch == '3':
			return
		else:
			exit(0)
	sll = SinglyLinkedListView()
	sll.insert_all(values)


def insertion_sort(w):
	options = ['1. Enter array manually (n<16, 10 <= val <= 99, space-sep)', '2. Get Random Values upto n(<16)','3. Generate best case', '4. Generate worst case', '5. Return']
	print(' ' * (w//2) + 'INSERTION SORT\n\n')
	print(' ' * (w//4) + 'ENTER: ')
	for opt in options:
		print(' ' * (w//4) + opt)
	while True:
		ch = input('\nChoice (Enter any other key to exit): ')
		if ch == '1':
			try:
				values = list(map(int, input("Enter Values: ").split(' ')))
				if len(values) > 16:
					values = values[:16]
				values = list(filter(lambda x: x > 9 and x < 99, values))
			except Exception as e:
				print('Incorrect input values.')
				return
			else:
				break
		elif ch == '2':
			try:
				n = abs(int(input("Enter size: ")))
				n = min(16, n)
				values = [randint(10,99) for _ in range(n)]
			except Exception as e:
				print('Incorrect input value.')
				return
			else:
				break
		elif ch == '3':
			values = [i for i in range(10, 26)]
			break
		elif ch == '4':
			values = [i for i in range(25, 9, -1)]
			break
		elif ch == '5':
			return
		else:
			exit(0)
	insv = InsertionSortView(values)
	insv.sort()


def binary_search(w):
	options = ['1. Enter array manually (n<16, 10 <= val <= 99, space-sep)', '2. Get Random Values upto n(<15)', '3. Return']
	print(' ' * (w//2) + 'BINARY SEARCH\n\n')
	print(' ' * (w//4) + 'ENTER: ')
	for opt in options:
		print(' ' * (w//4) + opt)
	while True:
		ch = input('\nChoice (Enter any other key to exit): ')
		if ch == '1':
			try:
				values = list(map(int, input("Enter Values: ").split(' ')))
				if len(values) > 16:
					values = values[:16]
				values = list(filter(lambda x: x > 9 and x < 99, values))
				values.sort()
			except Exception as e:
				print('Incorrect input values.')
				return
			else:
				break
		elif ch == '2':
			try:
				n = abs(int(input("Enter size: ")))
				n = min(16, n)
				values = [randint(10,99) for _ in range(n)]
			except Exception as e:
				print('Incorrect input value.')
				return
			else:
				break
		elif ch == '3':
			return
		else:
			exit(0)
	bsv = BinarySearchView(values)
	try:
		val = int(input('Enter Value to search for: '))
		if val < 10 and val > 99:
			raise Exception
	except Exception as e:
		print('Wrong Input.')
	else:				
		bsv.search_for(val)


def get_terminal_hw(stdscr):
	return stdscr.getmaxyx()


def main():
	programs = ['1. MAX HEAP', '2. LINKED LISTS', '3. INSERTION SORT', '4. BINARY SEARCH']
	h, w = list(map(int, wrapper(get_terminal_hw)))
	check_terminal_size(h, w)
	print(' ' * (w//2) + 'WELCOME\n\n')

	while True:
		print(' ' * (w//4) + 'ENTER: ')
		for item in programs:
			print(' ' * (w//4) + item)
		ch = input('\nChoice (Enter any other key to exit): ')
		if ch == '1':
			max_heap(w)
		elif ch == '2':
			linked_lists(w)
		elif ch == '3':
			insertion_sort(w)
		elif ch == '4':
			binary_search(w)
		else:
			print('Exit')
			break




if __name__ == '__main__':
	main()