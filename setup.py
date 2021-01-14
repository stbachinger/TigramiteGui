from setuptools import setup, find_namespace_packages

setup(name='TigramiteGUIPrototype',
      version='0.1',
      description='GUI prototype for causal time series analysis programe tigramite',
      url='https://github.com/laureleya/PrototypeTigramiteGui',
      author='Sarah Bachinger',
      author_email='sarah.bachinger@uni-jena.de',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=[
          'ipywidgets',
      ],
      zip_safe=False)