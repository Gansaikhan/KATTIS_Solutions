# @Author Gansaikhan Shur
# Who Wants to Live Forever? (https://open.kattis.com/problems/whowantstoliveforever)
# whowantstoliveforever/1.in has been used in this example
# Difficulty: 8.0

import sys


def get_bit(bits, i):
    if 0 <= i < len(bits):
        return int(bits[i])
    else:
        return 0


def get_new_state(old_state):
    new_state = []
    for index in range(len(old_state)):
        if((get_bit(old_state, index-1) ^ get_bit(old_state, index+1)) == 1):
            new_state.append(1)
        elif (get_bit(old_state, index-1) == 0 and get_bit(old_state, index+1) == 0) or (get_bit(old_state, index-1) == 1 and get_bit(old_state, index+1) == 1):
            new_state.append(0)
    return new_state


def is_dead(state):
    if set(state).pop() == "1":
        return False
    elif set(state).pop() == 1:
        return False
    elif len(set(state)) == 1:
        return True
    else:
        return False


def foresee_fate(state):
    seen = []
    while True:
        if is_dead(state):
            return False
        if state in seen:
            return True
        seen.append(state)
        state = get_new_state(state)


num_cases = int(sys.stdin.readline().strip())
for i in range(num_cases):
    cur_state = []
    case = sys.stdin.readline().strip()
    for char in case:
        cur_state.append(char)
    print("LIVES" if foresee_fate(cur_state) else "DIES")
