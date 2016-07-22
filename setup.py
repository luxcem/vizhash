from distutils.core import setup
setup(
    name = 'vizhash',
    packages = ['vizhash'],
    version = '1.1.0',
    description = 'Python Visual Hash, generate a visual random image associated with a string.',
    author = 'luxcem',
    author_email = 'a@luxcem.fr',
    url = 'https://github.com/luxcem/vizhash',
    download_url = 'https://github.com/luxcem/vizhash/tarball/1.1.0',
    keywords = ['visual hash', 'vizhash', 'random', 'maze'],
    classifiers = [],
    install_requires=[
        "Pillow"
    ],
)
