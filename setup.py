from setuptools import find_packages, setup


setup(
    name='adventofcode',
    use_scm_version=True,
    description='Advent of Code',
    long_description=open('README.md').read(),
    url='https://github.com/cr3/adventofcode',
    author='Marc Tardif',
    author_email='marc@interunion.ca',
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    package_data={
        'adventofcode': [
            '*/*.txt',
        ],
    },
    entry_points={
        'console_scripts': [
            'day1-part1= adventofcode.day1:part1',
            'day1-part2= adventofcode.day1:part2',
            'day2-part1= adventofcode.day2:part1',
            'day2-part2= adventofcode.day2:part2',
            'day3-part1= adventofcode.day3:part1',
            'day3-part2= adventofcode.day3:part2',
            'day4-part1= adventofcode.day4:part1',
        ],
    },
)
