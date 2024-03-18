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

from ObesityRisk.utils.common import *
from ObesityRisk import logger
from ObesityRisk.constants import *
from ObesityRisk.entity.config_entity import ModelTrainerConfig
from ObesityRisk.components.data_transformation import PrepareTransformation
import warnings
warnings.filterwarnings('ignore')



class PrepareModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def initiate_model_trainer(self):
        train_data = pd.read_csv(self.config.train_set)
        test_data = pd.read_csv(self.config.test_set)

        logger.info("Initializing model trainer")

        logger.info("Slpitting Train data into train and test")
        train_X = train_data.drop(['id', 'NObeyesdad'], axis=1)
        train_y = train_data['NObeyesdad']
        test_X = test_data.drop(['id', 'NObeyesdad'], axis=1)
        test_y = test_data['NObeyesdad']

        remap={'Insufficient_Weight':0 ,'Normal_Weight':1 ,'Obesity_Type_I':2 ,'Obesity_Type_II':3,
                    'Obesity_Type_III':4, 'Overweight_Level_I':5 ,'Overweight_Level_II':6}

        train_y = train_data['NObeyesdad'].map(remap)
        test_y = test_data['NObeyesdad'].map(remap)

        logger.info("loading preprocessing object")
        preprocessor = PrepareTransformation.get_data_transformation_object(self)

        logger.info('applying preprocessing object on train features')
        scaled_train_X = preprocessor.fit_transform(train_X)
        scaled_test_x = preprocessor.transform(test_X)

        
        print("Input Features of Train Data: ", train_data.iloc[:, :-1].columns)
        print("Target Feature of Train Data: ", train_data.iloc[:, -1])
        print(scaled_train_X)
        print(train_y)

        logger.info('Converting scaled train array into dataframe')
        scaled_train_X_data = np.array(scaled_train_X)
        scaled_train_X_df = pd.DataFrame(scaled_train_X_data)
        scaled_train_X_df.loc[:, 'NObeyesdad'] = train_y
        print(scaled_train_X_df)

        logger.info('Converting scaled test array into dataframe')
        scaled_test_x_data = np.array(scaled_test_x)
        scaled_test_x_df = pd.DataFrame(scaled_test_x_data)
        scaled_test_x_df.loc[:, 'NObeyesdad'] = test_y
        print(scaled_test_x_df)

        logger.info('Saving scaled train and test dataframe to')
        scaled_train_X_df.to_csv(os.path.join(self.config.scaled_train_set, 'scaled_train_data.csv'), index= False)
        scaled_test_x_df.to_csv(os.path.join(self.config.scaled_test_set, 'scaled_test_data.csv'), index= False)


        logger.info('fitting train data into model') 

        xcls = XGBClassifier(grow_policy= self.config.grow_policy, n_estimators=self.config.n_estimators, 
                             learning_rate=self.config.learning_rate, gamma=self.config.gamma, subsample=self.config.subsample,
                             colsample_bytree=self.config.colsample_bytree, max_depth=self.config.max_depth, 
                             min_child_weight=self.config.min_child_weight, reg_lambda=self.config.reg_lambda, 
                             reg_alpha=self.config.reg_alpha)
        xcls.fit(scaled_train_X, train_y)
        #rcv = RandomizedSearchCV( estimator= xcls, param_distributions=config.params, n_iter=10,cv=5, n_jobs=1,scoring='accuracy')
        #rcv.fit(X_train, y_train)
        #pred = rcv.predict(X_test)
        #ac = accuracy_score(y_test, pred)
        #print(ac)

        logger.info("saving trained model")
        model = save_pickle(os.path.join(self.config.model, "model.pkl"),xcls)
        save_pickle(os.path.join(self.config.preprocessing_obj, 'preprocessor.pkl'), preprocessor)

        return scaled_train_X_df, scaled_test_x_df, model