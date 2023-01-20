
import pandas as pd
import numpy as np
import sys
import os
import random
import pickle
import joblib

from itertools import combinations
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier

# Declare the constants
LABEL_COLUMN_NAME = 'bug'
UNWANTED_COLUMNS = []
WANTED_COLUMNS = [
    'dit', 'noc', 'cbo', 'rfc', 'lcom', 'ca', 'ce', 'npm', 'lcom3',
    'loc', 'dam', 'moa', 'mfa', 'cam', 'ic', 'cbm', 'amc', 'max_cc', 'avg_cc'
]
N_FOLDS = 5
RANDOM_STATE = 1
N_ESTIMATORS = 20
SUBSAMPLE = 0.60
LR = 0.1
MAX_DEPTH = 10

# Declare the variables
total = 0
best_models = 0
best_generated_model = 0
feat = []
models = []

# Generate the features
for c in range(1, 50):
    feat.append('feature')

# Generate the combinations


def random_combinations(iterable, r, x):
    pool = tuple(iterable)
    n = len(pool)
    a = []
    for i in range(x):
        indices = sorted(random.sample(range(n), r))
        a.insert(len(a), tuple(pool[i] for i in indices))
    return list(set(a))


# Evaluate the features
def eval_features(df, features):
    global models
    id = 0

    X = df[features].values
    y = df[LABEL_COLUMN_NAME].values
    a = []
    b = []
    cv = StratifiedKFold(n_splits=N_FOLDS, shuffle=True,
                         random_state=RANDOM_STATE)
    for (train, val) in cv.split(X, y):
        classifier = XGBClassifier(n_estimators=N_ESTIMATORS, subsample=SUBSAMPLE,
                                   learning_rate=LR, max_depth=MAX_DEPTH, n_jobs=16, random_state=1)

        classifier = classifier.fit(X[train], y[train])

        if (id == 3):
            models.append(classifier)
        id = id + 1

        probas_ = classifier.predict_proba(X[val])
        area = roc_auc_score(y[val], probas_[:, 1])
        a.insert(len(a), area)

        for i in probas_[:, 1]:
            b.append(i)

    return a, b

# Evaluate the with the panel


def eval_panel(df, comb):
    for ff in comb:
        f = []
        for x in ff:
            f.insert(len(f), x)
        A, B = eval_features(df, f)
        print("%s,%f" % (f, np.mean(A)))
        sys.stdout.flush()

# Check the best models


def check_best_models(acc, features):
    global best_models, best_generated_model, feat

    model_accuracy = np.mean(acc)*100

    # check the number of models above the baseline model
    if (model_accuracy > 78.5):
        best_models = best_models + 1
        if (len(features) < len(feat)):
            feat = features

    # check the highest model achieved
    if (model_accuracy > best_generated_model):
        best_generated_model = model_accuracy


# Reads dataset
df = pd.read_csv(sys.argv[1])

# Maps label
df.dropna(axis=0, subset=['bug'], inplace=True)

# Main loop
RANDOM_STATE = 1
f = []
i = 0
for f1 in WANTED_COLUMNS:
    if i == 20:
        break
    if f1 in f:
        continue
    k = 0
    x = f1
    i = i + 1
    j = 0
    avg = 0
    for f2 in WANTED_COLUMNS:
        if f2 in f:
            continue
        j = j + 1
        f.insert(len(f), f2)
        A, B = eval_features(df, f)
        print("%s,%f" % (f, np.mean(A)))
        f.remove(f2)
        sys.stdout.flush()
        avg = avg + np.mean(A)
        if np.mean(A) > k:
            x = f2
            k = np.mean(A)
    avg /= j
    f.insert(len(f), x)

for c in range(1, 5):
    s = 50000
    comb = random_combinations(WANTED_COLUMNS, c, s)
    eval_panel(df, comb)

joblib.dump(models, 'models.pkl')

print('program complete!!!')
