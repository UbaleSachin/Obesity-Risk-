# frequently used code instead of writing everywhere we will import from here.
import os
from box.exceptions import BoxValueError # for prebuild exceptions
import yaml
from src.ObesityRisk import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import pandas as pd
import pickle



# read yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:      # yaml file path
            content = yaml.safe_load(yaml_file)    # loading ymal file
            logger.info(f'yaml file {path_to_yaml} loaded successfully')
            return ConfigBox(content)   # return ConfigBox type
    except BoxValueError:
        raise ValueError('yaml file is empty') # error if yaml file is empty
    except Exception as e:
        raise e



# creating Directories Artifact for saving files
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True): # list of path directories
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True) # making directories
        if verbose:
            logger.info(f"creating directory at {path}")



# for saving evaluation matrices in jason format
@ensure_annotations
def save_json(path = Path, data = dict): # path for saving json file, data to be saved in json file
    with open(path, 'w') as f:
        json.dump(data, f, indent = 4)
    logger.info(f"jason file saved to as: {path}")



# for loading any json files
@ensure_annotations
def load_json(path: Path) -> ConfigBox: # path for json file
    with open(path) as f:
        content = json.load(f) # loading json file
    logger.info(f"json file loaded successfully from {path}")
    return ConfigBox(content) 



# for saving files in binary format
@ensure_annotations
def save_binary(data: Any, path: Path): # data to stroe in the file, path to binary file
    joblib.dump(value=data, filename=path) # saving binary file
    logger.info(f"binary file saved to {path}")



# for loading binary files
@ensure_annotations
def load_binary(path: Path) -> Any: # path to binary file
    data = joblib.load(path) # loading binary file from path
    logger.info(f"binary file loaded from {path}")
    return data # returning data



# getting size of file 
@ensure_annotations
def get_size(path: Path) -> str: # path of file
    size_in_kb = round(os.path.getsize(path)/1024) # getting file size in KB
    return f" ~ {size_in_kb} KB " 



@ensure_annotations
def save_pickle(path, data):
    with open(path, 'wb') as f:
        pickle.dump(data, f)



@ensure_annotations
def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise e