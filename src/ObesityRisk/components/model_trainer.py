import os

import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegressionCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split,RandomizedSearchCV
from sklearn.metrics import accuracy_score

from src.ObesityRisk.utils.common import *
from src.ObesityRisk import logger
from src.ObesityRisk.constants import *
from src.ObesityRisk.entity.config_entity import ModelTrainerConfig
import warnings
warnings.filterwarnings('ignore')



class PrepareModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def initiate_model_trainer(self,train_data, test_data):
        logger.info("Initializing model trainer")

        logger.info("Slpitting data into Train and Test")
        X_train, y_train, X_test, y_test = (
                train_data[:, :-1],
                train_data[:, -1],
                test_data[:, :-1],
                test_data[:, -1]
                )

        print(train_data[:,-1])
        print(test_data[:,-1])
        print(y_train)
        print(y_test)

        

        logger.info('fitting train data into model') 

        xcls = XGBClassifier(self.config.grow_policy, self.config.n_estimators, self.config.learning_rate, self.config.gamma,
                            self.config.subsample, self.config.colsample_bytree, self.config.max_depth, 
                            self.config.min_child_weight, self.config.reg_lambda, self.config.reg_alpha)
        xcls.fit(X_train, y_train)

        logger.info("Model Training Completed")
        #rcv = RandomizedSearchCV( estimator= xcls, param_distributions=config.params, n_iter=10,cv=5, n_jobs=1,scoring='accuracy')
        #rcv.fit(X_train, y_train)
        #pred = rcv.predict(X_test)
        #ac = accuracy_score(y_test, pred)
        #print(ac)

        logger.info("Saving Trained Model")
        save_pickle(os.path.join(self.config.model, "model.pkl"),xcls)

        return xcls