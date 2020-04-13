import svgwrite
import maze_generator as mz


class Svg_Generetor:

    def __init__(self, file_name="temp", show_solution=False,
                 size=1, layers_approx=3, seed=""):
        self.maze = mz.Maze(layers_approx, size, seed)
        self.file_name = file_name
        self.show_solution = show_solution
        self.create_svg()

    def svg_draw(self, x, y, stroke, stroke_width,
                 stroke_opacity, svg_drawing):
        svg_drawing.add(svg_drawing.line(
            x,
            y,
            stroke=stroke,
            stroke_width=stroke_width,
            stroke_opacity=stroke_opacity,
            stroke_linecap="square"
        ))

    def create_svg(self):
        maze_points = self.maze.points
        maze_last_point = abs(self.maze.points[-1][-1])
        maze_solution = self.maze.solution
        maze_seed = self.maze.seed

        if self.file_name != "":
            svg_drawing = svgwrite.Drawing('src/static/data/'+self.file_name+'.svg', profile='full')
        else:
            svg_drawing = svgwrite.Drawing('src/static/data/'+maze_seed+'.svg', profile='full')

        for i in range(len(maze_points)-1):
            ax = maze_points[i][0] + maze_last_point + 2
            ay = maze_points[i][1] + maze_last_point + 2
            bx = maze_points[i+1][0] + maze_last_point + 2
            by = maze_points[i+1][1] + maze_last_point + 2
            self.svg_draw([ax, ay], [bx, by], svgwrite.rgb(5, 5, 5, '%'), 3, 0.99, svg_drawing)
        print(1)
        if self.show_solution:
            for j in range(len(maze_solution)-1):
                cx = maze_solution[j][0] + maze_last_point + 1
                cy = maze_solution[j][1] + maze_last_point + 1
                dx = maze_solution[j+1][0] + maze_last_point + 1
                dy = maze_solution[j+1][1] + maze_last_point + 1
                # if cx == dx:
                #     cy = cy + 1
                #     dy = dy
                # else :
                #     cy = cy
                #     dy = dy + 1
                self.svg_draw([cx, cy], [dx, dy], svgwrite.rgb(10, 30, 10, '%'), 1, 0.7, svg_drawing)
        padding = [(maze_last_point*2)+3, (maze_last_point*2)+3]
        self.svg_draw([0, 0], padding, svgwrite.rgb(5, 5, 5, '%'), 1, 0.0, svg_drawing)
        svg_drawing.save()
