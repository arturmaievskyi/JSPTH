from setuptools import setup, find_packages

setup(
    name='JSPTH',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'my_tool=my_library.cli:main',
        ]
    }
)
