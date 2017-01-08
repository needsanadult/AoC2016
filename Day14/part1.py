import hashlib
import re
import sys
sys.setrecursionlimit(2020)

puzzle = 'qzyelonm'
num = 0
trips = []
quints = []
def recursivehash(a_hash, num):
	if num+1 > 0:
		new_hash = hashlib.md5(a_hash.encode('UTF-8')).hexdigest()
		return recursivehash(new_hash, num-1)
	else:
		return a_hash

def loophash(to_hash, value):
	end_hash = hashlib.md5(to_hash.encode('UTF-8')).hexdigest()
	for _ in range(value):
		end_hash = hashlib.md5(end_hash.encode('UTF-8')).hexdigest()
	return end_hash

def find_trip(s):
	has_trip = re.findall(r'([abcdef0-9])\1\1', s)
	if has_trip:
		return True
	else:
		return False

# while len(vals) < 750:
# 	hashed = recursivehash(puzzle+str(num), 2016)
# 	if find_trip(hashed):
# 		trips.append((num, hashed))
# 	num += 1

while len(vals) < 750:
	h = loophash(puzzle+str(num), 2016)
	if find_trip(h):
		trips.append((num, h))
	num += 1

