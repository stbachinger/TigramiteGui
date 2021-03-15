from setuptools import setup, find_namespace_packages

setup(name='TigramiteGUI',
      version='0.1',
      python_requires=">3.6",
      description='GUI prototype for causal time series analysis program tigramite',
      url='https://github.com/laureleya/PrototypeTigramiteGui',
      author='Sarah Bachinger',
      author_email='sarah.bachinger@uni-jena.de',
      license='LGPL',
      packages=find_namespace_packages(),
      install_requires=[
          'ipywidgets',
          'numpy',
          'scipy',
          'matplotlib',
          'sklearn',
          'networkx',
          'cython',
          'mpi4py',
          'tigramite',
      ],
      zip_safe=False)
