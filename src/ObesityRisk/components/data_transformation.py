import os
import sys

import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from ObesityRisk.utils.common import *
from ObesityRisk import logger
from ObesityRisk.constants import *
from ObesityRisk.entity.config_entity import  DataTransformationConfig



class PrepareTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def data_split(self):      
         
        csv = pd.read_csv(self.config.data)

        #csv['BMI'] = csv['Weight'] / csv['Height'] * csv['Height']
        
        train_df, test_df = train_test_split(csv, test_size=0.2, random_state=42)

        train_df.to_csv(os.path.join(self.config.train_set, "train_data.csv"), index = False)
        test_df.to_csv(os.path.join(self.config.test_set, "test_data.csv"), index = False)
        logger.info(f'Train Data and Test Data split completed')

        return self.config.train_set, self.config.test_set


    def get_data_transformation_object(self):

        csv = pd.read_csv(self.config.data)
        numeric_features = csv.select_dtypes(include = [int, float]).columns.drop(['id'])
        categorical_features = csv.select_dtypes(include = object).columns.drop(['NObeyesdad'])


        numeric_pipeline = Pipeline(
            steps = [
                ('impiter', SimpleImputer(strategy = 'mean')),
                ('scaler', StandardScaler())
                ]
            )

        categorical_pipeline = Pipeline(
            steps = [
                ('imputer', SimpleImputer(strategy = 'most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown = 'ignore')),
                ('scaler', StandardScaler(with_mean = False))
                ]
            )

        logger.info(f'numeric columns: {numeric_features} ')
        logger.info(f'categorical columns: {categorical_features} ')


        preprocessor = ColumnTransformer(
            [
                ('num_pipeline',numeric_pipeline, numeric_features),
                ('cat_pipeline',categorical_pipeline, categorical_features),
            ]
            )
        
        logger.info("Saving the prerocessing objest")

        #save_pickle(path = os.path.join(self.config.preprocessing_obj, "preprocessor.pkl"),
        #data = preprocessor)

        return preprocessor
    
