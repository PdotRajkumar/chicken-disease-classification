import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reading yaml files

    Args:
        path_to_yaml (Path): path as input

    Raises:
        ValueError: if yaml file is empty
        e: For any other exceptions that occur during file reading.


    Returns:
        ConfigBox: Configbox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"content from yaml file : {path_to_yaml} loaded")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): path list as input
        verbose (bool, optional): _description_. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory created for {path} ")
            


@ensure_annotations
def save_json(path:Path, data:dict):
    """save json

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json format
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")
    

@ensure_annotations
def get_size(path:Path)->str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    
    return f"~ {size_in_kb} KB"
 

def decodeImage(imgstring, fiLeName):
    imgdata = base64.b64decode(imgstring)
    with open(fiLeName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath) :
    with open(croppedImagePath,"rb") as f:
        return base64.b64endode(f.read())