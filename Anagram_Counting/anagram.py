# @Author Gansaikhan Shur
# Anagram Counting (https://open.kattis.com/problems/anagramcounting)
# samples/sample.in has been used in this example

import sys

data = []
for i in sys.stdin:
    data.append(i)

data = [line.rstrip('\n') for line in data if line]

for i in range(len(data)):
    cur_str = data[i]
    anagram_count = 0
    print(cur_str)
