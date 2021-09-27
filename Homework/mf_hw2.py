# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                              ┃
# ┃  __  __         _    _            _                      _             ___   ┃
# ┃ |  \/  |__ _ __| |_ (_)_ _  ___  | |   ___ __ _ _ _ _ _ (_)_ _  __ _  |_  )  ┃
# ┃ | |\/| / _` / _| ' \| | ' \/ -_) | |__/ -_) _` | '_| ' \| | ' \/ _` |  / /   ┃
# ┃ |_|  |_\__,_\__|_||_|_|_||_\___| |____\___\__,_|_| |_||_|_|_||_\__, | /___|  ┃
# ┃                                                                |___/         ┃
# ┃                                                                              ┃
# ┃                            +-+-+-+-+-+-+-+-+ +-+                             ┃
# ┃                            |H|o|m|e|w|o|r|k| |2|                             ┃
# ┃                            +-+-+-+-+-+-+-+-+ +-+                             ┃
# ┃                                                                              ┃
# ┃                                 Matt Farrow                                  ┃
# ┃            https://github.com/mattfarrow1/7335-machine-learning-2            ┃
# ┃                                                                              ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# ╔═════════════╗
#   Instructions
# ╚═════════════╝

# This is called DeathToGridSearch because with this example you will never have
# to think about how to manage a large number of classifiers etc simultaneously.
# You will now be able to run and collect results in a very straightforward
# manner. #LongLongLiveGridSearch!

# import numpy as np
# from sklearn.metrics import accuracy_score # other metrics too pls!
# from sklearn.ensemble import RandomForestClassifier # more!
# from sklearn.model_selection import KFold

# Adapt this code below to run your analysis
# 1. Write a function to take a list or dictionary of CLFs and hypers (i.e. use
#    logistic regression), each with 3 different sets of hyperparameters for
#    each
# 2. Expand to include larger number of classifiers and hyperparameter settings
# 3. Find some simple data
# 4. Generate matplotlib plots that will assist in identifying the optimal CLF
#    and parampters settings
# 5. Please set up your code to be run and save the results to the directory
#    that its executed from
# 6. Investigate grid search function

# M = np.array([[1,2],[3,4],[4,5],[4,5],[4,5],[4,5],[4,5],[4,5]])
# L = np.ones(M.shape[0])
# n_folds = 5

# data = (M, L, n_folds)

# def run(a_clf, data, clf_hyper={}):
#   M, L, n_folds = data               # Unpack data container
#   kf = KFold(n_splits=n_folds)       # Establish the cross validation
#   ret = {}                           # Classic explication of results

#   for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
#     clf = a_clf(**clf_hyper) # unpack parameters into clf is they exist
#     clf.fit(M[train_index], L[train_index])
#     pred = clf.predict(M[test_index])
#     ret[ids]= {'clf': clf,
#                'train_index': train_index,
#                'test_index': test_index,
#                'accuracy': accuracy_score(L[test_index], pred)}
#   return ret

# results = run(RandomForestClassifier, data, clf_hyper={})

# ╔══════════════════╗
#   Define Objectives
# ╚══════════════════╝

# Inputs
#   - list or dictionary of classifiers and hyperparameters

# For each classifier:
#   - build a hyperparameter grid (sklearn function help - ParameterGrid)

# for each parameter set:
#   - set the model parameters
#   - (model.set_params(**params_dict))
#   - cross-fold validate (make this a fuction)
#   - store score (returned at the end of the function)

# ╔═══════╗
#   Setup
# ╚═══════╝

import numpy as np
import itertools as it
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
import matplotlib.pyplot as plt

# ╔═════════════════╗
#   Create gridsearch
# ╚═════════════════╝
class death_to_gridsearch(object):
    def __init__(self, M, L, parameters={}, metrics=[]):
        self.M = M
        self.L = L
        self.parameters = parameters
        self.metrics = metrics
        self.grid_results = []
        self.top_scores = []
        self.top_metrics = {k: [] for k in metrics}

        for p in parameters:
            self.top_scores.append(
                {
                    "clf": p,
                    "top_scores": dict.fromkeys(metrics, 0),
                    "best_params": {k: {} for k in metrics},
                }
            )

        # # Create container based on metric
        # # This will be a list of best scores for a given metric, in the order of input classifiers
        # self.top_metrics = {k: [] for k in metrics}

    def grid_search(self):
        for model, params in self.parameters.items():
            print("")
            print("Running", model.__name__, "model")

            keys, values = zip(*params.items())
            parameters_to_run = [
                dict(zip(keys, value)) for value in it.product(*values)
            ]

            for run_hyper in parameters_to_run:
                results = self.__run(model, run_hyper, self.metrics)
                self.grid_results.append(results)

        for model in self.top_scores:
            for metric in model["top_scores"]:
                self.top_metrics[metric].append(model["top_scores"][metric])

        return self.top_scores

    # Our run implementation is a bit different than what was assigned.
    # I changed it to use cross_val_score
    def __run(self, a_clf, clf_hyper={}, clf_metrics={}):
        clf = a_clf(**clf_hyper)  # unpack parameters into clf

        ret = {}

        for metric in clf_metrics:
            scores = cross_val_score(
                clf, X=self.M, y=self.L, cv=5, scoring=metric, n_jobs=-1
            )
            ret.update({"clf": clf, "clf_params": clf_hyper, metric: scores})

            # Update our collection of best mean scores
            mean_score = scores.mean()
            for model in self.top_scores:
                if model["clf"] == a_clf and model["top_scores"][metric] < mean_score:
                    model["top_scores"][metric] = mean_score
                    model["best_params"][metric] = clf_hyper

        return ret

    def print_scores(self):
        for model in self.top_scores:
            print("")
            print(model["clf"].__name__)

            for metric in model["top_scores"]:
                print(
                    metric,
                    "{:.2f}".format(model["top_scores"][metric]),
                    "-",
                    model["best_params"][metric],
                )

    def plot_scores(self, save_path):
        clfs_list = [clf.__name__ for clf in models_and_hypers]
        num_plots = len(gridsearch.top_metrics)
        index = 0
        # Printing two plots side-by-side, so make our figure a rectangle
        plt.figure(figsize=(16, 8))
        for metric in gridsearch.top_metrics:
            index = index + 1
            plt.subplot(num_plots, 2, index)
            plt.title(metric)
            plt.plot(clfs_list, gridsearch.top_metrics[metric])
            plt.savefig(f"{save_path}_Scores.png")
        plt.tight_layout()
        plt.show()


# ╔════════════╗
#   Define Data
# ╚════════════╝

#  During class and office hours, it was advised that limiting our data to a
#  binary classification would be an easier undertaking than building something
#  that could handle a multi-class classification problem. I'd intended to use
#  the iris dataset, but it has three classes. I'll limit the data to only two
#  classes instead.
iris = datasets.load_iris()
M = iris.data[50:]
L = iris.target[50:]

# scaler = StandardScaler()
# scaler.fit(M)
# M_std = scaler.transform(M)

# ╔══════════════════════════════╗
#   Define Models & Hyperparameters
# ╚══════════════════════════════╝

models_and_hypers = {
    RandomForestClassifier: {
        "n_estimators": [100, 200, 500, 1000],
        "max_features": ["auto", "sqrt", "log2"],
        "bootstrap": [True],
        "criterion": ["gini", "entropy"],
        "oob_score": [True, False],
    },
    KNeighborsClassifier: {
        "n_neighbors": np.arange(3, 15),
        "weights": ["uniform", "distance"],
        "algorithm": ["ball_tree", "kd_tree", "brute"],
    },
    LogisticRegression: {
        "solver": ["newton-cg", "sag", "lbfgs"],
        "multi_class": ["ovr", "multinomial"],
    },
}

# Setup the metrics we want to test
metrics = ["accuracy", "roc_auc", "recall", "precision"]

gridsearch = death_to_gridsearch(
    M=M, L=L, parameters=models_and_hypers, metrics=metrics
)
top_scores = gridsearch.grid_search()
gridsearch.print_scores()
gridsearch.plot_scores(
    save_path="/Users/mattfarrow/Documents/GitHub/7335-machine-learning-2/Homework/mf_hw2_files/"
)

# Save top_scores as a pickle file
try:
    import cPickle as pickle
except ImportError:  # Python 3.x
    import pickle

with open("top_scores.p", "wb") as fp:
    pickle.dump(top_scores, fp, protocol=pickle.HIGHEST_PROTOCOL)

# Save top_scores as a JSON file
import json

with open("top_scores.json", "w") as fp:
    json.dump(top_scores, fp, sort_keys=True, indent=4)
