triangles = 0

f = open('is_tri.txt')
for line in f:
	w = line
	w.strip()
	sides = w.split()
	for x in sides:
		t.append(int(x))

col1 = t[0::3]
col2 = t[1::3]
col3 = t[2::3]

c3 = [col3[i:i+3] for i in range(0, len(col3), 3)]
c2 = [col2[i:i+3] for i in range(0, len(col2), 3)]
c1 = [col1[i:i+3] for i in range(0, len(col1), 3)]


for s in range(len(c3)):
	c3[s].sort()

for s in range(len(c2)):
	c2[s].sort()

for s in range(len(c1)):
	c1[s].sort()

print (c3)

def count_tris(t):
	global triangles
	for x in t:
		if x[0] + x[1] > x[2]:
			triangles = triangles + 1

count_tris(c1)
count_tris(c2)
count_tris(c3)





