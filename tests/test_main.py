import pytest
import pandas as pd
import sys
import numpy as np
import os
from src.exception import CustomException
from src.utils import load_object

# Define test data
test_data = {
    'gender': 'female',
    'race_ethnicity': 'group C',
    'parental_level_of_education': "bachelor's degree",
    'lunch': 'standard',
    'test_preparation_course': 'completed',
    'reading_score': 45,
    'writing_score': 23
}

@pytest.fixture
def load_model_and_preprocessor():
    """Fixture to load model and preprocessor"""
    preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
    model_path = os.path.join('artifacts', 'model.pkl')

    model = load_object(model_path)
    preprocessor = load_object(preprocessor_path)
    return model, preprocessor

def test_model_prediction(load_model_and_preprocessor):
    """Test if model runs predictions successfully"""
    model, preprocessor = load_model_and_preprocessor

    # Convert to DataFrame
    test_data_df = pd.DataFrame([test_data], columns=test_data.keys())

    # Transform input data
    arr_data = preprocessor.transform(test_data_df)

    # Ensure transformation output is not empty
    assert arr_data is not None
    assert arr_data.shape[0] == 1  # Check if we have 1 row

    # Make predictions
    pred = model.predict(arr_data)

    # Ensure model produces a prediction
    assert pred is not None
    print("Prediction:", pred)
