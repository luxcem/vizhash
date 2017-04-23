from setuptools import setup
__version__ = '1.4.2'

setup(
    name='vizhash',
    packages=['vizhash'],
    version=__version__,
    description=('Python Visual Hash,'
                 'generate a visual random image associated with a string.'),
    author='luxcem',
    author_email='a@luxcem.fr',
    url='https://github.com/luxcem/vizhash',
    download_url='https://github.com/luxcem/vizhash/tarball/{}'.format(
        __version__),
    keywords='visual hash vizhash random maze identicon',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires=['Pillow'],
    entry_points={
        'console_scripts': [
            'vizhash = vizhash.vizhash:entrypoint',
        ],
    },
    tests_require=['Pillow', 'pytest', 'pytest-cov'])
