from setuptools import setup, find_packages

setup(
    name='simple-quizzer',
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
