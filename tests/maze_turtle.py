import turtle as tt
import time
import src.maze_generator.maze as mz


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
    new_maze = mz.Maze(20, 3)
    drawseg(new_maze.points)
    tt.pensize(1)
    tt.pencolor(0.7, 0, 0)
    time.sleep(1.5)
    tt.speed(2)
    drawseg(new_maze.solution)
    print("points: ", new_maze.points)
    print("solution: ", new_maze.solution)
    print("layer-app: ", new_maze.layer_approx)
    print("layers: ", new_maze.layers)
    print("size: ", new_maze.size)
    print("seed: ", new_maze.seed)
    tt.exitonclick()


if __name__ == "__main__":
    main()
