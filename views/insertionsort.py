import math
import curses
from time import sleep
from timeit import timeit
from random import randint
from curses import wrapper



class InsertionSortView(object):
	
	def __init__(self, arr):
		self.title = 'INSERTION SORT'
		self.arr = arr
		self.animation = False
		self.info = None
		self.highlighted_index_1 = None
		self.highlighted_index_2 = None
		self.highlighted_xpos_1 = None
		self.highlighted_xpos_2 = None


	def sort(self):
		self.animation = True
		self.highlighted_index_1 = 0
		self.highlighted_xpos_1 = 0
		wrapper(self.view)
		for i in range(1,len(self.arr)):
			key = self.arr[i]
			self.highlighted_index_1 = i
			self.highlighted_xpos_1 = self.calc_x_pos(i)
			wrapper(self.view)
			k = i
			for j in range(i-1,-1,-1):

				self.info = f'COMPARE {self.arr[j]} and {self.arr[k]}'
				self.highlighted_index_1 = j
				self.highlighted_xpos_1 = self.calc_x_pos(j)
				self.highlighted_index_2 = k
				self.highlighted_xpos_2 = self.calc_x_pos(k)
				wrapper(self.view)
				if self.arr[j] > key:
					self.arr[j], self.arr[k] = self.arr[k], self.arr[j]
					self.info = f'SWAP {self.arr[j]} and {self.arr[k]}'
					wrapper(self.view)
				else:
					break
				k -= 1
		self.highlighted_index_1 = None
		self.highlighted_index_2 = None
		self.info = None
		self.animation = False
		wrapper(self.view)


	# for generating views
	def calc_x_pos(self, i):
		x_pos = 0
		for j in range(0, i):
			x_pos += (len(str(self.arr[j])) + 3)
		return x_pos


	def view(self, stdscr):
		stdscr.clear()
		values = list(map(str, self.arr))
		padx, pady = 10, 5
		stdscr.addstr(3,padx, self.title)
		stdscr.addstr(pady, padx, '   '.join(values))
		if self.highlighted_index_1 is not None:
			stdscr.addstr(pady, padx + self.highlighted_xpos_1, str(self.arr[self.highlighted_index_1]),curses.A_STANDOUT)
		if self.highlighted_index_2 is not None:
			stdscr.addstr(pady, padx + self.highlighted_xpos_2, str(self.arr[self.highlighted_index_2]),curses.A_STANDOUT)

		if self.info:
			stdscr.addstr(pady + 4, padx, self.info)

		if not self.animation:
			stdscr.addstr(pady + 7, 0, '(Press Esc to exit)')
			stdscr.refresh()
			stdscr.getkey()
		else:
			stdscr.refresh()
			sleep(0.7)




def main():
	arr = []
	for _ in range(15):
		arr.append(randint(10,100))
	insv = InsertionSortView(arr)
	insv.sort()


if __name__ == '__main__':
	main()

