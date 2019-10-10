# @Author Gansaikhan Shur
# Another Brick in the Wall (https://open.kattis.com/problems/anotherbrick)
# samples/1.in has been used in this example
import sys

data = []
for i in sys.stdin:
    data.append(i)

data = [line.rstrip('\n') for line in data if line]
height, width, num_bricks = map(int, data[0].split())
width_bricks = data[1].split()
# print(str(height), str(type(height))) ==> (( 2 <class 'int'> ))
# print(str(width), str(type(width))) ==>  (( 10 <class 'int'> ))
# print(str(num_bricks), str(type(num_bricks))) ==> (( 7 <class 'int'> ))
# print(str(width_bricks), str(type(width_bricks))) ==> (( ['5', '5', '5', '5', '5', '5', '5'] <class 'list'> ))


def place_brick(h, w, n_bricks, w_bricks):
    curr_heigth = 0
    cur_length = 0

    for brick in w_bricks:
        cur_length += int(brick)
        # fits thus increments the height
        if cur_length == w and curr_heigth != h:
            curr_heigth += 1
            cur_length = 0
        # too wide to place bricks
        elif cur_length > w:
            return False

        if curr_heigth == h:
            return True

    return False


def print_result(isPossible):
    print("YES" if isPossible else "NO")


print_result(place_brick(height, width, num_bricks, width_bricks))
