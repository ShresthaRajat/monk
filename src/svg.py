import svgwrite
import maze_generator as mz

class


def svg(x, y, stroke, stroke_width, stroke_opacity, svg_drawing):
    svg_drawing.add(svg_drawing.line(
        x,
        y,
        stroke=stroke,
        stroke_width=stroke_width,
        stroke_opacity=stroke_opacity,
        stroke_linecap="square"
    ))


def create_svg(maze_points, maze_last_point, maze_solution, seed, t=False):
    svg_drawing = svgwrite.Drawing('src/static/data/'+seed+'.svg', profile='full')
    # svg_drawing = svgwrite.Drawing('src/static/test.svg', profile='tiny')
    for i in range(len(maze_points)-1):
        ax = maze_points[i][0] + maze_last_point + 2
        ay = maze_points[i][1] + maze_last_point + 2
        bx = maze_points[i+1][0] + maze_last_point + 2
        by = maze_points[i+1][1] + maze_last_point + 2
        svg([ax, ay], [bx, by], svgwrite.rgb(5, 5, 5, '%'), 3, 0.99, svg_drawing)
    if t:
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
            svg([cx, cy], [dx, dy], svgwrite.rgb(10, 30, 10, '%'), 1, 0.7, svg_drawing)
        padding = [(maze_last_point*2)+3, (maze_last_point*2)+3]
        svg([0, 0], padding, svgwrite.rgb(5, 5, 5, '%'), 1, 0.0, svg_drawing)
        print(svg_drawing)
    svg_drawing.save()


maze = mz.Maze(3, 4)
maze_points = maze.points
maze_solution = maze.solution
maze_last_point = abs(maze_points[-1][-1])
maze_seed = maze.seed

create_svg(maze_points, maze_last_point, maze_solution, maze_seed, True)
