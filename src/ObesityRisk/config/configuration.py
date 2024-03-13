from ObesityRisk.constants import *
from ObesityRisk.utils.common import read_yaml,create_directories
from ObesityRisk.entity.config_entity import (DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig,
                                                  ModelEvaluationConfig)




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
            root = config.root,
            data = config.data,
            train_set = config.train_set,
            test_set = config.test_set,
            preprocessing_obj = config.preprocessing_obj
        )

        return data_transformation_config




    def get_model_trainer(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.XgbClassifier

        create_directories([config.root])

        model_trainer_config = ModelTrainerConfig(
            root = Path(config.root),
            model = Path(config.model),
            train_set = config.train_set,
            test_set = config.test_set,
            scaled_train_set= config.scaled_train_set,
            scaled_test_set = config.scaled_test_set,
            preprocessing_obj= config.preprocessing_obj,
            grow_policy=  params.grow_policy,
            n_estimators= params.n_estimators,
            learning_rate= params.learning_rate,
            gamma =   params.gamma,
            subsample= params.subsample,
            colsample_bytree= params.colsample_bytree,
            max_depth= params.max_depth,
            min_child_weight= params.min_child_weight,
            reg_lambda= params.reg_lambda,
            reg_alpha= params.reg_alpha,
            
        )

        return model_trainer_config
    


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.XgbClassifier
        
        create_directories([config.root])

        model_evaluation_config = ModelEvaluationConfig(
            root = config.root,
            scaled_test_set = config.scaled_test_set,
            model = config.model,
            preprocessing_obj= config.preprocessing_obj,
            metrics = config.metrics,
            all_params = params,
            mlflow_uri = 'https://dagshub.com/ubalesachin22/Obesity-Risk-.mlflow'
        )

        return model_evaluation_config