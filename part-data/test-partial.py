from functools import partial
import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)


if __name__ == "__main__":
    points = [(1, 2), (3, 4), (7, 8), (5, 6)]
    pt = (5, 6)
    points.sort(key=partial(distance, pt))
    print(points)
