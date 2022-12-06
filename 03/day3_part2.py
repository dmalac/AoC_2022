# https://adventofcode.com/2022/day/3

result = 0
with open("input.txt") as file:
	lines = [line.strip('\n') for line in file]
for i in range(0,len(lines),3):
	a = list(set(set(lines[i]) & set(lines[i+1])) & set(lines[i+2]))[0]
	result += ord(a) - ord('a') + 1 if a.islower() else ord(a) - ord('A') + 27
print(result)
