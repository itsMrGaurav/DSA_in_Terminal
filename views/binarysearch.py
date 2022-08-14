import math
import curses
from time import sleep
from timeit import timeit
from random import randint
from curses import wrapper


class BinarySearchView(object):
	"""docstring for BinarySearchView"""
	def __init__(self, arr):
		super(BinarySearchView, self).__init__()
		self.title = 'BINARY SEARCH'
		self.arr = arr
		self.animation = False
		self.info = None
		self.info2 = None
		self.highlighted_index = None
		self.highlighted_xpos = None

	def BinarySearch(self, i,j,val):
		if j - i <= 1:
			if self.arr[i] == val:
				self.info = 'FOUND'
			else: self.info = 'NOT FOUND'
			return 
		mid = (i + j)//2
		self.highlighted_index = mid
		self.highlighted_xpos = self.calc_x_pos(mid)
		self.info = f'COMPARE WITH {self.arr[mid]}'
		wrapper(self.view)
		if self.arr[mid] == val:
			self.info = f'FOUND'
			wrapper(self.view)
		elif self.arr[mid] > val:
			self.info = f'LEFT'
			wrapper(self.view)
			self.BinarySearch(i, mid, val)
		else:
			self.info = f'RIGHT'
			wrapper(self.view)
			self.BinarySearch(mid, j, val)

		self.highlighted_index = None

	def search_for(self, val):
		self.animation = True
		self.info2 = f'LOOKING FOR {val}'
		self.BinarySearch(0, len(self.arr), val)
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
		if self.highlighted_index is not None:
			stdscr.addstr(pady, padx + self.highlighted_xpos, str(self.arr[self.highlighted_index]),curses.A_STANDOUT)

		if self.info:
			stdscr.addstr(pady + 4, padx, self.info)
		if self.info2:
			stdscr.addstr(pady + 5, padx, self.info2)

		if not self.animation:
			stdscr.addstr(pady+6, 0, '(Press any key (except 10-99) to exit)')
			stdscr.addstr(pady+7, 0, 'Enter a value to search:')
			curses.echo()
			val = stdscr.getstr(pady+7, 25, 2)
			try:
				val = int(val)
				if val < 10 and val > 99:
					raise Exception
			except Exception as e:
				stdscr.addstr(pady+6, 0, 'Wrong Input')
			else:				
				self.search_for(val)
		else:
			stdscr.refresh()		
			sleep(0.5)


def main():
	arr = []
	for _ in range(20):
		arr.append(randint(10,99))
	arr.sort()
	bs = BinarySearchView(arr)
	bs.search_for(23)

if __name__ == "__main__":
	main()