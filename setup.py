from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    It removes any empty lines and comments.
    """
    requirements=[]
    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","")for req in requirements]
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
        return requirements
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements
            
# print(get_requirements('requirements.txt'))
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ankit",
    author_email="work021129@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)