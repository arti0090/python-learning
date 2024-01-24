import pandas as pd
import seaborn as sns

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'

column_names = [
    'MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin'
]

raw_dataset = pd.read_csv(
    url,
    names=column_names,
    na_values='?',
    comment='\t',
    sep=' ',
    skipinitialspace=True
)

dataset = raw_dataset.copy()

# show last few of dataset
# print(dataset.tail())

# dataset has some NaN values, this function first check for them and later sums it
# will return Horsepower - 6 as 6 cars have no value in it
dataset.isna().sum()

# drop the rows that has no values 
dataset = dataset.dropna()

# changing Origin dataset from Origin[1,2,3] to boolean for every each of them
dataset['Origin'] = dataset['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
# added dtype=int as it does not like booleans later
dataset = pd.get_dummies(dataset, columns=['Origin'], prefix='', prefix_sep='', dtype=int)

# split dataset for train and test
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# ploting the data to search for something that is function of other, like here it could be that mpg gets lower
# when there is more weight or displacement etc.
sns.pairplot(train_dataset[['MPG', 'Cylinders', 'Displacement', 'Weight']], diag_kind='kde')

# print(train_dataset.describe().transpose())

# pop the mpg label from data
train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop('MPG')
test_labels = test_features.pop('MPG')

def get_train_dataset():
    return train_features, train_labels

def get_test_dataset():
    return test_features, test_labels

def get_full_train_dataset():
    return train_dataset