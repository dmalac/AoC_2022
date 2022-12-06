# https://adventofcode.com/2022/day/5

import re
import copy

with open("input.txt") as file:
	tmp_st, tmp_instr = file.read().split('\n\n')
# make a dictionary with input
tmp_st = tmp_st.split('\n')
orig_stacks = {}
for item in sorted(tmp_st[-1].replace(' ', '')):
	orig_stacks[item] = []
for i in range(-2, (len(tmp_st) + 1) * -1, -1):
	for j in range(len(tmp_st[i])):
		if tmp_st[i][j].isalpha():
			orig_stacks[str(int((j + 3)/4))].append(tmp_st[i][j])
# prepare instructions
instr = re.sub("[a-z]", '', tmp_instr).split('\n')

def top_packets(stacks):
	result = ""
	for k in stacks:
		result += stacks[k][-1]
	return result

def first_round(stacks, instr):
	for line in instr:
		times, src, dest = line.split()
		for move in range(int(times)):
			stacks[dest].append(stacks[src].pop())
	return (top_packets(stacks))

def second_round(stacks, instr):
	for line in instr:
		pcs, src, dest = line.split()
		stacks[dest] += stacks[src][int(pcs) * -1:]
		stacks[src] = stacks[src][:int(pcs) * -1]
	return (top_packets(stacks))

print("First round:\t", first_round(copy.deepcopy(orig_stacks), instr))
print("Second round:\t", second_round(copy.deepcopy(orig_stacks), instr))
