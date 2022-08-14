import math
import curses
from time import sleep
from timeit import timeit
from random import randint
from curses import wrapper

class MaxHeapView:

	def __init__(self):
		self.heap = []
		self.count = 0
		self.animate = False
		self.action = None

	def __repr__(self):
		return f"{self.heap}"

	def height(self):
		return math.ceil(math.log(self.count + 1, 2))

	def extract_max(self):
		return self.heap[0]	

	def heapify_up(self):
		wrapper(self.tree_view)
		i = self.count//2 - 1
		while i >= 0:
			_max = self.heap[i]
			left = 2 * i + 1
			right = left + 1
			is_swapped = False
			if left < self.count and self.heap[left] > _max:
				_max = self.heap[left]
				self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
				is_swapped = True
			if right < self.count and self.heap[right] > _max:
				_max = self.heap[right]
				self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
				is_swapped=True
			if not is_swapped:
				break
			wrapper(self.tree_view)
			if i%2: i = (i+1)//2 - 1
			else: i = i//2 - 1

	def heapify_down(self, i=0):
		wrapper(self.tree_view)
		if i > self.count:
			return
		left = 2 * i + 1
		right = left + 1
		if left < self.count and self.heap[i] < self.heap[left]:
			self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
			self.heapify_down(left)
		if right < self.count and self.heap[i] < self.heap[right]:
			self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
			self.heapify_down(right)

	def __insert(self, val):
		self.heap.append(val)
		self.count += 1
		self.action = f'ADD {val}'
		self.heapify_up()
		self.action = None

	def insert_all(self, arr):
		self.animate = True
		for v in arr:
			self.__insert(v)
		self.animate = False
		wrapper(self.tree_view)

	def __delete(self, val):
		index = self.heap.index(val)
		self.heap[-1], self.heap[index] = self.heap[index], self.heap[-1]
		val = self.heap.pop()
		self.count -= 1
		self.action = f'DELETE {val}'
		self.heapify_down(index)
		self.action = None

	def delete_all(self, arr):
		self.animate = True
		for v in arr:
			if v in self.heap:
				self.__delete(v)
			else:
				continue
		self.animate = False
		wrapper(self.tree_view)

	def get_arrows(self, l):
		syms = ['\\'] * l
		for i in range(1,l,2):
			syms[i] = '/'
		return syms

	def tree_view(self, stdscr):
		# clear the console
		stdscr.clear()

		# create view		
		arr = list(map(str, self.heap))
		rem = int((2 ** self.height() - 1) - self.count)
		arr.extend([' '] * rem)
		start = (self.count + rem ) // 2
		end = self.count + rem
		i, j = 0, 2
		while start > 0:
			res = ' ' * (2**i) + (' ' * (2**(i+1) - 1)).join(arr[start:end])
			stdscr.addstr(j, 0, res)
			syms = ' ' * (2**i) + (' ' * (2**(i+1) - 1)).join(self.get_arrows(end-start)) 
			stdscr.addstr(j+1, 0, syms)
			end = start
			start = start//2 
			i += 1
			j += 2
		res = ''
		if self.heap != []: 
			res = ' ' * (2 ** i) + str(self.heap[0])
		stdscr.addstr(j, 0, res)
		
		# refresh 
		if not self.animate:
			stdscr.addstr(j+5, 0, '(Press any other key (except 0-9) to exit)')
			stdscr.addstr(j+6, 0, 'Enter a value to delete: ')
			curses.echo()
			ch = stdscr.getch()
			if ch >= ord('0') and ch <= ord('9'):
				self.delete_all([ch - ord('0')])
		else:
			if self.action: stdscr.addstr(j+5, 0, f'{self.action}')
			else: stdscr.addstr(j+5, 0, f'{self.action} {self.heap}')
			stdscr.refresh()		
			sleep(0.5)



def main():
	my_heap = MaxHeapView()
	arr = []
	for _ in range(63):
		arr.append(randint(1,9))
	my_heap.insert_all(arr)
	# my_heap.delete_all(arr[:25])



if __name__ == "__main__":
	main()
