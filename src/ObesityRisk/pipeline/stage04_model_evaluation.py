from src.ObesityRisk.config.configuration import ConfigurationsManager
from src.ObesityRisk.components.model_evaluation import ModelEvaluation
from src.ObesityRisk import logger

STAGE_NAME = 'Model Evaluation'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationsManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        #model_evaluation_config.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<< STAGE --->  {STAGE_NAME}  <--- STARTED  >>>>>>>>>>")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"<<<<<<<< STAGE ---> {STAGE_NAME} <--- FINISHED >>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e