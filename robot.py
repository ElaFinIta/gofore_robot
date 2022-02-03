line_count = 30
dot_count = 50
direction = 'up'

def isFree(lines, x, y):
    # print(x,y)
    # print(lines[x][y])
    if (x >= 0) & (y >= 0) & (x < line_count) & (y < dot_count) & (lines[x][y] != '#'):
        return True
    else:
        return False

def turnRight(direction):
    if direction == 'up':
        return 'R'
    if direction == 'R':
        return 'down'
    if direction == 'down':
        return 'L'
    if direction == 'L':
        return 'up'

def moveForward(lines, x, y, direction, steps):
    # print(steps)
    # print('direction:', direction)
    # base case: E found
    if lines[x][y] == 'E':
        print('total steps:', steps)
        return True

    if direction == 'up':
        if isFree(lines, x-1, y):
            steps += 1
            # print('step n:', steps)
            if moveForward(lines, x-1, y, direction, steps):
                return True
        else:
            direction = turnRight(direction)
            steps += 1
            if moveForward(lines, x, y+1, direction, steps):
                return True

    if direction == 'R':
        if isFree(lines, x, y+1):
            steps += 1
            # print('step n:', steps)
            if moveForward(lines, x, y+1, direction, steps):
                return True
        else:
            direction = turnRight(direction)
            steps += 1
            if moveForward(lines, x+1, y, direction, steps):
                return True

    if direction == 'down':
        if isFree(lines, x+1, y):
            steps += 1
            # print('step n:', steps)
            if moveForward(lines, x+1, y, direction, steps):
                return True
        else:
            direction = turnRight(direction)
            steps += 1
            if moveForward(lines, x, y-1, direction, steps):
                return True

    if direction == 'L':
        if isFree(lines, x, y-1):
            steps += 1
            # print('step n:', steps)
            if moveForward(lines, x, y-1, direction, steps):
                return True
        else:
            direction = turnRight(direction)
            steps += 1
            if moveForward(lines, x-1, y, direction, steps):
                return True


with open('field3275647.txt', 'r') as f:
    text = f.readlines()
    lines = text[1:]

    # S and E coordinates initialized with zero
    # s_i = 0
    # s_j = 0
    # e_i = 0
    # e_j = 0

    # find S and E coordinates
    for i, l in enumerate(lines):
        if 'S' in l:
            for j, step in enumerate(l):
                if step == 'S':
                    s_i = i
                    s_j = j
                    # print('S found in line {}, index {}'.format(i, j))
        # if 'E' in l:
        #     for j, step in enumerate(l):
        #         if step == 'E':
        #             e_i = i
        #             e_j = j
                    # print('E found in line {}, index {}'.format(i, j))

    # print(s_i, s_j)
    # print(lines[s_i][s_j])
    # print(e_i, e_j)
    # print(lines[e_i][e_j])
    moveForward(lines, s_i, s_j, 'up', steps=0)



