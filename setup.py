from setuptools import setup
from setuptools import find_packages


setup(name='recurrentshop',
      version='1.2.0',
      description='Framework for building complex recurrent neural networks with Keras',
      author='Fariz Rahman',
      author_email='fariz@datalog.ai',
      url='https://github.com/GuillaumeShrp/recurrentshop',
      download_url='https://github.com/GuillaumeShrp/recurrentshop',
      license='MIT',
      install_requires=['keras'],
      packages=find_packages())
