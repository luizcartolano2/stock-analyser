from setuptools import setup, find_packages

setup(
    name='stock-analyser',
    version='0.1.0',
    author='Luiz Eduardo Cartolano',
    author_email='cartolanoluiz@gmail.com',
    description='A project to analyse and give the best stocks on a given exchange',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/luizcartolano2/stock-analyser',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.8',
    license='MIT License',
)
