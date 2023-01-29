"""
This is a boilerplate pipeline
generated using Kedro 0.18.4
"""

import logging
from typing import Any, Dict, Tuple
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd


def split_data(
    data: pd.DataFrame, parameters: Dict[str, Any]
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Splits data into features and target training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters.yml.
    Returns:
        Split data.
    """

    data_train = data.sample(
        frac=parameters["train_fraction"], random_state=parameters["random_state"]
    )
    data_test = data.drop(data_train.index)

    X_train = data_train.drop(columns=parameters["target_column"])
    X_test = data_test.drop(columns=parameters["target_column"])
    y_train = data_train[parameters["target_column"]]
    y_test = data_test[parameters["target_column"]]

    return X_train, X_test, y_train, y_test



def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LogisticRegression:
    """Trains the linear regression model.
    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.
    Returns:
        Trained model.
    """
    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)
    return regressor



def calculate_accuracy(regressor: LogisticRegression, X_test: pd.DataFrame, y_test: pd.Series):
    """
    It takes a trained logistic regression model, a test set, and the test set's labels, and returns the
    accuracy of the model on the test set
    
    :param regressor: the regressor object
    :type regressor: LogisticRegression
    :param X_test: The test data
    :type X_test: pd.DataFrame
    :param y_test: the actual values of the target variable
    :type y_test: pd.Series
    :return: The accuracy score of the model
    """
    y_pred = regressor.predict(X_test)
    return accuracy_score(y_test,y_pred)

