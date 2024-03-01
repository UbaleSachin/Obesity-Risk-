from dataclasses import  dataclass
from pathlib import Path
import os


@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path


@dataclass(frozen= True)
class DataTransformationConfig:
    root : Path
    train_set : Path
    test_set: Path
    preprocessing_obj: Path