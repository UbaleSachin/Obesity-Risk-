from src.ObesityRisk.constants import *
from src.ObesityRisk.utils.common import *
from src.ObesityRisk.entity.config_entity import (DataIngestionConfig, DataTransformationConfig)




class ConfigurationsManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_file])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file
        )

        return data_ingestion_config



    
    def get_transformation_config(self)-> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root])
        create_directories([config.train_set])
        create_directories([config.test_set])
        #create_directories([config.preprocessing_obj])

        data_transformation_config = DataTransformationConfig(
            root = Path(config.root),
            train_set = Path(config.train_set),
            test_set = Path(config.test_set),
            preprocessing_obj = Path(config.preprocessing_obj)
        )

        return data_transformation_config