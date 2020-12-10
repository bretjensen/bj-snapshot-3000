from setuptools import setup

setup(
    name='bj-snapshot-3000',
    version='0.1',
    author='Brett Jensen',
    author_email='bretjensen@gmail.com',
    description='CLI Tool for managing EC2 volume snapshots from AWS',
    license='GPLv3+',
    packages=['shotty'],
    url="https://github.com:bretjensen/bj-snapshot-3000.git",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty.cli
    ''',
)