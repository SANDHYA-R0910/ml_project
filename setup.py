from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requiremts(file_path=str)->List[str]:
    '''
    this function will return a list of requirements
    
    '''
     
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
        


setup(
    name='ml_project',
    version='0.0.1',
    author='Sandy',
    author_email='sandhyarsanju@gmail.com',
    packages=find_packages(),
    install_requirements=get_requiremts('requirements.txt')
)
    
    