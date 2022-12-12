from typing import TYPE_CHECKING

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
try:
    from sklearn.externals import joblib
except ImportError:
    import joblib

import pandas as pd
if TYPE_CHECKING:
    from pandas import DataFrame


def train(df: "DataFrame"):
    model = DecisionTreeClassifier()

    x = df.drop(columns=['genre'])
    y = df['genre']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    model.fit(x_train, y_train)

    model_path = 'music_recommender.joblib'
    joblib.dump(model, model_path)


if __name__ == '__main__':
    try:
        from importlib import resources
    except ImportError:
        import importlib_resources as resources

    data_file_name = 'music.csv'
    DATA_MODULE = 'music_recommender.data'
    with resources.open_text(DATA_MODULE, data_file_name) as csv_file:
        df = pd.read_csv(csv_file)

    train(df)
