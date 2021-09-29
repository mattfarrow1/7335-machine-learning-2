# +-+-+-+-+-+-+-+-+
# |M|L|2| |H|W| |2|
# +-+-+-+-+-+-+-+-+
# Matt Farrow

# Note: this project's code is adapted from the work that Dan Crouthamel & Fabio
# Savorgnan previously did in this class. Although my intention had been to
# re-write the code in my own style as I worked through it, the final product
# bears a much stronger resemblance to the original work than I would like.
#
# https://github.com/bSharpCyclist/MSDS-7335-ML2/blob/main/GridSearch.py

# %%
# ╔══════════╗
#   Libraries
# ╚══════════╝

import numpy as np
import itertools as it
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn import datasets
import matplotlib.pyplot as plt
import json

# Import classifiers
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Import evaluation metrics
# Import Evaluation metrics Classification
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


# %%
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

# %%
# ╔══════════════════════════════╗
#   Define Models & Hyperparameters
# ╚══════════════════════════════╝

# Define the models
# models_list = [RandomForestClassifier, KNeighborsClassifier, SVC]
models_list = {
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

n_folds = 5

data = (M, L, n_folds)


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
            # "f1": f1_score(L[test_index], pred),
            # "precision": precision_score(L[test_index], pred),
            # "recall": recall_score(L[test_index], pred),
        }
    return ret


# def build_clf_dict(results):
#     for key in results:
#         k1 = results[key]["clf"]
#         v1 = results[key]["accuracy"]
#         k1Test = str(k1)

#         k1Test = k1Test.replace("            ", " ")  # remove large spaces from string
#         k1Test = k1Test.replace("          ", " ")
#         if k1Test in clf_accuracy_dict:
#             clf_accuracy_dict[k1Test].append(v1)
#         else:
#             clf_accuracy_dict[k1Test] = [v1]


def build_clf_dict(results_dict):
    clf_accuracy_dict = {}

    for key in results_dict:
        k1 = results_dict[key]["clf"]
        v1 = results_dict[key]["accuracy"]
        k1Test = str(k1)  # Since we have a number of k-folds for each classifier...
        # We want to prevent unique k1 values due to different "key" values
        # when we actually have the same classifer and hyper parameter settings.
        # So, we convert to a string

        # String formatting
        k1Test = k1Test.replace("            ", " ")  # remove large spaces from string
        k1Test = k1Test.replace("          ", " ")

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


# def run_grid_search(models_list, models_and_hypers):
#     for clf in models_list:
#         clf_name = str(clf)

#         for k1, v1 in models_and_hypers.items():
#             if k1 in clf_name:
#                 k2, v2 = zip(*v1.items())
#                 for values in it.product(*v2):
#                     hypers = dict(zip(k2, values))
#                     results = run(clf, data, hypers)
#                     build_clf_dict(results)


def run_grid_search(models_list, models_and_hypers, data, filename=""):
    # define empty dictionaries to start
    np_results = {}
    accuracyDics = {}

    # iterate through the model dictionary to execute each model
    for key, value in models_list.items():
        # just for grins, let the user know which model we're processing
        print("Processing Model: ", key)

        # get the hyper parameter dictionary listings for the specific model
        paramDict = models_and_hypers[key]

        # take our hyper parameter dictionary and use itertools to build out
        # all possible permutations for execution
        keys1, values1 = zip(*paramDict.items())
        paramList = [dict(zip(keys1, v)) for v in it.product(*values1)]

        # iterate through the hyper parameter permutations and execute them
        for dic in paramList:
            # execute the run function on each model type and hyper parameter configuration
            # add the results to the np_results dictionary for use in other methods
            np_results.update(run(value, data, dic))
        # results = run(value, data, dic)

        # find the classifiers for plotting from all the permutations we've run through
        # this will get us to the "best" permutation of results to plot and prevent us
        # from printing 100's of plots
        accuracyDics.update(build_clf_dict(np_results))


# Initialize an empty dictionary for accuracy scores
# clf_accuracy_dict = {}

# run_grid_search(models_list, models_and_hypers)

# # for determining maximum frequency (# of kfolds) for histogram y-axis
# n = max(len(v1) for k1, v1 in clf_accuracy_dict.items())

# # for naming the plots
# filename_prefix = "clf_Histograms_"

# # Set up the plots
# plot_num = 1

# # Adjust matplotlib subplots for easy terminal window viewing
# left = 0.125  # the left side of the subplots of the figure
# right = 0.9  # the right side of the subplots of the figure
# bottom = 0.1  # the bottom of the subplots of the figure
# top = 0.6  # the top of the subplots of the figure
# wspace = 0.2  # the amount of width reserved for space between subplots,
# # expressed as a fraction of the average axis width
# hspace = 0.2  # the amount of height reserved for space between subplots,
# # expressed as a fraction of the average axis height

# for k1, v1 in clf_accuracy_dict.items():
#     fig = plt.figure(figsize=(20, 10))  # This dictates the size of our histograms
#     ax = fig.add_subplot(
#         1, 1, 1
#     )  # As the ax subplot numbers increase here, the plot gets smaller
#     plt.hist(v1, facecolor="green", alpha=0.75)  # create the histogram with the values
#     ax.set_title(k1, fontsize=30)  # increase title fontsize for readability
#     ax.set_xlabel(
#         "Classifer Accuracy (By K-Fold)", fontsize=20
#     )  # increase x-axis label fontsize for readability
#     ax.set_ylabel(
#         "Frequency", fontsize=20
#     )  # increase y-axis label fontsize for readability
#     ax.xaxis.set_ticks(
#         np.arange(0, 1.1, 0.1)
#     )  # The accuracy can only be from 0 to 1 (e.g. 0 or 100%)
#     ax.yaxis.set_ticks(np.arange(0, n + 1, 1))  # n represents the number of k-folds
#     ax.xaxis.set_tick_params(
#         labelsize=20
#     )  # increase x-axis tick fontsize for readability
#     ax.yaxis.set_tick_params(
#         labelsize=20
#     )  # increase y-axis tick fontsize for readability

#     # pass in subplot adjustments from above.
#     plt.subplots_adjust(
#         left=left, right=right, bottom=bottom, top=top, wspace=wspace, hspace=hspace
#     )
#     plot_num_str = str(plot_num)  # convert plot number to string
#     plot_num = plot_num + 1  # increment the plot_num counter by 1
#     plt.savefig("MF Accuracy Scores.png")


def plot_parameters(clf_accuracy_dict, filename="clf_Histograms_"):
    # for naming the plots
    filename_prefix = filename

    # initialize the plot_num counter for incrementing in the loop below
    plot_num = 1

    # Adjust matplotlib subplots for easy terminal window viewing
    left = 0.125  # the left side of the subplots of the figure
    right = 0.9  # the right side of the subplots of the figure
    bottom = 0.1  # the bottom of the subplots of the figure
    top = 0.6  # the top of the subplots of the figure
    wspace = 0.2  # the amount of width reserved for space between subplots,
    # expressed as a fraction of the average axis width
    hspace = 0.2  # the amount of height reserved for space between subplots,
    # expressed as a fraction of the average axis height

    # for determining maximum frequency (# of kfolds) for histogram y-axis
    n = max(len(v1) for k1, v1 in clf_accuracy_dict.items())

    # create the histograms
    # matplotlib is used to create the histograms: https://matplotlib.org/index.html
    for k1, v1 in clf_accuracy_dict.items():
        # for each key in our clf_accuracy_dict, create a new histogram with a given key's values
        fig = plt.figure(figsize=(10, 10))  # This dictates the size of our histograms
        ax = fig.add_subplot(
            1, 1, 1
        )  # As the ax subplot numbers increase here, the plot gets smaller
        plt.hist(
            v1, facecolor="green", alpha=0.75
        )  # create the histogram with the values
        ax.set_title(k1, fontsize=25)  # increase title fontsize for readability
        ax.set_xlabel(
            "Classifer Accuracy (By K-Fold)", fontsize=25
        )  # increase x-axis label fontsize for readability
        ax.set_ylabel(
            "Frequency", fontsize=25
        )  # increase y-axis label fontsize for readability
        ax.xaxis.set_ticks(
            np.arange(0, 1.1, 0.1)
        )  # The accuracy can only be from 0 to 1 (e.g. 0 or 100%)
        ax.yaxis.set_ticks(np.arange(0, n + 1, 1))  # n represents the number of k-folds
        ax.xaxis.set_tick_params(
            labelsize=20
        )  # increase x-axis tick fontsize for readability
        ax.yaxis.set_tick_params(
            labelsize=20
        )  # increase y-axis tick fontsize for readability
        # ax.grid(True) # you can turn this on for a grid, but I think it looks messy here.

        # pass in subplot adjustments from above.
        plt.subplots_adjust(
            left=left, right=right, bottom=bottom, top=top, wspace=wspace, hspace=hspace
        )
        plot_num_str = str(plot_num)  # convert plot number to string
        filename = (
            filename_prefix + plot_num_str
        )  # concatenate the filename prefix and the plot_num_str
        plt.savefig(
            filename, bbox_inches="tight"
        )  # save the plot to the user's working directory
        plot_num = plot_num + 1  # increment the plot_num counter by 1
    plt.show()


run_grid_search(models_list, models_and_hypers, data, "MF_clf_Histograms_")

# # %%
# # ╔═════════════════╗
# #   Create gridsearch
# # ╚═════════════════╝
# class death_to_gridsearch(object):

#     # Declare the instance of the object of our gridsearch
#     def __init__(self, M, L, parameters={}, metrics=[]):
#         self.M = M  # equivalent to X, defined on line 31
#         self.L = L  # equivalent to y, defined on line 32
#         self.parameters = parameters  # model hyperparameters
#         self.metrics = metrics  # scoring metrics
#         self.grid_results = []  # create a list for our results
#         self.top_scores = []  # create a list for the top scores
#         self.top_metrics = {
#             k: [] for k in metrics
#         }  # dictionary that contains a list of the top metrics

#         # Initialize the top_scores dictionary that will be used when we save
#         # our top performing model results to a JSON file. The dictionary will
#         # contain the classifier and its hyperparameters that performed the
#         # best.
#         for p in parameters:
#             self.top_scores.append(
#                 {
#                     "clf": p,
#                     "top_scores": dict.fromkeys(metrics, 0),
#                     "best_parameters": {k: {} for k in metrics},
#                     "top_parameters": {k: {} for k in metrics},
#                 }
#             )

#         # Initialize the top_metrics dictionary
#         self.top_metrics = {k: [] for k in metrics}

#     # Define the actual grid search
#     def grid_search(self):

#         # Fore each classifier and its associated hyperparameters
#         for model, params in self.parameters.items():

#             # Print out which model is currently running
#             print("")
#             print("Running", model.__name__, "model")

#             # Use the zip() function to create a list of all of the possible
#             # classifier/hyperparameter combinations to test
#             keys, values = zip(*params.items())
#             parameters_to_run = [
#                 dict(zip(keys, value))
#                 for value in it.product(
#                     *values
#                 )  # itertools' product function recommendation from Discord
#             ]

#             # Save the restults to the grid_results list
#             for run_hyper in parameters_to_run:
#                 results = self.__run(model, run_hyper, self.metrics)
#                 self.grid_results.append(results)

#         # For each scoring metric, save the top performing metrics to the
#         # top_scores list
#         for model in self.top_scores:
#             for metric in model["top_scores"]:
#                 self.top_metrics[metric].append(model["top_scores"][metric])
#         return self.top_scores

#     def __run(self, a_clf, clf_hyper={}, clf_metrics={}):
#         clf = a_clf(**clf_hyper)  # unpack the hyperparameters
#         ret = {}

#         # For each metric, calculate a score using 5-fold cross-validation
#         for metric in clf_metrics:
#             scores = cross_val_score(
#                 clf, X=self.M, y=self.L, cv=5, scoring=metric, n_jobs=-1
#             )
#             # ret.update({"clf": clf, "clf_params": clf_hyper, metric: scores})
#             ret.update({"clf": clf, "top_parameters": clf_hyper, metric: scores})

#             # Update our collection of best mean scores
#             mean_score = scores.mean()
#             for model in self.top_scores:
#                 if model["clf"] == a_clf and model["top_scores"][metric] < mean_score:
#                     model["top_scores"][metric] = mean_score
#                     model["best_parameters"][metric] = clf_hyper
#                     model["top_parameters"][metric] = clf_hyper

#         return ret

#     # Print out the metrics scores to the terminal for each classifier along
#     # with their associated hyperparameters
#     def print_scores(self):
#         for model in self.top_scores:
#             print("")
#             print(model["clf"].__name__)

#             for metric in model["top_scores"]:
#                 print(
#                     metric,
#                     "{:.2f}".format(model["top_scores"][metric]),
#                     "-",
#                     model["best_parameters"][metric],
#                     model["top_parameters"][metric],
#                 )

#     # Set up the plots. Using matplotlib, we create for plots, one for each
#     # metric, and plot out the scores for each classifier. This method allows
#     # for a very quick understanding of the model performance, but doesn't show
#     # any great detail - something I might reconsider in the future.
#     def plot_scores(self, save_path):
#         clfs_list = [clf.__name__ for clf in models_and_hypers]
#         num_plots = len(gridsearch.top_metrics)
#         index = 0
#         plt.figure(figsize=(16, 10))
#         for metric in gridsearch.top_metrics:
#             index = index + 1
#             plt.subplot(num_plots, 2, index)
#             plt.title(metric)
#             plt.scatter(clfs_list, gridsearch.top_metrics[metric], s=60, marker="+")
#             plt.savefig(f"{save_path}Top Model Scores.png")
#         plt.tight_layout(h_pad=2)
#         plt.suptitle("Best Scores for Each Model & Metric")
#         plt.show()


# # %%
# # ╔══════════════╗
# #   Run gridsearch
# # ╚══════════════╝
# # Define the metrics we want to test
# metrics = ["accuracy", "f1", "recall", "precision"]

# # Define the gridsearch using our data
# gridsearch = death_to_gridsearch(
#     M=M, L=L, parameters=models_and_hypers, metrics=metrics
# )

# # Run the gridsearch and get the top scores
# top_scores = gridsearch.grid_search()

# # ╔══════════════════╗
# #   Print, Plot & Save
# # ╚══════════════════╝

# # Print and plot the top scores
# gridsearch.print_scores()
# gridsearch.plot_scores(
#     save_path="/Users/mattfarrow/Documents/GitHub/7335-machine-learning-2/Homework/"
# )
# # Save top_scores as a JSON file
# with open("top_scores.json", "w") as fp:
#     json.dump(top_scores, fp, sort_keys=True, indent=4)

# %%
