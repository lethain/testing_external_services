import os
from setuptools import setup, find_packages
import testing_external_services

setup(name='testing_external_services',
      version=testing_external_services.__version__,
      description='Example of testing a Django app with external services using mock.',
      author='Will Larson',
      author_email='lethain@gmail.com',
      url='http://www.lethain.com',
      packages=find_packages(),
      classifiers=[],
      include_package_data=True,
      package_data={ 'testing_external_services': ['templates/*.html', 'fixtures/*.json']},
      zip_safe=False,
      )
