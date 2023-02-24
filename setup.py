from setuptools import setup, find_packages

version = '0.0rc1'

setup(
    name='flashquiz',
    version=version,
    description='[TEST VERSION] Quiz yourself on your flashcards',
    author='mike-fmh',
    author_email='mikemh@uri.edu',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ]
)
