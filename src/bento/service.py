from bentoml.io import JSON,PandasDataFrame
import bentoml
import pandas as pd

iris_clf_runner = bentoml.mlflow.get('model').to_runner()

svc = bentoml.Service('iris_classifier',runners = [iris_clf_runner])

@svc.api(
    input=PandasDataFrame(),
    output=JSON(),
    route='predict_species'
)
def predict(iris_df:pd.DataFrame):
    predictions = iris_clf_runner.predict.run(iris_df)
    return {'predictions':predictions}