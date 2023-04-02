from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e."
def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n","") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = "RegressorProjects",
    version="0.0.1",
    author="Rachit More",
    author_email="rachitmore3@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
)