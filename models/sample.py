import pandas
import random
import os

# PARAMETERS
s = 10000  # desired sample size


# UTILITY

def row_count(big_file):
    with open(big_file, encoding="utf8") as f:
        for i, l in enumerate(f):
            pass
    return i


def write_csv(obj, filename):
    path = '../data/' + filename
    os.makedirs(os.path.dirname(path), exist_ok=True)
    obj.to_csv(path)


# SCRIPT

train = '../data/train.csv'

n = row_count(train)  # number of rows in the file
skip = sorted(random.sample(range(n), n - s))
df = pandas.read_csv(train, skiprows=skip)
print(df)
write_csv(df, 'true_train.csv')