import sys

data = []

for i in sys.stdin:
    data.append(i)


data = [line.rstrip('\n') for line in data if line]

for datum in data:
    if 'problem' in datum.lower():
        print('yes')
    else:
        print('no')