import re

bots_with_micros = {}
bots_give_micros = {}


f = open('instructions.txt')
for line in f:
	if line.startswith('bot'):
		bot_out = re.findall(r'bot\s(\d+)\sgives\slow\sto\s(output|bot)\s(\d+)\sand\shigh\sto\s(output|bot)\s(\d+)', line)
		bots_with_micros[int(bot_out[0][0])] = []
		if bot_out[0][1] == 'output' and bot_out[0][3] == 'output':
			bots_give_micros[int(bot_out[0][0])] = [300+int(bot_out[0][2]), 300+int(bot_out[0][4])]
			bots_with_micros[300+int(bot_out[0][2])] = []
			bots_with_micros[300+int(bot_out[0][4])] = []
		elif bot_out[0][1] == 'output' and bot_out[0][3] == 'bot':
			bots_give_micros[int(bot_out[0][0])] = [300+int(bot_out[0][2]), int(bot_out[0][4])]
			bots_with_micros[300+int(bot_out[0][2])] = []
		elif bot_out[0][1] == 'bot' and bot_out[0][3] == 'bot':
			bots_give_micros[int(bot_out[0][0])] = [int(bot_out[0][2]), int(bot_out[0][4])]
		else:
			bots_give_micros[int(bot_out[0][0])] = [int(bot_out[0][2]), 300+int(bot_out[0][4])]
			bots_with_micros[300+int(bot_out[0][4])] = []
f.close()
f = open('instructions.txt')
for line in f:
	if line.startswith('value'):
		value = re.findall(r'value\s(\d+)\sgoes\sto\sbot\s(\d+)', line)
		if not bots_with_micros[int(value[0][1])]:
			bots_with_micros[int(value[0][1])] = [int(value[0][0])]
		elif bots_with_micros[int(value[0][1])][0] < int(value[0][0]):
			bots_with_micros[int(value[0][1])].append(int(value[0][0]))
		else:
			bots_with_micros[int(value[0][1])] = [int(value[0][0]), my_dict[int(value[0][1])][0]]
f.close()
		

print (bots_with_micros)
print (bots_give_micros)

def arrange_micros(bot_that_just_got_micros):
	if len(bots_with_micros[bot_that_just_got_micros]) == 2:
		if bots_with_micros[bot_that_just_got_micros][0] > bots_with_micros[bot_that_just_got_micros][1]:
			bots_with_micros[bot_that_just_got_micros] = [bots_with_micros[bot_that_just_got_micros][1], bots_with_micros[bot_that_just_got_micros][0]]


has_two = True
find_bot = 0
while has_two:
	has_two = False
	for key, val in bots_with_micros.items():
		if len(val) == 2:
			lowValue = bots_with_micros[key][0]
			bot_to_get_lowValue = bots_give_micros[key][0]
			bots_with_micros[bot_to_get_lowValue].append(lowValue)
			highValue = bots_with_micros[key][1]
			bot_to_get_highValue = bots_give_micros[key][1]
			bots_with_micros[bot_to_get_highValue].append(highValue)
			bots_with_micros[key] = []
			if bot_to_get_lowValue != None:
				arrange_micros(bot_to_get_lowValue)
			if bot_to_get_highValue != None:
				arrange_micros(bot_to_get_highValue)
	for key, val in bots_with_micros.items():
		if len(val) == 2:
			has_two = True

def find_mult():
	value = bots_with_micros[300][0] * bots_with_micros[301][0] * bots_with_micros[302][0]
	return value


print (find_mult())