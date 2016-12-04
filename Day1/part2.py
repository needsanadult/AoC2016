def pos_vert_coords(number):
	for x in range(number):
		alter_val = travels[len(travels)-1][1]
		tupval = (travels[len(travels)-1][0], alter_val + 1)
		travels.append(tuple(tupval))
	return travels

def neg_vert_coords(number):
	for x in range(number):
		alter_val = travels[len(travels)-1][1]
		tupval = (travels[len(travels)-1][0], alter_val - 1)
		travels.append(tuple(tupval))
	return travels

def pos_horz_coords(num):
	for x in range(num):
		alter_val = travels[len(travels)-1][0]
		tupval = (alter_val + 1, travels[len(travels)-1][1])
		travels.append(tuple(tupval))
	return travels

def neg_horz_coords(num):
	for x in range(num):
		alter_val = travels[len(travels)-1][0]
		tupval = (alter_val - 1, travels[len(travels)-1][1])
		travels.append(tuple(tupval))
	return travels

tst_dir = ['R2', 'L5', 'L1', 'L6']

rawlist = 'R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1'

dirs = rawlist.split(', ')

loc = [0, 0]

heading = 'N'

def determine_heading(head, direction):
	if head == 'N':
		if direction == 'L':
			head = 'W'
		else:
			head = 'E'
	elif head == 'S':
		if direction == 'L':
			head = 'E'
		else:
			head = 'W'
	elif head == 'W':
		if direction == 'L':
			head = 'S'
		else:
			head = 'N'
	elif head == 'E':
		if direction == 'L':
			head = 'N'
		else:
			head = 'S'
	return head

for x in dirs:
	print ('Starting Location:', loc)
	print ('Starting Heading:', heading)
	dis = int(x[1:])
	print ('Amount to travel:', dis)
	L_or_R = x[0]
	print ('Turn Direction:', L_or_R)
	current_head = heading
	print ('Current Heading:', current_head)
	if x.startswith('R') and heading == 'N':
		loc[0] = loc[0] + dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
		pos_horz_coords(dis)
	elif x.startswith('L') and heading == 'N':
		loc[0] = loc[0] - dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
		neg_horz_coords(dis)
	elif x.startswith('R') and heading == 'S':
		loc[0] = loc[0] - dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
		neg_horz_coords(dis)
	elif x.startswith('L') and heading == 'S':
		loc[0] = loc[0] + dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
		pos_horz_coords(dis)
	elif x.startswith('R') and heading == 'W':
		loc[1] = loc[1] + dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
		pos_vert_coords(dis)
	elif x.startswith('L') and heading == 'W':
		loc[1] = loc[1] - dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
		neg_vert_coords(dis)
	elif x.startswith('R') and heading == 'E':
		loc[1] = loc[1] - dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
		neg_vert_coords(dis)
	else:
		loc[1] = loc[1] + dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
		pos_vert_coords(dis)
print (travels)


vals = []
for x in travels:
  if travels.count(x) >=2:
    vals.append(x)

print (vals)

blocks = vals[0][0] + vals[0][1]
print (blocks)