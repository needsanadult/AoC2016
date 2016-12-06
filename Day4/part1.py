room_sums = 0
f = open('rooms.txt')
for line in f:
	match = []
	results = []
	final = []
	d = line
	e = d.replace('-', '')
	f = e[0:len(e) - 11]
	num = int(e[len(e) - 11:len(e) - 8])
	s = e[len(e) - 7:len(e) - 2]
	for x in s:
		match.append(x)
	h = list(set(f))
	for x in h:
		final.append((x, f.count(x)))
	final.sort()
	final.sort(reverse=True, key=lambda x: x[1])
	first5 = final[:5]
	for i, j in first5:
		results.append(i)
	if match == results:
		room_sums += num
print (room_sums)
