from setuptools import setup

# Requirements should already be installed in conda environment
setup(name='cd_cleaner',
      version='0.0.1',
      description='Package to run joor-cd-cleaner tool',
      author='Toni Sanmateu',
      author_email='antonio.sanmateu@gmail.com',
      packages=['constants', 'dictionaries', 'generate', 'prod', 'services', 'utils'])

