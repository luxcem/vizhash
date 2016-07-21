from PIL import Image, ImageDraw
import random
import copy

def explore(i, j, cases, colors):
    cases[i][j] = True

    cells = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
    random.shuffle(cells)
    for (x, y) in cells:
        if cases[x][y]: continue
        color = copy.copy(colors[i][j])
        for k in range(3):
            color[k] += random.gauss(0, random.randint(3,20))
            color[k] = int(max(0, min(color[k], 255)))
        colors[x][y] = color
        explore(x, y, cases, colors)


def identicon(square_size = 16, n = 16):
    size = (square_size * n, square_size * n)

    im = Image.new('RGB',size)
    d = ImageDraw.Draw(im)

    cases = [[False] * n + [True] for _ in range(n)] + [[True] * (n + 1)]
    colors = [[None] * n for _ in range(n)]


    i, j = random.randrange(n), random.randrange(n)
    colors[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0,255)]
    explore(i, j, cases, colors)

    for i in range(n):
        for j in range(n):
            coordinates = [i * square_size, j * square_size, (i + 1) * square_size, (j + 1) * square_size]
            d.rectangle(coordinates, tuple(colors[i][j]))
    return im

if __name__ == '__main__':
    import argparse,sys
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--seed", default=None)
    parser.add_argument("-n", type=int, help="Number of blocks (default : 16)", default=16)
    parser.add_argument("-S", "--size", type=int, help="Block size (default :16)", default= 16)
    parser.add_argument("-f", "--filename", help="Output", default=None)
    args = parser.parse_args()
    sys.setrecursionlimit(args.n * args.n)

    if args.seed:
        random.seed(args.seed)

    im = identicon(args.size, args.n)
    if args.filename:
        im.save(args.filename)
    else:
        im.show()
