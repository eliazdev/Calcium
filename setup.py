from setuptools import setup, find_packages


setup(
    name='pycalcium',
    version='1.1',
    license='GPL',
    author="EliaZ",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/eliazdev/Calcium',
    keywords='calcium',
    install_requires=[
          'ply'
      ],

)