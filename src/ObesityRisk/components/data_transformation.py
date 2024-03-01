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

from src.ObesityRisk.utils.common import *
from src.ObesityRisk import logger
from src.ObesityRisk.constants import *
from src.ObesityRisk.entity.config_entity import  DataTransformationConfig



class PrepareTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def data_split(self,
                csv_file_path = CSV_FILE_PATH,
                train_set_path = TRAIN_SET_PATH,
                test_set_path = TEST_SET_PATH,
                ):      
         
        self.csv = read_csv(csv_file_path)
        self.train = train_set_path
        self.test = test_set_path
        
        train_df, test_df = train_test_split(self.csv, test_size=0.2, random_state=42)

        train_df.to_csv(self.train)
        test_df.to_csv(self.test)
        logger.info(f'{train_df} and {test_df} split completed')

        return self.train, self.test


    def get_data_transformation_object(self,
                    csv_file_path = CSV_FILE_PATH):

        self.csv = read_csv(csv_file_path)
        numeric_features = self.csv.select_dtypes(include = [int, float]).columns.drop(['id'])
        categorical_features = self.csv.select_dtypes(include = object).columns.drop(['NObeyesdad'])


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

        return preprocessor


    def initiate_data_transformation(self,
                                train_data, test_data, 
                                preprocessing_obj = PREPROCESSOR_PATH,
                                ):

        train_data = read_csv(TRAIN_SET_PATH)
        test_data = read_csv(TEST_SET_PATH)
        self.preprocessing_obj = preprocessing_obj

        logger.info(f"loading {train_data} and {test_data}")

        target_feature = ["NObeyesdad"]

        input_train_features = train_data.iloc[:,1:-1]
        target_input_train_feature = train_data['NObeyesdad']

        input_test_features = test_data.iloc[:,1:-1]
        traget_input_test_feture = test_data['NObeyesdad']

        logger.info(f'loading preprocessing object')

        preprocessing_obj = self.get_data_transformation_object()

        logger.info(f'applying preprocessing on {input_train_features} and {input_test_features}')

        input_train_array = preprocessing_obj.fit_transform(input_train_features)
        input_test_array = preprocessing_obj.transform(input_test_features)

        train_array = np.c_[input_train_array, np.array(target_input_train_feature)]
        test_array = np.c_[input_test_array, np.array(traget_input_test_feture)]

        logger.info("Saving the prerocessing objest")

        save_pickle(path = self.preprocessing_obj,
        data = preprocessing_obj)

        return train_array, test_array