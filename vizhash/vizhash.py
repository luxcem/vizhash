import sys
import argparse
import hashlib
import copy

from random import Random

from PIL import Image, ImageDraw


class Vizhash:

    def __init__(self, data, square_size=16, n=16):
        self.square_size = square_size
        self.n = n
        # Use the sha256 digest of the data to avoid collision on the
        # random generator
        seed = hashlib.sha256(data.encode("utf-8")).hexdigest()
        self.random = Random(seed)

    def _explore(self, i, j, cases, colors):
        """Maze generation algorithm"""
        cases[i][j] = True

        cells = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
        self.random.shuffle(cells)
        for (x, y) in cells:
            if cases[x][y]:
                continue
            color = copy.copy(colors[i][j])
            for k in range(3):
                color[k] += self.random.gauss(0, self.random.randint(3, 20))
                color[k] = int(max(0, min(color[k], 255)))
            colors[x][y] = color
            self._explore(x, y, cases, colors)

    def _get_colors(self, n):
        cases = [[False] * n + [True] for _ in range(n)] + [[True] * (n + 1)]
        colors = [[None] * n for _ in range(n)]

        i, j = self.random.randrange(n), self.random.randrange(n)
        colors[i][j] = [
            self.random.randint(0, 255),
            self.random.randint(0, 255),
            self.random.randint(0, 255)
        ]
        self._explore(i, j, cases, colors)
        return colors

    def identicon(self):
        n = self.n
        colors = self._get_colors(n)
        size = (self.square_size * n, self.square_size * n)

        im = Image.new('RGB', size)
        d = ImageDraw.Draw(im)

        for i in range(n):
            for j in range(n):
                coordinates = [
                    i * self.square_size,
                    j * self.square_size,
                    (i + 1) * self.square_size,
                    (j + 1) * self.square_size
                ]
                d.rectangle(coordinates, tuple(colors[i][j]))
        return im


def main(args):
    vizhash = Vizhash(args.seed, args.size, args.n)
    # Set recursion limit to avoid maximum recursion depth exceeded
    # sys.setrecursionlimit(max(args.n * args.n, 64))
    im = vizhash.identicon()
    if args.filename:
        im.save(args.filename)
    else:
        im.show()


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--seed", default="")
    parser.add_argument(
        "-n", type=int, help="Number of blocks (default : 16)", default=16)
    parser.add_argument("-S", "--size", type=int,
                        help="Block size (default :16)", default=16)
    parser.add_argument("-f", "--filename", help="Output", default=None)
    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))
