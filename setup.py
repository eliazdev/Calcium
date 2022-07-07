from setuptools import setup, find_packages


setup(
    name='pycalcium',
    version='1.1',
    license='GPL',
    author="EliaZ",
    description="A Mathematical Equation Parser and Solver",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/eliazdev/Calcium',
    download_url="https://github.com/eliazdev/Calcium/archive/refs/tags/v1.1.0.tar.gz",
    keywords='calcium',
    install_requires=[
          'ply'
      ],

)
