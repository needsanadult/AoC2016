list_of_letters = []
secret_word = ''

def maxval(dic):
	v = list(dic.values())
	k = list(dic.keys())
	return k[v.index(max(v))]

f = open('msg.txt')
for line in f:
	as_string = line.rstrip('\n')
	for x in as_string:
		list_of_letters.append(x)
for x in range(8):
	col_list = list_of_letters[x::8]
	col_dict = {x:col_list.count(x) for x in col_list}
	secret_word += maxval(col_dict)

print (secret_word)