from setuptools import setup

setup(
    name='dev-cli',
    version='0.1.0',
    py_modules=['main'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'yaml = main:cli',
        ],
    },
)
