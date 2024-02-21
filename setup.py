import setuptools
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

hyphen = "-e ."

__version__ = '0.0.1'

REPO_NAME = 'Obesity-Risk-'
AUTHER_NAME = 'UbaleSachin'
SRC_REPO = 'Obesity Risk'
AUTHER_EMAIL = 'ubalesachin22@gmail.com'


"""def get_requirements(file_path:str) -> List[str]:

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)

            return requirements"""


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHER_NAME,
    description="A small python package for ML app",
    long_description=long_description,
    author_email=AUTHER_EMAIL,
    long_description_content="text/markdown",
    url=f'https://github.com/{AUTHER_NAME}/{REPO_NAME}',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
    #install_requires = get_requirements('requirements.txt')
)
