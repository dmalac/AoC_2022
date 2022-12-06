# https://adventofcode.com/2022/day/6

with open("input.txt") as f:
	line = f.read()
def solution(line, dist):
	for i in range(len(line)):
		if len(set(line[i : i + dist])) == dist:
			return i + dist
print("First round:\t", solution(line, 4))
print("Second round:\t", solution(line, 14))