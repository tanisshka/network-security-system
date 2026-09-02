from setuptools import Require, setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    try:
        with open('requirements.txt') as f:
            requirements = f.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            if '-e .' in requirements:
                requirements.remove('-e .')
        return requirements
    except Exception as e:
        print(f"Error: {e}")
    return requirements 

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Tanishka Patil",
    author_email = "tanishkapatil0102@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
    description = "This is a machine learning network security project",
)
    
    
    