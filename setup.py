from setuptools import setup, find_packages

setup(
    name='simplequiz',
    version='0.1',
    description='GUI quizzer',
    author='mike-fmh',
    author_email='mikemh@uri.edu',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ]
)
