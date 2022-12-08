# https://adventofcode.com/2022/day/8

import numpy as np
from copy import deepcopy

with open("input.txt") as f:
	a = np.array([list(x) for x in list(f.read().split('\n'))]).astype(int)

shadow = np.full((a.shape), 1)
shadow[1:len(shadow[0,:]) - 1, 1:len(shadow[:,0]) - 1] = 0

def check_visibility(a: np.ndarray, shadow: np.ndarray):
	for i in range (len(a[0])):
		max = a[i][0]
		for j in range (len(a[i])):
			if a[i][j] > max:
				shadow[i][j] = 1
				max = a[i][j]
		max = a[i][len(a[i]) - 1]
		for j in range (len(a[i]) -1 , -1, -1):
			if a[i][j] > max:
				shadow[i][j] = 1
				max = a[i][j]

def scenic_score(val: int, x: int, y: int, x_add: int, y_add: int) -> int:
	score = 0
	while (0 < x < len(a[0]) - 1  and 0 < y < len(a) - 1):
		x += x_add
		y += y_add
		score += 1
		if (a[y][x] >= val):
			return score
	return score

def calc_max_score(y: int, x: int) -> int:
	score = 1
	for x_add, y_add in [(0,-1), (0,1), (-1,0), (1,0)]:
		score *= scenic_score(a[y][x], x, y, x_add, y_add)
	return score

check_visibility(a.transpose(), shadow.transpose())
check_visibility(a, shadow)
print ("First round:\t", shadow.sum())

it = np.nditer(shadow, flags=['multi_index'])
max_score = 0
for x in it:
	if x == 1 and all(c < len(a[0]) - 1 for c in it.multi_index) \
	and all(c > 0 for c in it.multi_index):
		score = calc_max_score(it.multi_index[0], it.multi_index[1])
		max_score = score if score > max_score else max_score
print ("Second round:\t", max_score)
