import numpy, time, sys, os
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
					new_array[x, y] = 0
				elif num < 4:
					new_array[x, y] = 1
				else:
					new_array[x, y] = 0
			else:
				if num == 3:
					new_array[x, y] = 1

	return new_array

def is_board_dead(board):
    return board.sum() == 0

def print_board(board):
    for y in xrange(0, board.shape[1]):
        for x in xrange(0, board.shape[0]):
            if board[x,y] == 1:
                sys.stdout.write('\033[7m  \033[0m')
            else:
                sys.stdout.write('  '),

        sys.stdout.write("\n")

def clear_screen():
    print("\x1b[2J\x1b[H")

def main():
	y, x = os.popen('stty size', 'r').read().split()
	x = int(x) / 2 - 4
	y = int(y) - 4

	the_array = make_board(x, y)
	for x in xrange(1,100):
		the_array = check_board(the_array)
                clear_screen()

		if is_board_dead(the_array):
		    print "No life here"
		    sys.exit()

                print_board(the_array)
                time.sleep(0.1)
		# draw_array(the_array)


main()
