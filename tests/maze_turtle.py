import turtle as tt
import time
import src.maze as maze


def drawseg(points):
    tt.speed(0)
    tt.pu()
    tt.goto(points[0][0], points[0][1])
    tt.pd()
    for a, b in points[1:]:
        tt.goto(a, b)


def main():
    tt.reset()
    tt.pensize(3)
    tt.speed(0)
    new_maze = maze.Maze(40, False, 8)
    drawseg(new_maze.points)
    tt.pensize(1)
    tt.pencolor(0.7, 0, 0)
    time.sleep(1.5)
    tt.speed(2)
    drawseg(new_maze.solution)
    tt.exitonclick()

    print(new_maze.seed)
    print(new_maze.color, new_maze.layers, new_maze.size, new_maze.size_limit)
    print(new_maze.points)
    print(new_maze.solution)
    print(new_maze.color_list)
    print()


if __name__ == "__main__":
    main()
