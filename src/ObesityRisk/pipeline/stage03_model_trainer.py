from src.ObesityRisk.config.configuration import ConfigurationsManager
from src.ObesityRisk.entity.config_entity import ModelTrainerConfig
from src.ObesityRisk.components.data_transformation import PrepareTransformation
from src.ObesityRisk.components.model_trainer import PrepareModelTrainer
from src.ObesityRisk import logger


STAGE_NAME = 'Model Trainer'


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationsManager()
        base_model_config = config.get_transformation_config()
        data_transformation = PrepareTransformation(config=base_model_config)
        train_data, test_data = data_transformation.data_split()
        train_arr,test_arr = data_transformation.initiate_data_transformation(train_data, test_data)

        get_model_trainer = config.get_model_trainer()
        model_trainer = PrepareModelTrainer(config=get_model_trainer)
        model_trainer.initiate_model_trainer(train_arr,test_arr)


if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- STARTED  >>>>>>>>>>")
        obj = ModelTrainerPipeline()
        obj.main
        logger.info(f"<<<<<<<< STAGE ---> {STAGE_NAME} <--- FINISHED >>>>>>>>>>")
    except Exception as e:
        logger.exception(e)

