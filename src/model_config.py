from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression

CONFIG = [
    {
        'name': 'Decision Tree Classifier',
        'Classifier': DecisionTreeClassifier,
        'dataset': 'balanced',
        'params': {
            'random_state': None,
            'max_depth': None,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Decision Tree Classifier',
        'Classifier': DecisionTreeClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': None,
            'max_depth': None,
        },
        'train_score': 0,
        'test_score': 0,
    },    
    {
        'name': 'Decision Tree Classifier',
        'Classifier': DecisionTreeClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 420,
            'max_depth': 10,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Decision Tree Classifier',
        'Classifier': DecisionTreeClassifier,
        'dataset': 'balanced',
        'params': {
            'random_state': 42,
            'max_depth': 20,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Decision Tree Classifier',
        'Classifier': DecisionTreeClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 42,
            'max_depth': 30,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Random Forest Classifier',
        'Classifier': RandomForestClassifier,
        'dataset': 'balanced',
        'params': {
            'random_state': 42,
            'max_depth': None,
            'n_jobs': -1
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Random Forest Classifier',
        'Classifier': RandomForestClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 42,
            'max_depth': None,
            'n_jobs': -1
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Random Forest Classifier',
        'Classifier': RandomForestClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 420,
            'max_depth': 10,
            'n_jobs': -1
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Random Forest Classifier',
        'Classifier': RandomForestClassifier,
        'dataset': 'balanced',
        'params': {
            'random_state': 42,
            'max_depth': 20,
            'n_jobs': -1
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Random Forest Classifier',
        'Classifier': RandomForestClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 42,
            'max_depth': 30,
            'n_jobs': -1
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'MLP Classifier',
        'Classifier': MLPClassifier,
        'dataset': 'balanced',
        'params': {
            'random_state': 420,
            'hidden_layer_sizes': (3, 1),
            'solver': 'lbfgs',
            'alpha': 0.001,
            'max_iter': 100,
            'early_stopping': True,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'MLP Classifier',
        'Classifier': MLPClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 420,
            'hidden_layer_sizes': (3, 1),
            'solver': 'lbfgs',
            'alpha': 0.001,
            'max_iter': 100,
            'early_stopping': True,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'MLP Classifier',
        'Classifier': MLPClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 420,
            'hidden_layer_sizes': (2, 1),
            'solver': 'adam',
            'alpha': 0.00001,
            'max_iter': 100,
            'early_stopping': True,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'MLP Classifier',
        'Classifier': MLPClassifier,
        'dataset': 'balanced',
        'params': {
            'random_state': 420,
            'hidden_layer_sizes': (2, 1),
            'solver': 'sgd',
            'alpha': 0.0001,
            'learning_rate': 'adaptive',
            'max_iter': 200,
            'early_stopping': True,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'MLP Classifier',
        'Classifier': MLPClassifier,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 42,
            'hidden_layer_sizes': (3, 1),
            'solver': 'lbfgs',
            'alpha': 0.001,
            'max_iter': 200,
            'early_stopping': True,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Multinomial Logistic Regression',
        'Classifier': LogisticRegression,
        'dataset': 'balanced',
        'params': {
            'random_state': 420,
            'penalty': 'none',
            'solver': 'lbfgs',
            'multi_class': 'multinomial',
            'max_iter': 500,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Multinomial Logistic Regression',
        'Classifier': LogisticRegression,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 420,
            'penalty': 'none',
            'solver': 'lbfgs',
            'multi_class': 'multinomial',
            'max_iter': 500,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Multinomial Logistic Regression',
        'Classifier': LogisticRegression,
        'dataset': 'balanced',
        'params': {
            'random_state': 42,
            'penalty': 'l2',
            'solver': 'lbfgs',
            'multi_class': 'multinomial',
            'max_iter': 500,
        },
        'train_score': 0,
        'test_score': 0,
    },
    {
        'name': 'Multinomial Logistic Regression',
        'Classifier': LogisticRegression,
        'dataset': 'imbalanced',
        'params': {
            'random_state': 42,
            'penalty': 'l2',
            'solver': 'lbfgs',
            'multi_class': 'multinomial',
            'max_iter': 500,
        },
        'train_score': 0,
        'test_score': 0,
    },
]
