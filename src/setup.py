from setuptools import setup

setup(name="Assignment3",
     version ="0.1",
     description="LED Testing for Assignment3 in COMP30670 2017",
     url="",
     author="Kate Rooney",
     author_email="kate.rooney1@ucdconnect.ie",
     licence="none",
     packages=['src'],
     entry_points={'console_scripts':['assignment3=src.main:main']}
     install_requires=['urllib.request','re', 'argparse'],
      )