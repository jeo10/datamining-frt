import pandas as pd


def open_file():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    df = pd.read_csv(url, names=['sepal length', 'sepal width', 'petal length','petal width', 'target'])
    return df