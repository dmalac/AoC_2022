# https://adventofcode.com/2022/day/1

import fileinput

current = 0
max_cal = [0, 0, 0]
for line in fileinput.input(files='input.txt'):
	if len(line) == 1:
		if current > min(max_cal):
			max_cal[0] = current
			max_cal.sort()
		current = 0
	else:
		current += int(line.strip())
if current > min(max_cal):
	max_cal[0] = current
print("First round:\t", max(max_cal))
print("Second round:\t", sum(max_cal))