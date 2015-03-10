import numpy
from random import randrange


def make_array(x, y):
	the_array = numpy.zeros((x, y))
	return the_array


def make_board(x, y):
	the_array = make_array(x, y)
	for i in xrange(0,x):
		for j in xrange(0,y):
			val = randrange(3)
			if val == 2:
				the_array[i, j] = True
			else:
				the_array[i, j] = False

	return the_array


def count_neighbours(the_array, x, y):
	width = the_array.shape[0]
	height = the_array.shape[1]
	num = 0
	for i in xrange(-1,1):
		xposn = i + x
		for j in xrange(-1,1):
			yposn = j + y
			if yposn > 0 and yposn < height:
				if xposn > 0 and xposn < width:
					if the_array[xposn, yposn]:
						num += 1
	return num


def check_board(the_array):
	width = the_array.shape[0]
	height = the_array.shape[1]
	new_array = make_array(width, height)
	for x in xrange(0, width):
		for y in xrange(0, height):
			num = count_neighbours(the_array, x, y)
			if the_array[x, y]:
				if num < 2:
					new_array[x, y] = False
				elif num < 4:
					new_array[x, y] = True
				else:
					new_array[x, y] = False
			else:
				if num == 3:
					new_array[x, y] = True

	return new_array


def main():
	x = 100
	y = 100
	the_array = make_board(x, y)
	for x in xrange(1,10):
		the_array = check_board(the_array)
		# draw_array(the_array)


main()
