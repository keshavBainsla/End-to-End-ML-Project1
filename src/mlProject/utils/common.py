import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reads yaml file and returns 

    Args:
    path_to_yaml (str): path like input

    Raises:
        valueError: if yaml file is empty
        e:empty file

    Returns:
        ConfigBox:ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbase=True):
    """creates list of directories

    Args:
        path_to_directories (list): list of directories
        ignore_log (bool,optimal): ignore if multiple dirs is to be created. Default to False.
        """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbase:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path:Path,data:dict):
    """saves json file
    Args:
    path (str): path to save json file
    data (dict): data to be saved
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at:{path}")


@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """loads json file
    Args:
    path (str): path to load json file
    Returns:
    ConfigBox:ConfigBox type
    """
    with open(path,"r") as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from :{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    """saves binary file
    Args:
    data (Any): data to be saved
    path (str): path to save binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at:{path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    """loads binary file
    Args:
    path (Path): path to load binary file
    Returns:
    Any: data stored in binary file
    """
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded successfully from :{path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """gets size of file
    Args:
    path (Path): path to file
    Returns:
    str: size of file
    """
    return str(Path(path).stat().st_size)





             