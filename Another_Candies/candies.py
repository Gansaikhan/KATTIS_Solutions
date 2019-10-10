# @Author Gansaikhan Shur
# Another Candies (https://open.kattis.com/problems/anothercandies)
# anothercandies/a.in has been used in this example.

import sys
num_cases = int(sys.stdin.readline().strip())


for i in range(0, num_cases):
    # Read the blank line so looping through is easier
    empty_line = sys.stdin.readline()
    num_students = int(sys.stdin.readline().strip())
    total = 0
    for j in range(0, num_students):
        total += int(sys.stdin.readline().strip())
    print("YES" if total % num_students == 0 else "NO")
