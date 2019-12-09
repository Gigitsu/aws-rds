from setuptools import setup

from codecs import open
from os import path

version = '0.0.1b1'

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aws-rds',
    version=version,
    description='Manage AWS RDS tokens',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Luigi Clemente',
    author_email='luigi.clemente@gsquare.it',
    packages=['awsrds'],
    scripts=['aws-rds'],
    keywords='aws rds db auth token db_auth_token generate_db_auth_token',
    url='https://github.com/gigitsu/aws-rds',
    install_requires=['boto3', 'pyperclip'],
    entry_points={
        'console_scripts': [
            'aws-rds=awsrds:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
