from typing import TYPE_CHECKING

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

try:
    from sklearn.externals import joblib
except ImportError:
    import joblib
import pandas as pd

if TYPE_CHECKING:
    from pandas import DataFrame


def test(df: "DataFrame", model_path):
    model = joblib.load(model_path)

    x = df.drop(columns=['genre'])
    y = df['genre']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    predictions = model.predict(x_test)

    score = accuracy_score(y_test, predictions)

    return {"accuracy": score}


if __name__ == '__main__':
    try:
        from importlib import resources
    except ImportError:
        import importlib_resources as resources

    data_file_name = 'music.csv'
    DATA_MODULE = 'music_recommender.data'
    with resources.open_text(DATA_MODULE, data_file_name) as csv_file:
        df = pd.read_csv(csv_file)

    model_path = 'music_recommender.joblib'
    metrics = test(df, model_path)
    print(f'{metrics = }')
