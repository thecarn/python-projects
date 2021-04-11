import random
import curses


def endGame():
    print('close game')

def runGame():
    print('game running')
    s = curses.initscr()
    curses.curs_set(0)
    sh, sw = s.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(350)

    print('height: ', sh)
    print('width: ', sw)

    snk_x = sw//2
    snk_y = sh//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2],
        [snk_y, snk_x-3]
    ]

    food = [sh//2, sw//2]
    w.addch(food[0], food[1], curses.ACS_PI)
    key = curses.KEY_RIGHT
    i = 0
    while True:
        i += 1
        print('frame: ', i)
        print('snake position: ', snake)
        next_key = w.getch()
        key = key if next_key == -1 else next_key
        
        if snake[0][0] == sh:
            print('hit the floor, you lose!')
            curses.endwin()
            quit()
        elif snake[0][0] == -1:
            print('hit the ceiling, you lose!')
            curses.endwin()
            quit()
        elif snake[0][1] == -1:
            print('hit the left wall, you lose!')
            curses.endwin()
            quit()
        elif snake[0][1] == sw:
            print('hit the right wall, you lose!')
            curses.endwin()
            quit()
        elif snake[0] in snake[1:]:
            print('ran into snake body, you lose!')
            curses.endwin()
            quit()
    

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

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
        else:
            tail = snake.pop()
            try:
                w.addch(tail[0], tail[1], ' ')
            except:
                print('addch error')
            
            
            
        if snake[0][0] == sh:
            print('hit the floor, you lose!')
            curses.endwin()
            quit()
        elif snake[0][0] == -1:
            print('hit the ceiling, you lose!')
            curses.endwin()
            quit()
        elif snake[0][1] == -1:
            print('hit the left wall, you lose!')
            curses.endwin()
            quit()
        elif snake[0][1] == sw:
            print('hit the right wall, you lose!')
            curses.endwin()
            quit()
        elif snake[0] in snake[1:]:
            print('ran into snake body, you lose!')
            curses.endwin()
            quit()
    
        try:
            w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        except:
            print('addch error')
        
    


def main():
    print('main')
    runGame()

main()
    