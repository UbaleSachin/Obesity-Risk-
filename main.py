from src.ObesityRisk import logger
from src.ObesityRisk.pipeline.stage01_data_ingestion import DataIngestionTrainPipeline
from src.ObesityRisk.pipeline.stage02_data_transformation import DataTransformationPipeline

SATGE_NAME = "Data Ingestion"
try:
    logger.info(f" Stage {SATGE_NAME} started")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f" Stage {SATGE_NAME} finished")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Transformation'
try:
    logger.info(f" Stage {SATGE_NAME} started")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f" Stage {SATGE_NAME} finished")
except Exception as e:
    logger.exception(e)
    raise e
