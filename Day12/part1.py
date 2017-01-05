import re
i = 0
registers = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
}

def copy_register(register_to_copy, register):
	if type(register_to_copy) == int:
		registers[register] = register_to_copy
	else:
		registers[register] = registers[register_to_copy]

def inc_dec_reg(instruction, register):
	if instruction == 'inc':
		registers[register] += 1
	else:
		registers[register] -= 1

def jump_instruction(reg_or_num, jump_num):
	if type(reg_or_num) == int:
		if reg_or_num != 0:
			return jump_num
		else:
			return 1
	else:
		if registers[reg_or_num] != 0:
			return jump_num 
		else:
			return 1


def fix_type(val):
	if len(val) > 1:
		return int(val)
	else:
		if ord(val) < 97:
			return int(val)
		else:
			return registers[val]

def jnz_type(val):
	if len(val) > 1:
		return int(val)
	else:
		if ord(val) < 97:
			return int(val)
		else:
			return registers[val]


f = open('instructions.txt').read().splitlines()

while i < len(f):
	loop_count = 1
	if f[i].startswith('i') or f[i].startswith('d'):
		regex_line = re.findall(r'([a-z]{3})\s([a-z])', f[i])
		inc_dec_reg(regex_line[0][0], regex_line[0][1])
	else:
		regex_line = re.findall(r'([a-z]{3})\s([a-z0-9]+)\s(-?[a-z0-9]{1,2})', f[i])
		conv = fix_type(regex_line[0][1])
		if regex_line[0][0] == 'cpy':
			copy_register(conv, regex_line[0][2])
		else:
			loop_count = jump_instruction(conv, int(regex_line[0][2]))
	i += loop_count


print (registers)