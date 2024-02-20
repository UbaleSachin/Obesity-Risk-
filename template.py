import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s: %(lineno)s:')


project_name = 'Obesity Risk'

list_of_flies = {
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/congiguration",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "main.py",
    "requirements.txt",
    "setup.py",
    "dvc.yaml",
    "params.yaml",
    "notebook/EDA.ipynb",
    "notebook/trials.ipynb",
}


for filepath in list_of_flies:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory: {filedir} for file: {filename}')

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'creating file: {filepath}')
    
    else:
        logging.info(f"{filename} already exists")


