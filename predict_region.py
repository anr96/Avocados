import pandas as pd
from sklearn.utils import shuffle
from sklearn import svm, metrics, neural_network


"""
Read data and partition train/test sets
Goal: predict the region an avocado came from
Columns not used for prediction: id, Date, and type
"""
input_file = 'data/avocado.csv'
data = shuffle(pd.read_csv(input_file))
print(data.shape)
print(data[:-1000])
regions = pd.read_csv(input_file, usecols=[13])

train = data[:-1000]
test = data[-1000:]
train_x = train.drop('id', axis=1)
train_x = train_x.drop('region', axis=1)
train_x = train_x.drop('Date', axis=1)
train_x = train_x.drop('type', axis=1)
train_y = train[train.columns[-1]]
test_x = test.drop('id', axis=1)
test_x = test_x.drop('region', axis=1)
test_x = test_x.drop('Date', axis=1)
test_x = test_x.drop('type', axis=1)
test_y = test[test.columns[-1]]

print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)


""" Support vector machine classifier """
svm_clf = svm.SVC(gamma=0.001)  # , C=len(regions))
svm_clf.fit(train_x, train_y)
svm_pred = svm_clf.predict(test_x)


"""
Neural network multi-layer perceptron classifier
TODO: change around parameters 
"""
mlp_clf = neural_network.MLPClassifier()
mlp_clf.fit(train_x, train_y)
mlp_pred = mlp_clf.predict(test_x)


""" Comparison of metrics for classifiers """
print(metrics.classification_report(test_y, svm_pred))
# results are noticeably better than non-NN classifier
print(metrics.classification_report(test_y, mlp_pred))
