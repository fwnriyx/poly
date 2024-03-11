import pandas as pd
import numpy as np
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import warnings
warnings.filterwarnings('ignore')


# load data
df = pd.read_csv('data/winequality.csv')
X = df.drop(columns='quality')
y = df['quality']
X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=42)

# define model hyperparameter
min_split = 2
min_leaf = 1

# run MLFlow script
with mlflow.start_run():   
    random_forest = RandomForestClassifier(n_estimators=100,
                                           min_samples_split=min_split,
                                           min_samples_leaf=min_leaf)

    random_forest.fit(X_train, y_train)  # fit data

    y_pred = random_forest.predict(X_val)  # run prediction

    # Getting metrics on the validation
    acc_score = accuracy_score(y_val, y_pred)
    recall = recall_score(y_val, y_pred, average='macro')    
    precision = precision_score(y_val, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_val, y_pred, average='macro')

    # logging parameters and metrics to MLFlow
    mlflow.log_param('sample_min_split', min_split)
    mlflow.log_param('sample_min_leaf', min_leaf)
    mlflow.log_metric('accuracy', acc_score)
    mlflow.log_metric('recall', recall)
    mlflow.log_metric('precision', precision)

    # logging model to MLFlow
    mlflow.sklearn.log_model(random_forest, 'random_forest')