from ObesityRisk.config.configuration import ConfigurationsManager
from ObesityRisk.components.data_transformation import PrepareTransformation
from ObesityRisk import logger

STAGE_NAME = 'Data Transformation'


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationsManager()
        data_transformation_config = config.get_transformation_config()
        data_transformation = PrepareTransformation(config=data_transformation_config)
        data_transformation.data_split()
        data_transformation.get_data_transformation_object()


if __name__ == '__main__':
    try:
        logger.info(f" <<<<<<<< STAGE --->  {STAGE_NAME}  <--- STARTED  >>>>>>>>>>")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f"<<<<<<<< STAGE ---> {STAGE_NAME} <--- FINISHED >>>>>>>>>>")
    except Exception as e:
        logger.exception(e)