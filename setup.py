import os
from setuptools import setup, Command

class CompleteClean(Command): 
    user_options = [] 
    def initialize_options(self): 
     pass 
    def finalize_options(self): 
     pass 
    def run(self): 
     os.system('rm -rf ./build ./dist ./*.egg-info')
     os.system("find . -type f  -name '*.pyc' -delete")

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "danke",
    python_requires='>=3.6',
    version = "1.0.0",
    author = "Usuario",
    author_email = "usuario@localhost.local",
    description = ("Danke proyect"),
    long_description=read('README.md'),
    url = 'http://localhost/proyecto',
    packages=['danke', 'tests'],
    install_requires=requirements,
    cmdclass={ 'clean': CompleteClean },
    test_suite = 'nose.collector'
)
