height = 30
width = 50
direction = 'up'

def isFree(lines, x, y):
    # check position is inside the field and not on obstacle
    if (x >= 0) & (y >= 0) & (x < height) & (y < width) & (lines[x][y] != '#'):
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
    # base case: E found, end of recursion
    if lines[x][y] == 'E':
        print('total steps:', steps)
        return True

    if direction == 'up':
        if isFree(lines, x-1, y):
            steps += 1
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
            if moveForward(lines, x, y-1, direction, steps):
                return True
        else:
            direction = turnRight(direction)
            steps += 1
            if moveForward(lines, x-1, y, direction, steps):
                return True


with open('field.txt', 'r') as f:
    text = f.readlines()
    lines = text[1:]

    # find S coordinates
    for i, l in enumerate(lines):
        if 'S' in l:
            for j, step in enumerate(l):
                if step == 'S':
                    s_i = i
                    s_j = j

    moveForward(lines, s_i, s_j, 'up', steps=0)



