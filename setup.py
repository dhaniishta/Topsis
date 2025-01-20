from setuptools import setup, find_packages

setup(
    name='Topsis-Dhanishta-102203520',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis = Topsis_Dhanishta_102203520.topsis:main',
        ],
    },
    author='Dhanishta',
    author_email='dhanishtajaggi@gmail.com',
    description='A Python package for Topsis method',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dhaniishta/Topsis-Dhanishta-102203520',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
