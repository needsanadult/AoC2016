import hashlib
import re


puzzle = 'qzyelonm'

key_index = []

t = 0

def hashed(s):
	v = puzzle+str(s)
	h = hashlib.md5(v.encode('UTF-8')).hexdigest()
	return h

def has_triple(s):
	s1 = re.findall(r'([abcdef0-9])\1\1', s)
	if s1:
		return True
	else:
		return False


def has_quint(s):
	s1 = re.findall(r'([abcdef0-9])\1\1\1\1', s)
	if s1:
		return True
	else:
		return False

def hash_char(h):
	match = re.findall(r'([abcdef0-9])\1\1', h)
	return match[0]

def quintuple(quint, value, thehex):
	search = True
	num = value
	while search and num < value+1000:
		qhash = hashed(puzzle+str(num))
		print ('from', thash, '(index', value-1, ')', 'we found a triple and got', quint, 'and looking for it in', qhash, 'which is number', num)
		if quint in qhash:
			key_index.append(value-1)
			search = False
		num += 1

for x in range(130000):
	v = hashed(puzzle+str(x))
	if has_quint(v):
		print (x, v)

# i = 0
# while len(key_index) < 1:
# 	thash = hashed(puzzle+str(i))
# 	if has_triple(thash):
# 		char = hash_char(thash)
# 		quintuple(char*5, i+1, thash)
# 	i += 1

print (key_index)
print (len(key_index))
