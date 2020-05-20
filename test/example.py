from sklearn-ranking import RankSVM
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_validate
from sklearn import *
np.random.seed(1)

# prepare dataset
n_samples, n_features = 400, 5
true_coef = np.random.randn(n_features)
X = np.random.randn(n_samples, n_features)
noise = np.random.randn(n_samples) / np.linalg.norm(true_coef)
y = np.dot(X, true_coef)
y = np.arctan(y)  # add non-linearities
y += .1 * noise  # add noise
Y = np.c_[y, np.mod(np.arange(n_samples), 5)]

# Cross validate the sample
cv = cross_validation.KFold(n_samples, 5)
train, test = iter(cv).next()

# model training RANKSVM
rank_svm = RankSVM().fit(X[train], Y[train])
print(f'Performance of ranking:{rank_svm.score(X[test], Y[test])}')

# and that of linear regression
ridge = linear_model.RidgeCV(fit_intercept=True)
ridge.fit(X[train], y[train])

X_test_trans, y_test_trans = transform_pairwise(X[test], y[test])
score = np.mean(np.sign(np.dot(X_test_trans, ridge.coef_)) == y_test_trans)
print(f'Performance of linear regression : {score}')
