import os
import pandas as pd
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.metrics import accuracy_score
from ObesityRisk.utils.common import save_json
from ObesityRisk import logger
from ObesityRisk.utils.common import *
from ObesityRisk.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config

    
    def model_evaluation(self, true, predicted):
        ac = accuracy_score(true, predicted)
        return ac

    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.scaled_test_set)

        logger.info("Splitting Test data")
        test_x = test_data.iloc[:, :-1]
        test_y = test_data.iloc[:, -1]

        #test_y = test_data['NObeyesdad'].map(remap)

        logger.info('Loading Trained Model')
        model = load_pickle(self.config.model)


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            test_prediction = model.predict(test_x)

            ac = self.model_evaluation(test_y, test_prediction)

            scores = {"accuracy score": ac}
            save_json(path=Path(self.config.metrics), data = scores)
            
            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("accuracy score", ac)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, 'model', registered_model_name='XgbClassifier')
            else:
                mlflow.sklearn.log_model(model, 'model')
