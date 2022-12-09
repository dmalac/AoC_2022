# https://adventofcode.com/2022/day/9

def move_knot(h: list, t: list, where: str):
	if abs(t[0] - h[0]) > 1 or abs(t[1] - h[1]) > 1:
		t[0] += 0 if h[0] == t[0] else int((h[0] - t[0])/abs(h[0] - t[0]))
		t[1] += 0 if h[1] == t[1] else int((h[1] - t[1])/abs(h[1] - t[1]))

def move_rope(knots: list, where: str):
	for i, knot in enumerate(knots):
		if i == 0:
			knot[0] += direction[where][0]
			knot[1] += direction[where][1]
		else:
			move_knot(knots[i - 1], knot, where)
	places.append((knots[-1][0], knots[-1][1]))

with open("input.txt") as f:
	inst = f.read().split('\n')

direction = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
result = []

for rope_len in [2, 10]:
	knots = [[0,0] for i in range(rope_len)]
	places = []
	for line in inst:
		where, steps = line.split(' ')
		for step in range(int(steps)):
			move_rope(knots, where)
	result.append(len(set(places)))

print ("First round:\t", result[0])
print ("Second round:\t", result[1])
