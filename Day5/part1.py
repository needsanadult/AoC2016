import hashlib
puzzle_input = 'ffykfhsq'
pw = []
counter = 0


while len(pw) < 8:
	val = puzzle_input + str(counter)
	m = hashlib.md5(val.encode('UTF-8'))
	h = m.hexdigest()
	if h[0:5] == '00000':
		pw.append(h[5])
	counter += 1

print (pw)