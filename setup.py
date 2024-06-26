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
    install_requires=[
        'setuptools~=58.0.4',
        'pip~=21.2.4',
        'wheel~=0.37.0',
        'dill~=0.3.8',
        'future~=0.18.2',
        'isort~=5.13.2',
        'tomli~=2.0.1',
        'pylint~=3.1.0',
        'astroid~=3.1.0',
        'tomlkit~=0.12.4',
        'mccabe~=0.7.0',
        'platformdirs~=4.2.0',
        'numpy~=1.26.4',
        'pandas~=2.2.1',
        'tiingo~=0.14.0',
        'python-dotenv~=1.0.1',
        'flask~=3.0.2',
        'Flask-Caching~=2.1.0',
        'gunicorn~=21.2.0',
        'pytest~=8.1.1',
        'pytest-mock~=3.14.0',
        'mocker~=1.1.1',
        'mkdocs~=1.5.3',
        'mkdocs-material~=9.5.17',
        'mkdocstrings~=0.24.2',
        'mkdocstrings-python~=1.9.2'
    ],
    python_requires='>=3.8',
    license='MIT License',
)
