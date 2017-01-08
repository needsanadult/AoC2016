sample ='1'
data = '10010000000110000'
disk_length = 272
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
	
a = '10010000000110000'
while len(a) < disk_length:
	b = rev_str(a)
	b = opp_str(b)
	a = a_0_b(a, b)

# print (a)
# minus = len(a)-disk_length
# a = a[:-minus]

# print (len(a))
# print (a)

# def check_sum(s):
# 	check_sum = ''
# 	for x in range(0, len(s), 2):
# 		if a[x] == a[x+1]:
# 			check_sum += '1'
# 		else:
# 			check_sum += '0'
# 	return check_sum

# def find_odd(length, num):
# 	print (length, num)
# 	if length%2 == 0:
# 		return find_odd(length/2, num+1)
# 	else:
# 		return num	

# for x in range(int(find_odd(136, 1))):
# 	a = check_sum(a)


print (a)
print (len(a))
