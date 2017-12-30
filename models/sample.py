import pandas
import random

# PARAMETERS
s = 10000  # desired sample size


# UTILITY

def row_count(big_file):
    with open(big_file, encoding="utf8") as f:
        for i, l in enumerate(f):
            pass
    return i


# SCRIPT

train = '../data/train.csv'
n = row_count(train)  # number of rows in the file
skip = sorted(random.sample(range(n), n - s))
df = pandas.read_csv(train, skiprows=skip)

print(df)
