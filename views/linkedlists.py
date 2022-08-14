import math
import curses
from time import sleep
from timeit import timeit
from random import randint
from curses import wrapper


class Node:
	def  __init__(self, val, next=None, prev=None):
		self.val = val
		self.next = next
		self.prev = prev


class SinglyLinkedListView(object):
	"""docstring for SinglyLinkedListView"""
	def __init__(self):
		super(SinglyLinkedListView, self).__init__()
		self.root = None
		self.info = None
		self.arr = []
		self.highlighted_xpos = None
		self.highlighted_index = None
		self.animation = False


	def insert(self, val):
		
		if not self.root:
			self.root = Node(val)
			self.arr.append(val)
			return

		self.highlighted_xpos = 0
		self.highlighted_index = 0
		self.info = f'IN {val}'
		p = self.root
		while p.next:
			p = p.next
			self.highlighted_xpos = self.calc_x_pos(self.highlighted_index)
			wrapper(self.view)
			self.highlighted_index += 1

		self.highlighted_xpos = self.calc_x_pos(self.highlighted_index)
		wrapper(self.view)
		p.next = Node(val)
		self.arr.append(val)
		self.highlighted_index = None
		self.info = None



	def insert_all(self,arr):
		self.animation = True
		for ele in arr:
			self.insert(ele)
		self.animation = False
		wrapper(self.view)


	def delete(self, val):

		if not self.root:
			return 

		self.highlighted_xpos = 0
		self.highlighted_index = 0
		self.info = f'IN {val}'
		p = self.root
		parent = None
		found = False
		self.info = f'Delete {val}..'
		while p:
			if p.val == val:
				found = True
				break
			self.highlighted_xpos = self.calc_x_pos(self.highlighted_index)
			wrapper(self.view)
			self.highlighted_index += 1
			parent = p
			p = p.next

		if found:
			if parent: parent.next = p.next
			else: 
				self.root = p.next
			self.info = 'FOUND'
			wrapper(self.view)
			self.arr.remove(val)
		else:
			self.info = f'{val} NOT FOUND!'

		self.highlighted_index = None
		wrapper(self.view)
		self.info = None


	def delete_all(self, arr):
		self.animation = True
		for ele in arr:
			self.delete(ele)
		self.animation = False
		wrapper(self.view)


	# for generating views
	def calc_x_pos(self, i):
		x_pos = 0
		for j in range(0, i):
			x_pos += (len(str(self.arr[j])) + 2)
		return x_pos


	def view(self, stdscr):
		stdscr.clear()

		values = list(map(str, self.arr))
		padx, pady = 10, 5
		stdscr.addstr(pady, padx, '->'.join(values))
		if self.highlighted_index is not None:
			stdscr.addstr(pady, padx + self.highlighted_xpos, str(self.arr[self.highlighted_index]),curses.A_STANDOUT)

		if self.info:
			stdscr.addstr(pady + 4, padx, self.info)

		if not self.animation:
			stdscr.addstr(pady+4, 0, '(Press any key (except 10-99) to exit)')
			stdscr.addstr(pady+5, 0, 'Enter a value to delete:')
			curses.echo()
			val = stdscr.getstr(pady+5, 25, 2)
			try:
				val = int(val)
				if val < 10 and val > 99:
					raise Exception
			except Exception as e:
				stdscr.addstr(pady+6, 0, 'Wrong Input')
			else:				
				self.delete_all([val])
		else:
			stdscr.refresh()		
			sleep(0.5)


def main():
	obj = SinglyLinkedListView()
	arr = []
	for i in range(20):
		arr.append(randint(1,100))
	obj.insert_all(arr)
	obj.delete(101)
	obj.delete_all(arr[-4:-1])


if __name__ == '__main__':
	main()


		