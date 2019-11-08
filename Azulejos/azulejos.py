# @Author Gansaikhan Shur
# Azulejos (https://open.kattis.com/problems/azulejos)
# azulejos 1.in has been used in this example.

import sys

n_tiles_row = int(sys.stdin.readline().rstrip())
# print(n_tiles_row) ==> 4

# BACK ROW - JOAO
back_row_price = sys.stdin.readline().rstrip()
# print(back_row_price) ==> 3 2 1 2

back_row_height = sys.stdin.readline().rstrip()
# print(back_row_height) ==> 2 3 4 3

# FRONT ROW - MARIA
front_row_price = sys.stdin.readline().rstrip()
# print(front_row_price) ==> 2 1 2 1

front_row_height = sys.stdin.readline().rstrip()
# print(front_row_height) ==> 2 2 1 3

# preprocess data into lists of ints
back_row_price = [int(x) for x in back_row_price.strip().split(' ')]
back_row_height = [int(x) for x in back_row_height.strip().split(' ')]
front_row_price = [int(x) for x in front_row_price.strip().split(' ')]
front_row_height = [int(x) for x in front_row_height.strip().split(' ')]

# store each tile into lists of tuples
front = list()
back = list()
for i in range(n_tiles_row):
    back.append((i, back_row_price[i], back_row_height[i]))  # tuples of (tile_num, price, height)
    front.append((i, front_row_price[i], front_row_height[i]))

# sort tiles by price first (as the price must be non-descending) then by height descending
back = sorted(back, key=lambda x: (x[1], -x[2]))
front = sorted(front, key=lambda x: (x[1], -x[2]))

# print(back) ==> [(2, 1, 4), (1, 2, 3), (3, 2, 3), (0, 3, 2)]
# print(front) ==> [(3, 1, 3), (1, 1, 2), (0, 2, 2), (2, 2, 1)]

possible_back_tile_order = list()
possible_front_tile_order = list()
for i in range(n_tiles_row):
    if back[i][2] > front[i][2]:  # if next lowest priced back tile is taller than next lowest priced front tile
        possible_back_tile_order.append(back[i][0])
        possible_front_tile_order.append(front[i][0])
    else:
        break

if len(possible_back_tile_order) < n_tiles_row:  # check that all tiles had matching pairs in back and front
    print("impossible")
else:
    print(' '.join([str(x+1) for x in possible_back_tile_order])) 
    print(' '.join([str(x+1) for x in possible_front_tile_order]))