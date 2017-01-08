import hashlib
puzzle_input = 'ffykfhsq'
pw = []
counter = 0
find_order = []

while len(find_order) < 8:
	val = puzzle_input + str(counter)
	m = hashlib.md5(val.encode('UTF-8'))
	h = m.hexdigest()
	if h[0:5] == '00000' and ord(h[5]) >= 48 and ord(h[5]) <= 55 and h[5] not in find_order:
		pw.append((h[5], h[6]))
		find_order.append(h[5])
	counter += 1

pw.sort()

print (pw)

