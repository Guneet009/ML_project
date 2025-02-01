# from src.pipeline import predict_pipeline
# from src.logger import logging
# from src.exception import CustomException
# from src.utils import load_object,save_object,evaluate_model
# import os
# import sys

# def test_model():
#     preprocessor_path= os.path.join('artifacts','preprocessor.pkl')
#     model_path = os.path.join('artifacts','model.pkl')
#     logging.info("Loading object")
#     model = load_object(model_path)
#     preprocessor = load_object(preprocessor_path)
#     logging.info('Objects loaded')
#     data_scaled = preprocessor.transform(features)
#     preds = model.predict(data_scaled)


# test_data = {'gender':'female',
#                 'race_ethnicity':'group C',
#                 'parental_level_of_education':"bachelor's degree",
#                 'lunch':'standard',
#                 'test_preparation_course':'completed',
#                 'reading_score':45,
#                 'writing_score':23}

# arr_data = preprocessor.transform(np.array(test_data).reshape(1, -1))

# import pytest
# import pandas as pd
# import sys
# import numpy as np
# from sklearn.model_selection import train_test_split
# from src.exception import CustomException
# from src.utils import load_object
# import os

# # Define test data as a dictionary (single row)
# test_data = {
#     'gender': 'female',
#     'race_ethnicity': 'group C',
#     'parental_level_of_education': "bachelor's degree",
#     'lunch': 'standard',
#     'test_preparation_course': 'completed',
#     'reading_score': 45,
#     'writing_score': 23
# }

# try:
#     # Convert to DataFrame with explicitly defined columns
#     test_data_df = pd.DataFrame([test_data], columns=test_data.keys())

#     preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
#     model_path = os.path.join('artifacts', 'model.pkl')

#     model = load_object(model_path)
#     preprocessor = load_object(preprocessor_path)

#     # Transform input data
#     arr_data = preprocessor.transform(test_data_df)

#     # Make predictions
#     pred = model.predict(arr_data)
#     print(pred)

# except Exception as e:
#     raise CustomException(e, sys)
