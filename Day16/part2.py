import re

sample ='1'
data = '10010000000110000'
disk_length = 35651584
def rev_str(s):
	return s[::-1]

def opp_str(s):
	new_str = ''
	for val in s:
		if val == '0':
			new_str += '1'
		else:
			new_str += '0'
	return new_str

def a_0_b(a, b):
	return a+'0'+b

def data(s):
	b = s[::-1]
	b = b.replace('1', '2').replace('0', '1').replace('2', '0')
	return a+'0'+b


a = '10010000000110000'
# while len(a) < disk_length:
# 	b = rev_str(a)
# 	b = opp_str(b)
# 	a = a_0_b(a, b)

while len(a) < disk_length:
	a = data(a)

minus = len(a)-disk_length
a = a[:-minus]

def check_sum(s):
	check_sum = ''
	for x in range(0, len(s), 2):
		if a[x] == a[x+1]:
			check_sum += '1'
		else:
			check_sum += '0'
	return check_sum

def re_check(s):
	check_sum = ''
	matches = re.findall(r'.{2}', s)
	for x in matches:
		if x[0] == x[1]:
			check_sum += '1'
		else:
			check_sum += '0'
	return check_sum		

def checksum(s):
	checksum = ''
	for x, y in zip(s[0::2], s[1::2]):
		if x == y:
			checksum += '1'
		else:
			checksum += '0'
	return checksum

def odd(num):
	i = 0
	while num%2 == 0:
		num = num/2
		i += 1
	return i



cs_times = odd(len(a))

while cs_times > 0:
	a = checksum(a)
	cs_times -= 1

print (a)