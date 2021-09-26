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

# ╔═════════════════════╗
# ║      Instructions     ║
# ╚═════════════════════╝

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

# ╔═════════════════════╗
# ║   Define Objectives   ║
# ╚═════════════════════╝

# Inputs
# list or dictionary of classifiers and hyperparameters

# For each classifier:

# build a hyperparameter grid (sklearn function help - ParameterGrid)

# for each parameter set:

# set the model parameters

# (model.set_params(**params_dict))

# cross-fold validate (make this a fuction)

# store score (returned at the end of the function)

# %%
# ╔═════════════════════╗
# ║        Setup          ║
# ╚═════════════════════╝

import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import re

#  During class and office hours, it was advised that limiting our data to a
#  binary classification would be an easier undertaking than building something
#  that could handle a multi-class classification problem. I'd intended to use
#  the iris dataset, but it has three classes. I'll limit the data to only two
#  classes instead.
iris = datasets.load_iris()
M = iris.data[50:]  #
L = iris.target[50:]

# Define the number of folds
n_folds = 5

# Define 'data'
data = (M, L, n_folds)

# %%
# ╔══════════════════════╗
# ║Models & Hyperparameters║
# ╚══════════════════════╝

# Define the initial set of models we want to compare as a dictionary. Because
# this is a dictionary we can add/remove as needed.
model_dict = {
    "RandomForestClassifier": RandomForestClassifier,
    "KNeighboursClassifier": KNeighborsClassifier,
    "LogisticRegression": LogisticRegression,
}

# Define the optimization parameters for the models above.
model_params_dict = {
    "RandomForestClassifier": {
        "n_estimators": [100, 200, 500, 1000],
        "max_features": ["auto", "sqrt", "log2"],
        "bootstrap": [True],
        "criterion": ["gini", "entropy"],
        "oob_score": [True, False],
    },
    "KNeighboursClassifier": {
        "n_neighbors": np.arange(3, 15),
        "weights": ["uniform", "distance"],
        "algorithm": ["ball_tree", "kd_tree", "brute"],
    },
    "LogisticRegression": {
        "solver": ["newton-cg", "sag", "lbfgs"],
        "multi_class": ["ovr", "multinomial"],
    },
}

# %%
# ╔══════════════════════╗
# ║ Define: run            ║
# ╚══════════════════════╝
#
# This code was provided as part of the instructions for the assignment.
def run(a_clf, data, clf_hyper={}):
    M, L, n_folds = data  # Unpack data container
    kf = KFold(n_splits=n_folds)  # Establish the cross-validation
    ret = {}  # Classic explication of results

    for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
        clf = a_clf(**clf_hyper)  # Dictionary unpacking

        clf.fit(M[train_index], L[train_index])

        pred = clf.predict(M[test_index])

        ret[ids] = {
            "clf": clf,
            "train_index": train_index,
            "test_index": test_index,
            "accuracy": accuracy_score(L[test_index], pred),
        }

    return ret


# %%
# ╔══════════════════════╗
# ║ Define: plots          ║
# ╚══════════════════════╝


def plot_parameters(accuracy_dict, filename="Model_Histograms_"):

    # define filename parameters
    filename_prefix = filename
    plot_num = 1

    # Determine the maximum number of k-folds for each histogram y-axis
    n = max(len(v_i) for k_i, v_i in accuracy_dict.items())

    # Create the histograms using matplotlib
    # For each key in accuracy_dict, we'll create a new histogram with a given
    # key's values
    for k_i, v_i in accuracy_dict.items():

        # Define the plot size
        fig = plt.figure(figsize=(10, 10))

        # Create the histograms
        plt.hist(v_i, facecolor="skyblue")

        # Set tick marks
        plt.xticks(np.arange(0, 1.1, 0.1))
        plt.yticks(np.arange(0, n + 1, 1))

        # Set title and axis parameters
        plt.title(k_i, fontsize=18)
        plt.xlabel("Classifer Accuracy (By K-Fold)", fontsize=14)
        plt.ylabel("Frequency", fontsize=14)

        # Define plot names and numbers
        plot_num_str = str(plot_num)
        filename = filename_prefix + plot_num_str
        plt.savefig(filename, bbox_inches="tight")
        plot_num = plot_num + 1

    plt.show()


# %%
# ╔══════════════════════════╗
# ║Define: group classifiers ║
# ╚══════════════════════════╝


def best_classifiers(results_dict):
    accuracy_dict = {}

    for key in results_dict:
        k_i = results_dict[key]["clf"]
        v_i = results_dict[key]["accuracy"]
        k_iTest = str(k_i)

        # Remove extra spaces from k_iTest
        k_iTest = re.sub("\s\s+", " ", k_iTest)

        # Check if the string value 'k_iTest' exists as a key in the dictionary
        if k_iTest in accuracy_dict:
            accuracy_dict[k_iTest].append(
                v_i
            )  # append the values to create an array (techically a list) of values
        else:
            accuracy_dict[k_iTest] = [
                v_i
            ]  # create a new key (k_iTest) in accuracy_dict with a new value, (v_i)

    return accuracy_dict


# %%
# ╔═══════════════════════════════╗
# ║Define: hyperparameter search  ║
# ╚═══════════════════════════════╝


def hyper_search(model_dict, param_dict, data, filename=""):
    # define empty dictionaries to start
    np_results = {}
    accuracyDics = {}

    # iterate through the model dictionary to execute each model
    for key, value in model_dict.items():
        # Let the user know which model we're processing
        print("Processing Model: ", key)

        # Get the hyperparameter dictionary listings for the specific model
        paramDict = param_dict[key]

        # Use itertools to build out all possible hyperparameter permutations
        # for execution
        keys1, values1 = zip(*paramDict.items())
        paramList = [dict(zip(keys1, v)) for v in itertools.product(*values1)]

        # iterate through the hyper parameter permutations and execute them
        for dic in paramList:
            # execute the run function on each model type and hyper parameter configuration
            # add the results to the np_results dictionary for use in other methods
            np_results.update(run(value, data, dic))
        # results = run(value, data, dic)

        # find the classifiers for plotting from all the permutations we've run through
        # this will get us to the "best" permutation of results to plot and prevent us
        # from printing 100's of plots
        accuracyDics.update(best_classifiers(np_results))

    # plot the parameters
    plot_parameters(accuracyDics, filename)


# %%
# ╔═══════════════╗
# ║Run gridsearch ║
# ╚═══════════════╝
hyper_search(model_dict, model_params_dict, data, "MF_Model_Histograms_")

# %%
