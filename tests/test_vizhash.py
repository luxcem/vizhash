import pytest
import random

from PIL import Image

from vizhash import Vizhash

some_strings = ['', 'some string', '什么什么']
some_sizes = [1, 2, 5, 10]
some_squares = [1, 2, 4, 16]

@pytest.mark.parametrize('seed', some_strings)
def test_init(seed):
    vizhash = Vizhash(seed)
    assert isinstance(vizhash, Vizhash)
    assert isinstance(vizhash.random, random.Random)

@pytest.mark.parametrize('seed', some_strings)
@pytest.mark.parametrize('n', some_sizes)
def test_colors(seed, n):
    vizhash = Vizhash(seed)
    colors = vizhash._get_colors(n)
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
    vizhash = Vizhash(seed, square_size, n)
    im = vizhash.identicon()
    assert isinstance(im, Image.Image)
    assert im.size == (n*square_size, n*square_size)
    assert im.mode == 'RGB'
