import pytest
import random

import vizhash.vizhash as vizhash
from PIL import Image

some_strings = ['', 'some string', '什么什么']
some_sizes = [1, 2, 5, 10]
some_squares = [1, 2, 4, 16]

@pytest.mark.parametrize('seed', some_strings)
def test_init(seed):
    vh = vizhash.Vizhash(seed)
    assert isinstance(vh, vizhash.Vizhash)
    assert isinstance(vh.random, random.Random)

@pytest.mark.parametrize('seed', some_strings)
@pytest.mark.parametrize('n', some_sizes)
def test_colors(seed, n):
    vh = vizhash.Vizhash(seed)
    colors = vh._get_colors(n)
    assert isinstance(colors, list)
    assert len(colors) == n
    for i in range(n):
        assert isinstance(colors[i], list)
        assert len(colors[i]) == n
        for j in range(n):
            assert isinstance(colors[i][j], list)
            assert len(colors[i][j]) == 3
            for k in colors[i][j]:
                assert isinstance(k, int)
                assert ( k >= 0 and k <= 255 )

@pytest.mark.parametrize('seed', some_strings)
@pytest.mark.parametrize('n', some_sizes)
@pytest.mark.parametrize('square_size', some_squares)
def test_identicon(seed, square_size, n):
    vh = vizhash.Vizhash(seed, square_size, n)
    im = vh.identicon()
    assert isinstance(im, Image.Image)
    assert im.size == (n*square_size, n*square_size)
    assert im.mode == 'RGB'

@pytest.mark.parametrize('seed', some_strings)
@pytest.mark.parametrize('n', some_sizes)
@pytest.mark.parametrize('square_size', some_squares)
def test_main(seed, n, square_size, tmpdir):
    argv = ['-s', seed,
            '-n', str(n),
            '-S', str(square_size),
            '-f', str(tmpdir.join('tmpfile.png'))
    ]
    args = vizhash.parse_args(argv)
    assert args.seed == seed
    assert args.n == n
    assert args.size == square_size
    assert args.filename == str(tmpdir.join('tmpfile.png'))
    vizhash.main(args)
