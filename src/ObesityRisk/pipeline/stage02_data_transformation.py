from src.ObesityRisk.config.configuration import ConfigurationsManager
from src.ObesityRisk.components.data_transformation import PrepareTransformation
from src.ObesityRisk import logger

STAGE_NAME = 'Data Transformation'


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationsManager()
        data_transformation_config = config.get_transformation_config()
        data_transformation = PrepareTransformation(config=data_transformation_config)
        train_data, test_data = data_transformation.data_split()
        data_transformation.initiate_data_transformation(train_data, test_data)


if __name__ == '__main__':
    try:
        logger.info(f" Stage {SATGE_NAME} started")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f" Stage {SATGE_NAME} finished")
    except Exception as e:
        logger.exception(e)