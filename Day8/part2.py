import re

line_count = 0
lit = 0


screen = [[0 for i in range(50)] for i in range(6)]


def make_rect(column, row):
	for x in range(row):
		for y in range(column):
			screen[x][y] = 1
	return screen


def move_row(row, shift):
	row_to_shift = screen[row]
	startrow = row_to_shift[-shift:]
	endrow = row_to_shift[0:-shift]
	finalrow = startrow + endrow
	screen[row] = finalrow
	return screen
	

def move_column(column, shift):
	collist = [x[column] for x in screen]
	startcol = collist[-shift:]
	endcol = collist[0:-shift]
	finalcol = startcol + endcol
	for x in range(len(screen)):
		screen[x][column] = finalcol[x]
	return screen

f = open('commands.txt')
for line in f:
	shift_pos = []
	rect = []
	s = line.split()
	if s[0] == 'rect':
		rect = re.findall(r'rect (\d+)x(\d+)', line)
		rect_row = int(rect[0][1])
		rect_col = int(rect[0][0])
		make_rect(rect_col, rect_row)
	else:
		shift_pos = re.findall(r'\w+\s{1}([a-z]+)\s(x|y)=(\d+)\s{1}by\s{1}(\d+)', line)
		if shift_pos[0][0] == 'row':
			row_shift = int(shift_pos[0][3])
			row_num = int(shift_pos[0][2])
			move_row(row_num, row_shift)
		else:
			col_shift = int(shift_pos[0][3])
			col_num = int(shift_pos[0][2])
			move_column(col_num, col_shift)
	line_count += 1	

f.close()
for x in range(len(screen)):
	for y in range(len(screen[x])):
		lit = lit + screen[x][y]

print (lit)

for x in screen:
	print (x)