rawlist = 'R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1'

dirs = rawlist.split(', ')


direction_dict = {'N': [-1, 1],
				  'S': [1, -1],
				  'E': [1, -1],
				  'W': [-1, 1],
				  }

loc = [0, 0]
heading = 'N'


testdirs = ['R4', 'L2', 'L5', 'L1']


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




# for i in dirs:
# 	if re.match(left, i):
# 		heading = W
# 	else:
# 		heading = E

# for x in dirs:
# 	dis = int(x[1:])
# 	L_or_R = x[0]
# 	current_head = heading
# 	if x.startswith('R') and heading == 'N':
# 		loc[0] = loc[0] + dis
# 		heading = determine_heading(current_head, L_or_R)
# 	if x.startswith('L') and heading == 'N':
# 		loc[0] = loc[0] - dis
# 		heading = determine_heading(current_head, L_or_R)
# 	elif x.startswith('R') and heading == 'S':
# 		loc[0] = loc[0] - dis
# 		heading = determine_heading(current_head, L_or_R)
# 	elif x.startswith('L') and heading == 'S':
# 		loc[0] = loc[0] + dis
# 		heading = determine_heading(current_head, L_or_R)
# 	elif x.startswith('R') and heading == 'W':
# 		loc[1] = loc[1] + dis
# 		heading = determine_heading(current_head, L_or_R)
# 	elif x.startswith('L') and heading == 'W':
# 		loc[1] = loc[1] - dis
# 		heading = determine_heading(current_head, L_or_R)
# 	elif x.startswith('R') and heading == 'E':
# 		loc[1] = loc[1] - dis
# 		heading = determine_heading(current_head, L_or_R)
# 	else:
# 		loc[1] = loc[1] + dis
# 		heading = determine_heading(current_head, L_or_R)

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
	elif x.startswith('L') and heading == 'N':
		loc[0] = loc[0] - dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
	elif x.startswith('R') and heading == 'S':
		loc[0] = loc[0] - dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
	elif x.startswith('L') and heading == 'S':
		loc[0] = loc[0] + dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
	elif x.startswith('R') and heading == 'W':
		loc[1] = loc[1] + dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
	elif x.startswith('L') and heading == 'W':
		loc[1] = loc[1] - dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
	elif x.startswith('R') and heading == 'E':
		loc[1] = loc[1] - dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)
	else:
		loc[1] = loc[1] + dis
		print ('New Location:', loc)
		heading = determine_heading(current_head, L_or_R)
		print ('New Heading:', heading)



dist = abs(loc[0]) + abs(loc[1])

print (dist)