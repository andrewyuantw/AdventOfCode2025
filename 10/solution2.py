import time
from itertools import combinations
from functools import cache
from collections import defaultdict

# If there are n buttons, precomputes the end state of the possible ways to press the buttons
# For each button, we can choose to press or not to press. This results in 2^n possibilities. 
@cache
def get_end_state_to_button_combo_map(buttons, state_length):
    ret = defaultdict(list)
    power_set = [list(s) for r in range(len(buttons) + 1) for s in combinations(buttons, r)]
    for button_combo in power_set:
        curr_state = [True] * state_length
        for button in button_combo:
            for i in button:
                curr_state[i] = not curr_state[i]
        curr_state = tuple(curr_state)
        ret[curr_state].append(button_combo)
    return ret

@cache
def get_least_number_of_presses(target, buttons):
    ret = float('inf')
    if all(x == 0 for x in target):
        return 0

    encoded_odd_even_state = tuple(x % 2 == 0 for x in target)
    # Cached separately since dicts aren't hashable as @cache keys
    end_state_to_button_combo_map = get_end_state_to_button_combo_map(buttons, len(target))
    button_powersets = end_state_to_button_combo_map.get(encoded_odd_even_state, [])

    for button_combo in button_powersets:
        new_target_state = list(target)
        for button in button_combo:
            for i in button:
                new_target_state[i] -= 1
        
        if any(x < 0 for x in new_target_state):
            continue

        # Bifurcate method described in https://www.reddit.com/r/adventofcode/comments/1pk87hl/comment/ntp4njq/
        new_target_state = tuple(x//2 for x in new_target_state)
        ret = min(ret, len(button_combo) + 2 * get_least_number_of_presses(new_target_state, buttons))

    return ret

def parse_line(line):
    buttons = []
    for segment in line.split():
        if segment[0] == '(':
            buttons.append(tuple(int(x) for x in segment[1:-1].split(',')))
        elif segment[0] == '{':
            target_state = tuple(int(x) for x in segment[1:-1].split(','))
    return target_state, tuple(buttons)

with open('real_input.txt') as file:
    data = file.read().split("\n")
    ret = 0
    overall_start = time.time()

    for counter, line in enumerate(data):
        print(f"Processing line {counter}")
        target_state, buttons = parse_line(line)
        ret += get_least_number_of_presses(target_state, buttons)
        
    total_elapsed = time.time() - overall_start
    print(f"Total elapsed {total_elapsed:.3f}")   

    print(ret)