# https://adventofcode.com/2022/day/7

with open("input.txt", 'r') as file:
	line = file.read().split('\n')

def fill_dict(d):
	global i
	while line[i][0] == '$':
		i += 1
	while i < len(line) and line[i][0] != '$':
		a, b = line[i].split(' ')
		d[b] = {} if a == "dir" else int(a)
		i += 1
	while i < len(line) and line[i][0] == '$':
		x, y, z = line[i].split(' ')
		if z == "..":
			i += 1
			return
		else:
			fill_dict(d[z])

def calculate_dict(d):
	res = 0
	for key, value in d.items():
		if type(value) == type(home):
			subres = calculate_dict(d[key])
			sizes.append((key,subres))
			res += subres 
		else:
			res += value
	return res

home = {}
i = 0
sizes = []
# process input
fill_dict(home)
# PART 1
size = calculate_dict(home)
sizes.append(('/',size))
sizes = sorted(sizes, key=lambda tup: tup[1])
total = 0
for item in sizes:
	total += item[1] if item[1] <= 100000 else 0
print("First round:\t", total)
# PART 2
total_disk = 70000000
needed = 30000000
unused = total_disk - sizes[-1][1]
for item in sizes:
	if item[1] + unused >= needed:
		print("Second round:\t", item[1])
		break
