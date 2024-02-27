from src.ObesityRisk.config.configuration import ConfigurationsManager
from src.ObesityRisk.components.data_ingestion import DataIngestion
from src.ObesityRisk import logger

SATGE_NAME = 'Data Ingestion'

class DataIngestionTrainPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationsManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()



if __name__ == '__main__':
    try:
        logger.info(f" Stage {SATGE_NAME} started")
        obj = DataIngestionTrainPipeline()
        obj.main()
        logger.info(f" Stage {SATGE_NAME} finished")
    except Exception as e:
        logger.exception(e)

