from setuptools import setup

setup(name='chalice_helpers',
      version='0.1',
      description='Some utilities for AWS Chalice',
      url='http://github.com/stechstudio/chalice_helpers',
      author='Bubba Hines',
      author_email='bubba@stechstudio.com',
      license='MIT',
      packages=['chalice_helpers'],
      install_requires=[
          'chalice',
          'boto3',
          'commandlines'
      ],
      scripts=[
          'bin/kms-encrypt',
          'bin/kms-decrypt'
      ],
      zip_safe=False)
