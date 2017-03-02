from setuptools import setup

setup(name="Start",
     version ="0.1",
     description="LED Testing for Assignment3 in COMP30670 2017",
     url="",
     author="Kate Rooney",
     author_email="kate.rooney1@ucdconnect.ie",
     license="none",
     packages=['src'],
     entry_points={
        'console_scripts':['Start=src.main:main']
        },
      )