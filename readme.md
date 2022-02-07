Gofore › Junior-developer-assignment


Help the friendly robot (🤖) find its way home? The rules are following
- Count how many steps it takes to reach (E)
- Robot starts at character S
- Starting direction is always up
- If the robot is about to hit an obstacle, it should turn right before it and move forward.
- If the robot enters into S character after the start, treat S as a dot, so count it as a step.
(E) character is counted as step
- Make a note of the MAP_CODE in the first line, you'll need it in answer


```txt
2307172
##################################################
#........................#.......................#
#..#............................#..#.............#
#.............................#................#.#
#..................#.......#.....................#
#........#..............#........#...............#
#.......................................#........#
#.................................#..............#
#......................................#.........#
#................................................#
#.........#.......#................#.............#
#....#........#.................#....#...........#
#.......................................#........#
#................................................#
#................#..#............................#
#..................#.............#..........#....#
#.......#.................#.....................##
#.................#......................#.......#
#...............#.................#..............#
#...............................#..............#.#
#.#..............................................#
#...#.............##...........#.................#
#............#......#.....S..#...................#
#.......................#........................#
#................#.....................#.........#
#......................#.........................#
#....#...#.................................#.....#
#..........E#.............#.............#.....#..#
#...#...............................#............#
##################################################
```


### Steps
- [x] Find S and E
- [x] isFree function: check we are inside the lines, inside single line and that spot is not blocked (#)
- [x] turnRight function: to change direction
- [x] moveForward function with recursion to find path to END (E)