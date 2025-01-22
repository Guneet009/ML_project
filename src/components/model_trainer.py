import os
import sys

from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model,load_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_array,test_array):
        
        try:
            
            X_train = train_array[:,:-1]
            y_train = train_array[:,-1]
            X_test = test_array[:,:-1]
            y_test = test_array[:,-1]
            
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Linear Regression": LinearRegression(),
                "ADABoost": AdaBoostRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "CatBoost": CatBoostRegressor()
                # "XGBoost":XGBRegressor()
            }
            
            params = {
                "Decision Tree":{
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson']
                },
                "Random Forest":{
                    'n_estimators':[8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "ADABoost":{
                    'learning_rate':[.1,.01,0.5,.001],
                    'n_estimators':[8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    'n_estimators':[8,16,32,64,128,256]
                },
                "CatBoost":{
                    'depth':[6,8,10],
                    'learning_rate':[0.01, 0.05, 0.1],
                    'iterations':[30, 50, 100]
                }
                # "XGBoost":{
                #     'learning_rate':[.1,.01,.05,.001],
                #     'n_estimators':[8,16,32,64,128,256]
                # }
            }
            
            model_report:dict = evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,
                                               y_test=y_test,models=models,param=params)
            
            best_model_score = max(sorted(model_report.values()))
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model= models[best_model_name]
            
            if best_model_score<0.6:
                raise CustomException("No good model")
            
            logging.info("Best model found")
            logging.info(f"Best model is {best_model_name}")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            predicted = best_model.predict(X_test)
            
            r2_square = r2_score(y_test,predicted)
            
            return r2_square
            
        except Exception as e:
            raise CustomException(e,sys)
