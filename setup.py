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
)
