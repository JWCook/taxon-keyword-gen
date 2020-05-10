from setuptools import setup, find_packages

setup(
    name='taxon-keyword-gen',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'Click>=7.0',
        'pandas',
        'progress',
        'requests',
        'requests-ftp',
    ],
    entry_points={
        'console_scripts': [
            'taxgen=taxgen.cli:main',
        ],
    }
)
