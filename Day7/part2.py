import re
SSL = 0

def supernet_list(ip):
	inside_brackets = re.findall(r'(?<=\[)[a-z]+(?=\])', ip)
	for x in inside_brackets:
		ip = ip.replace('['+x+']', ' ')
	outside_brackets = ip.split()
	return outside_brackets

def hypernet_list(ip):
	inside_brackets = re.findall(r'(?<=\[)[a-z]+(?=\])', ip)
	return inside_brackets


def ABAs_and_BABs(list_of_nets):
	nets = []
	for x in list_of_nets:
		for a, b, c in zip(x, x[1:], x[2:]):
			if a == c and a != b:
				nets.append(a+b+c)
	return nets

f = open('ips.txt')
for line in f:
	slist = supernet_list(line)
	hlist = hypernet_list(line)
	aba_list = ABAs_and_BABs(slist)
	bab_list = ABAs_and_BABs(hlist)
	has_match = False
	for x in aba_list:
		aba_to_bab = x[1]+x[0]+x[1]
		if aba_to_bab in bab_list:
			has_match = True
	if has_match:
		SSL += 1
f.close()

print (SSL)
