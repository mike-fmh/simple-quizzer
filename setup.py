from setuptools import setup, find_packages

setup(
    name='flashquiz',
    version='0.1',
    description='Quiz yourself on your flashcards',
    author='mike-fmh',
    author_email='mikemh@uri.edu',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ]
)
