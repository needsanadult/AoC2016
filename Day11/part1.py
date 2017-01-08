###################################################################
#  Rules
#		-A chip has to be on the same floor with its own generator if another 
#		generator is on that floor
#		
# 		-The elevator has to at one item in it, either a generator or a chip,
#		to function
#		
#		-The elvator stops on every floor it goes by.
#
#		
#  
#  Valid move
#		-if floor is empty don't go back
#		
#  		-if there are generators on the floor the maximum amount of chips
#		is equal to the amount of generators
#		EX: a-generator a-chip b-generator b-chip (must be paired)
#		
#		-if there are chips on the floor there can be any number of generators 
#		as long as their chips match
#		EX: a-generator a-chip b-chip c-chip (any chips as long as generator is paired)
#
#
#  Code
#	** Loop
#		while len(f4) != 8
#   
#	** Bottom floor (initialized to f1)
#		for floor in floors:
#			if len(floor) != 0:
#				bottom_floor = floor
#
#		
#
#
#
###################################################################

gens = ['promethium', 'curium', 'cobalt', 'ruthenium', 'plutonium']
chips = ['promethium', 'curium', 'cobalt', 'ruthenium', 'plutonium']
elavator = []

f1 = [gens[0], chips[0]]
f2 = [gens[1], gens[2], gens[3], gens[4]]
f3 = [chips[1], chips[2], chips[3], chips[4]]
f4 = []
floors = [f1, f2, f3, f4]
bottom_floor = f1

adj_list = [[1], [0, 2], [1, 3], [2]]


def BFS(s, adj):
	level = {s: 0}
	parent = {s: None}
	i = 1
	frontier = [s]
	while frontier:
		next = []
		for u in frontier:
			for v in adj[u]:
				if v not in level:
					level[v] = i
					parent[v] = u
					next.append(v)
		frontier = next
		i += 1


BFS(adj_list[0], adj_list)

