maze = [[0 for i in range(50)] for i in range(50)]

def input_sum(x, y):
	bits = 0
	s = bin(x**2 + 3*x + 2*x*y + y + y**2 + 1362)
	t = s[2:]
	for dig in t:
		bits += int(dig)
	if bits % 2 == 0:
		return True
	else:
		return False

def is_room(x, y):
	if maze[x][y] == '.':
		return True
	else:
		return False


def node_value(x, y):
	return 50*x + y+1

for x in range(len(maze)):
	for y in range(len(maze[x])):
		if input_sum(x, y):
			maze[x][y] = '.'
		else:
			maze[x][y] = '#'

adj_list = {}

for x in range(len(maze)):
	for y in range(len(maze[x])):
		if maze[x][y] == '.':
			node = node_value(x, y)
			if x == 0 and y == 0:
				if is_room(x, y+1):
					adj_node = node_value(x, y+1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x+1, y):
					adj_node = node_value(x+1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
			elif x == 49 and y == 0:
				if is_room(x, y+1):
					adj_node = node_value(x, y+1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x-1, y):
					adj_node = node_value(x-1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
			elif x == 0 and y ==49:
				if is_room(x, y-1):
					adj_node = node_value(x, y-1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x+1, y):
					adj_node = node_value(x+1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
			elif x == 49 and y == 49:
				if is_room(x, y-1):
					adj_node = node_value(x, y-1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x-1, y):
					adj_node = node_value(x-1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
			elif x == 0:
				if is_room(x, y+1):
					if node in adj_list:
						adj_list[node].append(node_value(x, y+1))
					else:
						adj_list[node] = [node_value(x, y+1)]
				if is_room(x, y-1):
					if node in adj_list:
						adj_list[node].append(node_value(x, y-1))
					else:
						adj_list[node] = [node_value(x, y-1)]
				if is_room(x+1, y):
					if node in adj_list:
						adj_list[node].append(node_value(x+1, y))
					else:
						adj_list[node] = [node_value(x+1, y)]
			elif x == 49:
				if is_room(x, y+1):
					adj_node = node_value(x, y+1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x, y-1):
					adj_node = node_value(x, y-1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x-1, y):
					adj_node = node_value(x-1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
			elif y == 0:
				if is_room(x, y+1):
					adj_node = node_value(x, y+1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x+1, y):
					adj_node = node_value(x+1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x-1, y):
					adj_node = node_value(x-1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
			elif y == 49:
				if is_room(x, y-1):
					adj_node = node_value(x, y-1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x+1, y):
					adj_node = node_value(x+1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x-1, y):
					adj_node = node_value(x-1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
			else:
				if is_room(x, y+1):
					adj_node = node_value(x, y+1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x, y-1):
					adj_node = node_value(x, y-1)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x+1, y):
					adj_node = node_value(x+1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]
				if is_room(x-1, y):
					adj_node = node_value(x-1, y)
					if node in adj_list:
						adj_list[node].append(adj_node)
					else:
						adj_list[node] = [adj_node]

def bfs(s, adj, e):
	level = {s: 0}
	parent = {s: None}
	i = 1
	frontier = [s]
	while frontier:
		# print ('the frontier is:', frontier)
		next = []
		for u in frontier:
			# print ('u of frontier:', u)
			for v in adj[u]:
				# print ('v of adj[u]:', v, adj[u])
				if v not in level:
					# print ('level before v if not in level:', level)
					level[v] = i
					# print ('level after:', level)
					parent[v] = u
					# print ('the parents are:', parent)
					next.append(v)
					# print ('next is:', next)
		frontier = next
		i += 1
		# print ('end before while')
		# print ('')
	return level[e]

print (bfs(52, adj_list, 1590))
