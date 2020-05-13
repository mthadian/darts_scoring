import math


def scores(x, y):
    try:
        inner_radius = 1
        middle_radius = 5
        outer_radius = 10
        points = 0

        # calculate the line length from (0,0) to point hit using pythagoras' theoremn
        line_length = math.sqrt(x ** 2 + y ** 2)

        if line_length <= inner_radius:
            points = 10
        elif inner_radius < line_length <= middle_radius:
            points = 5
        elif middle_radius < line_length <= outer_radius:
            points = 1
        elif line_length > outer_radius:
            points = 0

        print("scores(", x, ",", y, ")")
        print(points)
        print("--------------------------------------------")

        return points

    except ValueError as Argument:
        print("An error occurred" + Argument)


scores(0, 0)
scores(0, 4)
scores(6, 8)
scores(6, 9)
