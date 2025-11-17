import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[3]

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: Empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    # Resolve relative paths against the project root so calls like
    # Path("config/config.yaml") work regardless of current working directory.
    if not path.is_absolute():
        path = ROOT_DIR / path

    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path} loaded successfully")
        return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """create list of directories

    Args:
        path_to_directories(list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_KB = round(os.path.getsize(path)/1024)
    return f"{size_in_KB} KB"