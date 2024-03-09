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

    def data_split(self):      
         
        csv = pd.read_csv(self.config.data)
        
        train_df, test_df = train_test_split(csv, test_size=0.2, random_state=42)

        train_df.to_csv(os.path.join(self.config.train_set, "train_data.csv"), index = False)
        test_df.to_csv(os.path.join(self.config.test_set, "test_data.csv"), index = False)
        logger.info(f'Train Data and Test Data split completed')

        return self.config.train_set, self.config.test_set


    def get_data_transformation_object(self,):

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

        return preprocessor


    def initiate_data_transformation(self,train_data, test_data,):

        train_data = pd.read_csv('artifacts/data_transformation/train_set/train_data.csv')
        test_data = pd.read_csv('artifacts/data_transformation/test_set/test_data.csv')

        logger.info(f"Loading Train_data and Test_data")

        target_feature = ["NObeyesdad"]

        remap={'Insufficient_Weight':0 ,'Normal_Weight':1 ,'Obesity_Type_I':2 ,'Obesity_Type_II':3,
                    'Obesity_Type_III':4, 'Overweight_Level_I':5 ,'Overweight_Level_II':6}
        
        
        input_train_features = train_data.iloc[:,1:-1]
        target_input_train_feature = train_data['NObeyesdad'].map(remap)

        input_test_features = test_data.iloc[:,1:-1]
        traget_input_test_feture = test_data['NObeyesdad'].map(remap)

        logger.info(f'loading preprocessing object')

        preprocessing_obj = self.get_data_transformation_object()

        logger.info(f'applying preprocessing on input_train_features and input_test_features')

        input_train_array = preprocessing_obj.fit_transform(input_train_features)
        input_test_array = preprocessing_obj.transform(input_test_features)

        train_array = np.c_[input_train_array, np.array(target_input_train_feature)]
        test_array = np.c_[input_test_array, np.array(traget_input_test_feture)]

        logger.info("Saving the prerocessing objest")

        save_pickle(path = os.path.join(self.config.preprocessing_obj, "preprocessor.pkl"),
        data = preprocessing_obj)
        
        return train_array, test_array