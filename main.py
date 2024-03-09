from src.ObesityRisk import logger
from src.ObesityRisk.pipeline.stage01_data_ingestion import DataIngestionTrainPipeline
from src.ObesityRisk.pipeline.stage02_data_transformation import DataTransformationPipeline
from src.ObesityRisk.pipeline.stage03_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- STARTED  >>>>>>>>>>")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- FINISHED >>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Transformation'
try:
    logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- STARTED  >>>>>>>>>>")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- FINISHED >>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer"
try:
    logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- STARTED  >>>>>>>>>>")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- FINISHED >>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
