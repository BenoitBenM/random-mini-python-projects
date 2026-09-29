from random import randint
import curses
import time


def coordinates_to_index(x: int, y: int) -> int:
    return (x + (WIDTH+1)*y)

def update_player_and_arena(arena: list, player_pos: list, apple_pos:list, direction: str):
    if direction in ["z", "q", "s", "d"]:        # Update snake body
        arena[coordinates_to_index(player_pos[-1][0], player_pos[-1][1])] = "🟫"

        # Add body part if apple eaten 
        if player_pos[0] == apple_pos:
            player_pos.append(player_pos[-1].copy())
            apple_pos = [randint(0, WIDTH-1), randint(0, HEIGHT-1)]
            arena[coordinates_to_index(apple_pos[0], apple_pos[1])] = "🍏"
        # print(str(player_pos) + " : added a body part")


        # Update old body parts
        print(str(player_pos) + " : old body")
        for i in range(len(player_pos) - 1, 0, -1):
            player_pos[i] = player_pos[i-1].copy()
        print(str(player_pos) + " : updated body")

        # Update head
        if direction == "z":
            player_pos[0][1] -= 1
        elif direction == "q":
            player_pos[0][0] -= 1
        elif direction == "s":
            player_pos[0][1] += 1
        elif direction == "d":
            player_pos[0][0] += 1
        print(str(player_pos) + " : updated head")

        for i in range(0, len(player_pos)):
            arena[coordinates_to_index(player_pos[i][0], player_pos[i][1])] = "🟥"

    return arena, player_pos, apple_pos

def game(stdscr, arena, player_pos, apple_pos):
    stdscr.nodelay(True)  # don't wait for input
    direction = "d"
    while True:
        key = stdscr.getch()
        if key == ord("z"):
                direction = "z"
        elif key == ord("q"):
            direction = "q"
        elif key == ord("s"):
            direction = "s"
        elif key == ord("d"):
            direction = "d"
        
        arena, player_pos, apple_pos = update_player_and_arena(arena, player_pos, apple_pos, direction)
        if player_pos[0] in player_pos[1:] or player_pos[0][0] in [-1, WIDTH] or player_pos[0][1] in [-1, HEIGHT]:
            return 
        stdscr.clear()
        stdscr.addstr(0, 0, "".join(arena))
        stdscr.refresh()
        time.sleep(0.1)


# Initial arena setup
arena = []
WIDTH = 15
HEIGHT = 15

for i in range(HEIGHT):
    for k in range(WIDTH):
        arena.append("🟫")
    arena.append("\n")

# Initial player and apple position setup
player_pos = [[0, 0]]
apple_pos = [randint(5, WIDTH-1), randint(5, HEIGHT-1)]


arena[coordinates_to_index(player_pos[0][0], player_pos[0][1])] = "🟥"
arena[coordinates_to_index(apple_pos[0], apple_pos[1])] = "🍏"

print("".join(arena))

# Game
curses.wrapper(game, arena, player_pos, apple_pos)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n###################################################\n###################################################\n###################################################\n###################################################\n######### # # # # YOU LOSE LOSER! # # # # #########\n###################################################\n###################################################\n###################################################\n###################################################\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")