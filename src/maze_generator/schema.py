import src.maze_generator.maze as mz
import src.maze_generator.maze_svg as sv
import graphene
from graphene import Int, Float


class MazeType(graphene.ObjectType):
    """A Simple mazetype object"""
    points = graphene.List(graphene.List(Int), description="The list of the co-ordinates of the lines to be generated")
    size = graphene.Int(description="The size of the maze")
    seed = graphene.String(description="The seed of the maze")
    color = graphene.List(graphene.List(Float), description="The list of colours of the layers Comming Soon!")
    solution = graphene.List(graphene.List(Int), description="The list of points of the solution")
    layers = graphene.Int(description="The numbers of layer of the maze")


class MazeSvgType(graphene.ObjectType):
    size = graphene.Int(description="The size of the maze")
    layers = graphene.Int(description="The numbers of layer of the maze")
    svg = graphene.String(description="The SVG code to be injected")
    seed = graphene.String(description="The seed of the maze")
    fileName = graphene.String(description="The filename of the maze created")


class MazeQuery(graphene.ObjectType):
    """Various queries related to generating or retreving mazes"""
    get_maze = graphene.Field(
        MazeType,
        size=graphene.Int(description="The size of the maze to be to generated"),
        color=graphene.Boolean(description="The parameter to color the layers of the maze (comming Soon!)"),
        layerApprox=graphene.Int(description="The approximate numbers of layers for the maze to be generated"),
        seed=graphene.String(description="The Seed to generate the maze"),
        description="Generates the maze according to the size or seed"
    )

    get_svg = graphene.Field(
        MazeSvgType,
        size=graphene.Int(description="The size of the maze to be to generated"),
        layerApprox=graphene.Int(description="The approximate numbers of layers for the maze to be generated"),
        seed=graphene.String(description="The Seed to generate the maze"),
        showSolution=graphene.Boolean(description="The parameter to render the solution of the maze"),
        fileName=graphene.String(description="The parameter to set the filename of the maze"),
        saveFile=graphene.Boolean(description="The parameter to weather to save the maze"),
        color=graphene.Boolean(description="The parameter to color the layers of the maze (comming Soon!)"),
        description="Generates the maze according to the size or seed"
    )

    def resolve_get_svg(root, info, size=7, layerApprox=50, seed="", showSolution=False, saveFile=False,
                        fileName="temp", color=False):
        if seed != "":
            svg_maze = sv.Svg_generator(fileName, showSolution, 0, 0, seed)
        else:
            svg_maze = sv.Svg_generator(fileName, showSolution, size, layerApprox, "")
        svg_string = svg_maze.read_svg()
        return_dict = {
            "size": svg_maze.maze.size,
            "layer": svg_maze.maze.layers,
            "svg": svg_string,
            "seed": svg_maze.maze.seed,
            "fileName": svg_maze.file_name
        }
        return return_dict

    def resolve_get_maze(root, info, layerApprox=1, color=False, size=4, seed=""):
        if seed != "":
            maze = mz.Maze(0, 0, seed)
        else:
            maze = mz.Maze(layerApprox, size)
        maze_package = {
            "points": maze.points,
            "solution": maze.solution,
            "layers": maze.layers,
            "size": maze.size,
            "seed": maze.seed,
            "color": maze.color
        }
        return maze_package


MazeSchema = graphene.Schema(query=MazeQuery)
