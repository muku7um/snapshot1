from setuptools import setup

setup(
name='snapshot1',
version='0.1',
description='snapshot1 is tool to manage AWS EC2 instances',
licence='GPLv3+',
packages=['shotty'],
install_requires=[
    'click',
    'boto3'
],
entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    ''',
)
