import turtle as tt
import random
import time


class Maze:

    mid = [[0, 0], [0, 10], [10, 10], [10, -10], [-10, -10], [-10, 20],
           [20, 20], [20, -20], [-20, -20], [-20, 30], [30, 30],
           [30, -30], [-30, -30]
           ]

    mid_solution = [[5, 5], [5, -5], [-5, -5], [-5, 15], [15, 15],
                    [15, -15], [-15, -15], [-15, 25], [25, 25],
                    [25, -25], [-25, -25]
                    ]

    def __init__(self, size_limit=30, color=True, layers=4):
        self.points = [] + Maze.mid
        self.solution = [] + Maze.mid_solution
        self.size_limit = size_limit
        self.color = color
        self.seed = ""
        self.color_list = [(0, 0, 0)]
        self.layers = layers
        self.size = 0
        self.generate()

    def draw_random(self):
        li = self.size
        x = 10*self.size
        random_list = [
            (
                [
                    [-(30+x), -(30+x)], [-(30+x), (40+x)], [-5, (40+x)],
                    [-5, (50+x)], [-(40+x), (50+x)], [-(40+x), 5],
                    [-(50+x), 5], [-(50+x), (60+x)], [(60+x), (60+x)],
                    [(60+x), 5], [(50+x), 5], [(50+x), (50+x)],
                    [5, (50+x)], [5, (40+x)], [(40+x), (40+x)],
                    [(40+x), -(40+x)], [10, -(40+x)], [10, -(50+x)],
                    [(50+x), -(50+x)], [(50+x), -5], [(60+x), -5],
                    [(60+x), -(60+x)], [0, -(60+x)], [0, -(40+x)],
                    [-(40+x), -(40+x)], [-(40+x), -5], [-(50+x), -5],
                    [-(50+x), -(50+x)], [-10, -(50+x)], [-10, -(60+x)],
                    [-(60+x), -(60+x)]
                ],
                li+3,
                "A",
                (1, 0, 0),
                [
                    [-(25+x), -(25+x)], [-(25+x), (35+x)],
                    [(35+x), (35+x)], [(35+x), -(35+x)],
                    [-(35+x), -(35+x)], [-(35+x), 0],
                    [-(55+x), 0], [-(55+x), -(55+x)]
                ]
            ),
            ([
                [-(30+x), -(30+x)], [-(30+x), -5], [-(40+x), -5],
                [-(40+x), -(40+x)], [-10, -(40+x)], [-10, -(50+x)],
                [-(50+x), -(50+x)], [-(50+x), (60+x)], [60+x, 60+x],
                [60+x, -(60+x)], [10, -(60+x)], [10, -(50+x)],
                [50+x, -(50+x)], [50+x, 50 + x], [-(40+x), 50+x],
                [-(40+x), 5], [-(30+x), 5], [-(30+x), 40+x],
                [40+x, 40+x], [40+x, -(40+x)], [0, -(40+x)],
                [0, -(60+x)], [-(60+x), -(60+x)]
            ],
                li+3,
                "B",
                (0, 1, 0),
                [
                    [-(25+x), -(25+x)], [-(25+x), 0], [-(25+x), (35+x)],
                    [(35+x), (35+x)], [(35+x), -(35+x)],
                    [-5, -(35+x)], [-5, -(55+x)], [-(55+x), -(55+x)]
            ]
            ),
            ([
                [-(30+x), -(30+x)], [-(30+x), (40+x)],
                [(40+x), (40+x)], [(40+x), -(40+x)],
                [-(40+x), -(40+x)], [-(40+x), (50+x)],
                [(50+x), (50+x)], [(50+x), -(50+x)],
                [-(50+x), -(50+x)]
            ],
                li+2,
                "C",
                (0.5, 0.5, 0.5),
                [
                    [-(25+x), -(25+x)], [-(25+x), (35+x)], [(35+x), (35+x)],
                    [(35+x), -(35+x)], [-(35+x), -(35+x)],
                    [-(35+x), (45+x)], [(45+x), (45+x)], [(45+x), -(45+x)],
                    [-(45+x), -(45+x)]
            ]
            ),
            ([
                [-(30+x), -(30+x)], [-(30+x), 0], [-(60+x), 0],
                [-(60+x), -(60+x)], [-10, -(60+x)], [-10, -(50+x)],
                [-(50+x), -(50+x)], [-(50+x), -10], [-(40+x), -10],
                [-(40+x), -(40+x)], [0, -(40+x)], [0, -(60+x)],
                [(60+x), -(60+x)], [(60+x), -10], [(50+x), -10],
                [(50+x), -(50+x)], [10, -(50+x)], [10, -(40+x)],
                [(40+x), -(40+x)], [(40+x), (40+x)], [0, (40+x)],
                [0, (70+x)], [(70+x), (70+x)], [(70+x), 10],
                [(60+x), 10], [(60+x), (60+x)], [10, (60+x)],
                [10, (50+x)], [(50+x), (50+x)], [(50+x), 0],
                [(70+x), 0], [(70+x), -(70+x)], [-(70+x), -(70+x)],
                [-(70+x), (80+x)], [-20, (80+x)], [-20, (70+x)],
                [-(60+x), (70+x)], [-(60+x), 10], [-(50+x), 10],
                [-(50+x), (60+x)], [-20, (60+x)], [-20, (50+x)],
                [-(40+x), (50+x)], [-(40+x), 10], [-(30+x), 10],
                [-(30+x), (40+x)], [-10, (40+x)], [-10, (80+x)],
                [(80+x), (80+x)], [(80+x), -(80+x)], [-(80+x), -(80+x)]
            ],
                li+5,
                "D",
                (0, 0, 1),
                [
                    [-(25+x), -(25+x)], [-(25+x), (35+x)], [-5, (35+x)],
                    [-5, (75+x)], [(75+x), (75+x)], [(75+x), -(75+x)],
                    [-(75+x), -(75+x)]
            ]
            )
        ]
        return random.choice(random_list)

    def generate(self):
        n = 0
        for i in range(self.layers):
            (m, n, p, c, s) = self.draw_random()
            print(n, p, c)
            self.size = n
            self.seed = self.seed + p
            self.points = self.points + m
            self.solution = self.solution + s
            if self.color:
                self.color_list = self.color_list + s
            if n > self.size_limit:
                break


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
    new_maze = Maze(40, False, 8)
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
