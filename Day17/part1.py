import hashlib

code = 'vwbaicqe'

maze = [[0 for i in range(4)] for i in range(4)]

maze[0][0] = 1
maze[3][3] = 4
maze[0][3] = 2
maze[3][0] = 3
maze[0][1] = 'N'
maze[0][2] = 'N'
maze[1][0] = 'W'
maze[2][0] = 'W'
maze[1][3] = 'E'
maze[2][3] = 'E'
maze[3][1] = 'S'
maze[3][2] = 'S'

r = [i+1 for i in range(16)]


rooms = []
for x in range(0, len(r), 4):
	rooms.append(r[x:x+4])

print (rooms)
print (maze)

adj = []

for x in range(len(maze)):
	for y in range(len(rooms)):
		adj.append((rooms[x][y], maze[x][y]))

print (adj)