# +-+-+-+-+-+-+-+-+
# |M|L|2| |H|W| |2|
# +-+-+-+-+-+-+-+-+
# Matt Farrow

# Note: this project's code is adapted from the work that Brandon Croom
# previously did in this class. Although my intention had been to re-write the
# code in my own style as I worked through it, the final product bears a much
# stronger resemblance to the original work than I would like.
#
# https://github.com/jbcroom/DS7335-ML2/blob/master/HW2/DS7335-ML2-Croom-HW2.py

# %%
# ╔══════════╗
#   Libraries
# ╚══════════╝

import numpy as np
import itertools as it
from sklearn.model_selection import KFold
from sklearn import datasets
import matplotlib.pyplot as plt
import json

# Import classifiers
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Import evaluation metrics
from sklearn.metrics import accuracy_score

# ╔════════════╗
#   Define Data
# ╚════════════╝

#  During class and office hours, it was advised that limiting our data to a
#  binary classification would be an easier undertaking than building something
#  that could handle a multi-class classification problem. Therefore, I decided
#  instead to use the breast cancer dataset from sklearn.
cancer = datasets.load_breast_cancer()
M = cancer.data
L = cancer.target

n_folds = 5

data = (M, L, n_folds)

# %%
# ╔══════════════════════════════╗
#   Define Models & Hyperparameters
# ╚══════════════════════════════╝

# Define the models
models_dict = {
    "RandomForestClassifier": RandomForestClassifier,
    "KNeighborsClassifier": KNeighborsClassifier,
    "SVC": SVC,
}

# Define a dictionary containing sub-dictionaries of different models and
# their associated hyperparameters.
models_and_hypers = {
    "RandomForestClassifier": {
        "n_estimators": [100, 200, 500, 1000],
        "max_features": ["auto", "sqrt", "log2"],
        "bootstrap": [True],
        "criterion": ["gini", "entropy"],
        "oob_score": [True, False],
    },
    "KNeighborsClassifier": {
        "n_neighbors": np.arange(3, 15),
        "weights": ["uniform", "distance"],
        "algorithm": ["ball_tree", "kd_tree", "brute"],
    },
    "SVC": {"kernel": ["linear", "poly", "rbf"], "degree": [1, 3, 5]},
}

# %%
# ╔════════════╗
#   Define: run
# ╚════════════╝


def run(a_clf, data, clf_hyper={}):
    M, L, n_folds = data  # Unpack data container
    kf = KFold(n_splits=n_folds)  # Establish the cross validation
    ret = {}  # Classic explication of results

    for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
        clf = a_clf(**clf_hyper)  # unpack parameters into clf is they exist
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
# ╔═════════════════════════╗
#   Define: build_clf_acc_dict
# ╚═════════════════════════╝


def build_clf_acc_dict(results_dict):
    clf_accuracy_dict = {}

    for key in results_dict:
        k1 = results_dict[key]["clf"]
        v1 = results_dict[key]["accuracy"]
        k1Test = str(k1)

        # String formatting
        # k1Test = k1Test.replace("            ", " ")  # remove large spaces from string
        # k1Test = k1Test.replace("          ", " ")
        k1Test = re.sub("\s\s+", " ", k1Test)

        # Then check if the string value 'k1Test' exists as a key in the dictionary
        if k1Test in clf_accuracy_dict:
            clf_accuracy_dict[k1Test].append(
                v1
            )  # append the values to create an array (techically a list) of values
        else:
            clf_accuracy_dict[k1Test] = [
                v1
            ]  # create a new key (k1Test) in clf_accuracy_dict with a new value, (v1)

    return clf_accuracy_dict


# %%
# ╔══════════════════════╗
#   Define: run_grid_search
# ╚══════════════════════╝


def run_grid_search(models_dict, hyperparameter_dict, data, filename=""):
    # Define empty dictionaries to start
    np_results = {}
    gs_accuracy = {}

    # Iterate through the model dictionary to execute each model
    for key, value in models_dict.items():

        print("Processing Model: ", key)

        # Get the hyperparameter dictionary listings for the specific model
        paramDict = hyperparameter_dict[key]

        # Use iterpools' product function to build out all possible
        # hyperparameter permutations
        keys1, values1 = zip(*paramDict.items())
        hyper_list = [dict(zip(keys1, v)) for v in it.product(*values1)]

        # Iterate through each permutation from hyper_list and add the results
        # to np_results
        for dic in hyper_list:
            np_results.update(run(value, data, dic))

        # Find the classifiers for plotting from all the permutations we've run through
        # this will get us to the "best" permutation of results to plot and prevent us
        # from printing 100's of plots
        gs_accuracy.update(build_clf_acc_dict(np_results))

        with open("gs_accuracy.json", "w") as fp:
            json.dump(gs_accuracy, fp, sort_keys=True, indent=4)

    # Plot the parameters
    plot_parameters(gs_accuracy, filename)


# %%
# ╔══════════════════════╗
#   Define: plot_parameters
# ╚══════════════════════╝


def plot_parameters(clf_accuracy_dict, filename="clf_Histograms_"):

    filename_prefix = filename

    # Initialize the plot_num counter for incrementing in the loop below
    plot_num = 1

    # Adjust matplotlib subplots for easy terminal window viewing
    left = 0.125
    right = 0.9
    bottom = 0.1
    top = 0.6
    wspace = 0.2
    hspace = 0.2

    # Determine the maximum number of K-folds for the y-axes
    n = max(len(v1) for k1, v1 in clf_accuracy_dict.items())

    # Create the plots
    for k1, v1 in clf_accuracy_dict.items():

        # For each key in our clf_accuracy_dict, create a new histogram with a given key's values
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(
            1, 1, 1
        )  # As the ax subplot numbers increase here, the plot gets smaller
        plt.hist(v1, facecolor="lightblue")
        ax.set_title(k1, fontsize=25, wrap=True)
        ax.set_xlabel("Classifer Accuracy (By K-Fold)", fontsize=15)
        ax.set_ylabel("Frequency", fontsize=15)
        # Accuracy is represented on a 0 to 1 scale (e.g. 0 or 100%)
        ax.xaxis.set_ticks(np.arange(0, 1.1, 0.1))
        ax.yaxis.set_ticks(np.arange(0, n + 1, 1))  # n represents the number of k-folds
        ax.xaxis.set_tick_params(labelsize=10)
        ax.yaxis.set_tick_params(labelsize=10)
        # Pass in the subplot adjustments from above
        plt.subplots_adjust(
            left=left, right=right, bottom=bottom, top=top, wspace=wspace, hspace=hspace
        )
        plot_num_str = str(plot_num)
        filename = filename_prefix + plot_num_str
        plt.savefig(filename, bbox_inches="tight")
        plot_num = plot_num + 1
    plt.show()


# %%
# ╔═══════════════╗
#   Run grid_search
# ╚═══════════════╝

run_grid_search(models_dict, models_and_hypers, data, "MF_clf_Histograms_")

# %%
