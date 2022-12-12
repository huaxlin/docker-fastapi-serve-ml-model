import os
from pathlib import Path

try:
    from sklearn.externals import joblib
except ImportError:
    import joblib

feature_cols = ["age", "gender"]

MODEL_DIR = Path(__file__).parent.parent

model_path = str(MODEL_DIR / 'music_recommender.joblib')
model = joblib.load(model_path)


def predict(row):
    data = list()

    data.append([row.get(feature_col) for feature_col in feature_cols])

    result = model.predict(data)[0]

    return {"class": result}
