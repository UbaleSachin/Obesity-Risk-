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
    data : Path
    train_set : Path
    test_set: Path
    preprocessing_obj: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root : Path
    model : Path
    train_set :Path
    test_set: Path
    scaled_train_set: Path
    scaled_test_set: Path
    preprocessing_obj: Path
    grow_policy:  str
    n_estimators: int
    learning_rate: float
    gamma :   float
    subsample: float
    colsample_bytree: float
    max_depth: int
    min_child_weight: int
    reg_lambda: float
    reg_alpha: float



@dataclass(frozen = True)
class ModelEvaluationConfig:
    root: Path
    scaled_test_set: Path
    model: Path
    preprocessing_obj: Path
    metrics: Path
    all_params: dict
    mlflow_uri: str