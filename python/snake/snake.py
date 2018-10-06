import curses, time
import collections

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.clear()
    maxy, maxx = stdscr.getmaxyx()
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    idx = 3
    path = collections.deque()
    y,x = 0,0
    while True:
        c = stdscr.getch()
        if c==ord('w'):
            idx = 0
        elif c==ord('s'):
            idx = 1
        elif c==ord('a'):
            idx = 2
        elif c==ord('d'):
            idx = 3
        elif c==ord('q'):
            break
        path.append([y,x])
        stdscr.addch(y,x,curses.ACS_BLOCK)
        y, x = y+dirs[idx][0], x+dirs[idx][1]
        if x>=0 and x<maxx and y>=0 and y<maxy:
            if len(path)==5:
                tail = path.popleft()
                stdscr.addch(tail[0],tail[1], ' ')
                stdscr.move(y,x)
            stdscr.refresh()
            time.sleep(0.1)
            continue
        break


curses.wrapper(main)
