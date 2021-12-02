import re
from functools import reduce

f = open("puzzle_input.txt", "r")

input = [x for x in f]

# Part 1
def get_numbers(search_string):
    return [int(re.search(r'\d', x)[0]) for x in input if search_string in x]

forwards = get_numbers('forward')
ups = get_numbers('up')
downs = get_numbers('down')

depth = - sum(ups) + sum(downs)
loc = sum(forwards)

print(f'The answer to question 1 is: {depth*loc}')

# Part 2
route = list(map(lambda x: {'type': x[0], 'input': int(re.search(r'\d', x)[0]), 'aim':0, 'hor_loc':0, 'depth':0}, input))

def calculate_coors(prev, curr):
    curr['hor_loc'] = prev['hor_loc']
    curr['aim'] = prev['aim']
    curr['depth'] = prev['depth']
    if curr['type'] == 'f':
        curr['hor_loc'] = curr['hor_loc'] + curr['input']
        curr['depth'] = curr['depth'] + curr['aim']*curr['input']
    if curr['type'] == 'u':
        curr['aim'] = curr['aim'] - curr['input']
    if curr['type'] == 'd':
        curr['aim'] = curr['aim'] + curr['input']
    print(curr)
    return curr

final_coors = reduce(calculate_coors, route, route[0])
print(final_coors['hor_loc'] * final_coors['depth'])
