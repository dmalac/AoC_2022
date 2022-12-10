# https://adventofcode.com/2022/day/10

with open("input.txt") as f:
	input = f.read().split('\n')
instr = []
for line in input:
	instr.append(0)
	if line[:4] == "addx":
		instr.append(int(line.split(' ')[1]))
instr[0] += 1	# X is 1 at the beginning

# PART 1
result = sum(num * sum(instr[:num - 1]) for num in range (20, 221, 40))

# PART 2
screen = ""
for num in range(len(instr)):
	screen += '#' if abs(num % 40 - sum(instr[:num])) <= 1 else '.'
	if (num + 1) % 40 == 0:
		screen += '\n'

print ("First round:\t", result)
print ("Second round:")
print (screen)
