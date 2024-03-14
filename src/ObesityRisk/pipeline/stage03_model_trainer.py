from ObesityRisk.config.configuration import ConfigurationsManager
from ObesityRisk.entity.config_entity import ModelTrainerConfig
from ObesityRisk.components.data_transformation import PrepareTransformation
from ObesityRisk.components.model_trainer import PrepareModelTrainer
from ObesityRisk import logger


STAGE_NAME = 'Model Trainer'


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationsManager()
        #base_model_config = config.get_transformation_config()
        #data_transformation = PrepareTransformation(config=base_model_config)
        #data_transformation.data_split()
        #data_transformation.get_data_transformation_object()
        get_model_trainer = config.get_model_trainer()
        model_trainer = PrepareModelTrainer(config=get_model_trainer)
        model_trainer.initiate_model_trainer()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- STARTED  >>>>>>>>>>")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f"<<<<<<<< STAGE ---> {STAGE_NAME} <--- FINISHED >>>>>>>>>>")
    except Exception as e:
        logger.exception(e)

