from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
import os
import sys
from dataclasses import dataclass

from src.utils import save_object



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class Data_Transformation:
    def __init__(self):
        self.dataTransformationConfig= DataTransformationConfig()
    
    def get_data_transformer_object(self):
        '''
        This function is responsible for Data Transformation object creation
        '''
        
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median"))
                    ("scaler",StandardScaler())
                ]
            )
            
            cat_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy="most_frequent"))
                    ("onehotencoder",OneHotEncoder())
                    ("scaling",StandardScaler(with_mean=False))
                ]
            )
            
            preprocessor = ColumnTransformer(
                ["num_pipeline",num_pipeline,numerical_columns]
                ["cat_pipelie",cat_pipeline,categorical_columns]
            )
            logging.info("Preprocessor object created")
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):
        
        '''
        To apply data transformation on data
        '''
        try:
            
            df_train = pd.read_csv(train_path)
            df_test = pd.read_csv(test_path)
            
            logging.info("Read the data")
            
            preprocessor_obj = self.get_data_transformer_object()
            
            logging.info("Got preprocessor object")
            
            target_column_name="math_score"
            
            input_feature_train_df = df_train.drop(columns=[target_column_name],axis=1)
            output_feature_train = df_train[target_column_name]
            input_feature_test_df = df_test.drop(columns=[target_column_name],axis=1)
            output_feature_test_df = df_test[target_column_name]
            
            logging.info("Applying preprocessor obj")
            
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[input_feature_train_arr,np.array(output_feature_train)]
            test_arr = np.c_[input_feature_test_arr,np.array(output_feature_test_df)]
            
            logging.info("Transformation completed")
            
            save_object(
                file_path=self.dataTransformationConfig.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )
            
            logging.info("Saved preprocesssor obj")
            
            return (
                train_arr,
                test_arr,
                self.dataTransformationConfig.preprocessor_obj_file_path
            )
            
            
        except Exception as e:
            raise CustomException(e,sys)