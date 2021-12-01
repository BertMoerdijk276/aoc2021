# 1st part:
f = open("puzzle_input.txt", "r")
input = [int(x) for x in f]

number_increased = sum([x > input[i] for i, x in enumerate(input[1:])])
print(f'The 1st answer is {number_increased}')

# 2nd part:
def compare_windows(i, wl):
    return sum(input[i+1:i+1+wl]) > sum(input[i:i+wl])

window_length = 3

number_increased_2 = sum([compare_windows(i, window_length) for i, _ in enumerate(input[window_length:])])
print(f'The 2nd answer is {number_increased_2}')
