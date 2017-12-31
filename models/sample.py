import pandas
import random
import os
from sklearn.model_selection import KFold

# PARAMETERS
s = 10000  # desired sample size


# UTILITY

def row_count(big_file):
    with open(big_file, encoding="utf-8") as f:
        for i, l in enumerate(f):
            pass
    return i


def write_csv(obj, filename):
    path = '../data/' + filename
    os.makedirs(os.path.dirname(path), exist_ok=True)
    obj.to_csv(path, encoding="utf-8")


# USE

def thin_data():
    train = '../data/train.csv'

    n = row_count(train)  # number of rows in the file
    skip = sorted(random.sample(range(n), n - s))
    skip.remove(0)
    skip.remove(1)
    df = pandas.read_csv(train, skiprows=skip, sep=',', engine='python')
    print(df)
    write_csv(df, 'small_train.csv')


def cross_validation_split(df):
    kf = KFold(n_splits=10, shuffle=True)
    kf.get_n_splits(df)
    for train_index, test_index in kf.split(df):
        print(train_index)
        # print(test_index)


thin_data()
cross_validation_split(pandas.read_csv('../data/small_train.csv', encoding='utf-8'))
