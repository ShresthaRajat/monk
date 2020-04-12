import random


class Maze:

    mid = [
        [0, 0], [0, 10], [10, 10], [10, -10], [-10, -10], [-10, 20],
        [20, 20], [20, -20], [-20, -20], [-20, 30], [30, 30],
        [30, -30], [-30, -30]
    ]

    mid_solution = [
        [5, 5], [5, -5], [-5, -5], [-5, 15], [15, 15],
        [15, -15], [-15, -15], [-15, 25], [25, 25],
        [25, -25], [-25, -25]
    ]

    def __init__(self, layer_approx=50, size=5, seed=""):
        self.points = [] + Maze.mid
        self.solution = [] + Maze.mid_solution
        self.layers = 0
        self.seed = seed
        self.color = [(0, 0, 0)]
        self.layer_approx = layer_approx
        self.size = size
        self.generate()

    def draw_layer(self, letter):
        current_layer = self.layers
        x = 10*current_layer
        layers = {
            "A" : (
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
                current_layer+3,
                "A",
                (1, 0, 0),
                [
                    [-(25+x), -(25+x)], [-(25+x), (35+x)],
                    [(35+x), (35+x)], [(35+x), -(35+x)],
                    [-(35+x), -(35+x)], [-(35+x), 0],
                    [-(55+x), 0], [-(55+x), -(55+x)]
                ]
            ),
            "B" : (
                [
                    [-(30+x), -(30+x)], [-(30+x), -5], [-(40+x), -5],
                    [-(40+x), -(40+x)], [-10, -(40+x)], [-10, -(50+x)],
                    [-(50+x), -(50+x)], [-(50+x), (60+x)], [60+x, 60+x],
                    [60+x, -(60+x)], [10, -(60+x)], [10, -(50+x)],
                    [50+x, -(50+x)], [50+x, 50 + x], [-(40+x), 50+x],
                    [-(40+x), 5], [-(30+x), 5], [-(30+x), 40+x],
                    [40+x, 40+x], [40+x, -(40+x)], [0, -(40+x)],
                    [0, -(60+x)], [-(60+x), -(60+x)]
                ],
                current_layer+3,
                "B",
                (0, 1, 0),
                [
                    [-(25+x), -(25+x)], [-(25+x), 0], [-(25+x), (35+x)],
                    [(35+x), (35+x)], [(35+x), -(35+x)],
                    [-5, -(35+x)], [-5, -(55+x)], [-(55+x), -(55+x)]
                ]
            ),
            "C" : (
                [
                    [-(30+x), -(30+x)], [-(30+x), (40+x)],
                    [(40+x), (40+x)], [(40+x), -(40+x)],
                    [-(40+x), -(40+x)], [-(40+x), (50+x)],
                    [(50+x), (50+x)], [(50+x), -(50+x)],
                    [-(50+x), -(50+x)]
                ],
                current_layer+2,
                "C",
                (0.5, 0.5, 0.5),
                [
                    [-(25+x), -(25+x)], [-(25+x), (35+x)], [(35+x), (35+x)],
                    [(35+x), -(35+x)], [-(35+x), -(35+x)],
                    [-(35+x), (45+x)], [(45+x), (45+x)], [(45+x), -(45+x)],
                    [-(45+x), -(45+x)]
                ]
            ),
            "D" : (
                [
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
                current_layer+5,
                "D",
                (0, 0, 1),
                [
                    [-(25+x), -(25+x)], [-(25+x), (35+x)], [-5, (35+x)],
                    [-5, (75+x)], [(75+x), (75+x)], [(75+x), -(75+x)],
                    [-(75+x), -(75+x)]
                ]
            )
        }
        return layers[letter]


    def draw_random(self, letter=""):
        if letter == "":
            letter = random.choice(["A","B","C","D"])
        return self.draw_layer(letter)

    def generate(self):
        n = 0
        if self.seed == "":
            for i in range(self.size):
                (m, n, p, c, s) = self.draw_random()
                self.layers = n
                self.seed = self.seed + p
                self.points = self.points + m
                self.solution = self.solution + s
                self.color.append(c)
                if n > self.layers:
                    break
        else:
            _seed = self.seed
            for layer in _seed:
                (m, n, p, c, s) = self.draw_random(layer)
                self.layers = n
                self.points = self.points + m
                self.solution = self.solution + s
                self.color.append(c)