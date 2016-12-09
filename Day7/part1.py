import re
TLS = 0

def abba_check(s):
	check = False
	match = re.findall(r'([a-z])([a-z])\2\1', s)
	for x in match:
		if x[0] != x[1]:
			check = True
			return check

f = open('ips.txt')
for line in f:
	fail = False
	success = False
	fail_test = re.findall(r'[a-z]+(?=\])', line)
	pass_test1 = re.findall(r'(?<=\])[a-z]+', line)
	pass_test2 = re.findall(r'[a-z]+(?=\[)', line)
	pass_test = pass_test1 + pass_test2
	for part in fail_test:
		if abba_check(part):
			fail = True
	for part in pass_test:
		if abba_check(part):
			success = True
	if not fail and success:
		TLS += 1
f.close()

print (TLS)
