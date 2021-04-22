import random
import curses

'''
TODO:
1: ADD FASTER SPEED AS SNAKE GETS LONGER
2: CHANGE APPEARANCE
3: GET RID OF GRAPHICAL BUG
4: GET RID OF WIDTH OF SNAKE ISSUE WHEN MOVING UP/DOWN VS MOVING LEFT/RIGHT
5: MAKE GAME MORE INTERESTING IN SOME WAY, ADD AN AI SNAKE THAT COMPETES OR SOMETHING LOL
6: ADD POINTS
7: INCREASE GROWTH RATE
'''
def runGame():
    print('game running')
    s = curses.initscr()
    curses.curs_set(0)
    sh, sw = s.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(1000)

    print('height: ', sh)
    print('width: ', sw)

    snk_x = sw//4
    snk_y = sh//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2],
        [snk_y, snk_x-3],
        [snk_y, snk_x-4],

    ]

    food = [sh//2, sw//2]
    w.addch(food[0], food[1], curses.ACS_PI)
    key = curses.KEY_RIGHT
    currentDirection = curses.KEY_RIGHT
    i = 0
    points = 0
    while True:
        i += 1
        print('frame: ', i)
        print('snake position: ', snake)
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        

        checkSnake(snake, sh, sw, points)

        new_head = [snake[0][0], snake[0][1]]

        new_head, key, currentDirection = generateMovementInfo(new_head, key, currentDirection)

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh-1),
                    random.randint(1, sw-1)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
            points += 100
        else:
            
            tail = snake.pop()
            try:
                w.addch(tail[0], tail[1], ' ')
                
            except:
                print('addch error')
        checkSnake(snake, sh, sw, points)
        try:
            w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        except:
            print('addch error')
        
def checkSnake(snake, sh, sw, points):
    print('check snake')
    if snake[0][0] == sh:
        print('hit the floor, you lose!')
        print('score: ', points)
        curses.endwin()
        quit()
    elif snake[0][0] == -1:
        print('hit the ceiling, you lose!')
        print('score: ', points)
        curses.endwin()
        quit()
    elif snake[0][1] == -1:
        print('hit the left wall, you lose!')
        print('score: ', points)
        curses.endwin()
        quit()
    elif snake[0][1] == sw:
        print('hit the right wall, you lose!')
        print('score: ', points)
        curses.endwin()
        quit()
    elif snake[0] in snake[1:]:
        print('ran into snake body, you lose!')
        print('score: ', points)
        curses.endwin()
        quit()

def generateMovementInfo(new_head, key, currentDirection):
    print('move snake')
    
    if currentDirection == curses.KEY_RIGHT:

        if key == curses.KEY_LEFT:
            #continue going right edgecase
            new_head[1] += 1
            key = currentDirection
            return new_head, key, currentDirection

        if key == curses.KEY_DOWN:
            new_head[0] += 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_UP:
            new_head[0] -= 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_RIGHT:
            new_head[1] += 1
            currentDirection = key
            return new_head, key, currentDirection

    elif currentDirection == curses.KEY_LEFT:

        if key == curses.KEY_LEFT:
            new_head[1] -= 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_DOWN:
            new_head[0] += 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_UP:
            new_head[0] -= 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_RIGHT:
            #continue going left edgecase
            new_head[1] -= 1
            key = curses.KEY_LEFT
            return new_head, key, currentDirection

    elif currentDirection == curses.KEY_UP:

        if key == curses.KEY_LEFT:
            new_head[1] -= 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_DOWN:
            #continue going up edgecase
            new_head[0] -= 1
            key = currentDirection
            return new_head, key, currentDirection

        if key == curses.KEY_UP:
            new_head[0] -= 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_RIGHT:
            new_head[1] += 1
            currentDirection = key
            return new_head, key, currentDirection

    elif currentDirection == curses.KEY_DOWN:

        if key == curses.KEY_LEFT:
            new_head[1] -= 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_DOWN:
            new_head[0] += 1
            currentDirection = key
            return new_head, key, currentDirection

        if key == curses.KEY_UP:
            #continue going down edgecase
            new_head[0] += 1
            key = currentDirection
            return new_head, key, currentDirection

        if key == curses.KEY_RIGHT:
            new_head[1] += 1
            currentDirection = key
            return new_head, key, currentDirection





def main():
    print('main')
    #var = input('Enter game mode: ')
    runGame()

main()
    