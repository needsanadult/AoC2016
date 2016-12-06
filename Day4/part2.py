list_of_results = []
def decode(num, s):
	global list_of_results
	global result
	for x in s:
		if x.isalpha():
			a = ord(x) - 97
			a += num
			a = a % 26
			result += chr(a + 97)
		else:
			result += x
	sector = result + '-' + str(num)
	list_of_results.append(sector)		
	return result


f = open('rooms.txt')
for line in f:
	result = ''
	g = line
	e = g[0:len(g) - 12]
	h = e.replace('-', ' ')
	n = int(g[len(g) - 11:len(g) - 8])
	decode(n, h)

sea = [s for s in list_of_results if 'northpole' in s]
print (sea)
