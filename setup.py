from setuptools import setup,find_packages
from typing import List
##USED TO CREATE PACKAGES. ANY FOLDER WHICH CONTAINS __init__.py WILLBE CONVERTED TO PACKAGES, WHICH CAN BE IMPORTED

HYPEN_E_DOT = '-e .'  #-e . is used in requirements.txt so when requirements.txt is run setup.py will also run
def get_requirements(file_path:str)->List[str]:
    '''
    This function will install requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Guneet',
    author_email='guneet1308@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)