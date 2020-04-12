import svgwrite
import maze_generator as mz


def svg(x, y, stroke, stroke_width, stroke_opacity, dwg):
    dwg.add(dwg.line(
        x, 
        y, 
        stroke=stroke, 
        stroke_width=stroke_width, 
        stroke_opacity=stroke_opacity,
        stroke_linecap="square"
        ))


def create_svg(maze_points, maze_last_point, maze_solution, seed, t=False):
    # dwg = svgwrite.Drawing('data/'+seed+'.svg', profile='full')
    dwg = svgwrite.Drawing('src/static/test.svg', profile='tiny')
    for i in range(len(maze_points)-1):
        ax = maze_points[i][0] + maze_last_point + 2
        ay = maze_points[i][1] + maze_last_point + 2
        bx = maze_points[i+1][0] + maze_last_point + 2
        by = maze_points[i+1][1] + maze_last_point + 2
        svg([ax, ay], [bx, by], svgwrite.rgb(5, 5, 5, '%'), 3, 0.99, dwg)
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
            svg([cx, cy], [dx, dy], svgwrite.rgb(10, 30, 10, '%'), 1, 0.7, dwg)
        padding = [(maze_last_point*2)+3, (maze_last_point*2)+3]
        svg([0,0], padding, svgwrite.rgb(5, 5, 5, '%'), 1, 0.0, dwg)
    dwg.save()


maze = mz.Maze(3, 4)
maze_points = maze.points
maze_solution = maze.solution
maze_last_point = abs(maze_points[-1][-1])
maze_seed = maze.seed

create_svg(maze_points, maze_last_point, maze_solution, maze_seed, True)
