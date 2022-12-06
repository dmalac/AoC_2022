# https://adventofcode.com/2022/day/3

import fileinput
result = 0
for line in fileinput.input("input.txt"):
	a = (list(set(line[:int(len(line)/2)]) & set(line[int(len(line)/2):]))[0])
	result += ord(a) - ord('a') + 1 if a.islower() else ord(a) - ord('A') + 27
print(result)