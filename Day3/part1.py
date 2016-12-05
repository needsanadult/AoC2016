triangles = 0

f = open('is_tri.txt')
for line in f:
	w = line
	w.strip()
	sides = w.split()
	for x in range(len(sides)):
		sides[x] = int(sides[x])
	sides.sort()
	if sides[0] + sides[1] > sides[2]:
		triangles = triangles + 1

print (triangles)
		