# +-+-+-+-+-+-+-+-+
# |M|L|2| |H|W| |2|
# +-+-+-+-+-+-+-+-+
# Matt Farrow

# %%
# ╔══════════╗
#   Libraries
# ╚══════════╝

import numpy as np
import itertools as it
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn import datasets
import matplotlib.pyplot as plt
import json

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
models_list = [RandomForestClassifier, KNeighborsClassifier, SVC]

# Define a dictionary containing sub-dictionaries of different models and
# their associated hyperparameters.
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
    SVC: {"kernel": ["linear", "poly", "rbf"], "degree": [1, 3, 5]},
}

# %%
# ╔═════════════════╗
#   Create gridsearch
# ╚═════════════════╝
class death_to_gridsearch(object):

    # Declare the instance of the object of our gridsearch
    def __init__(self, M, L, parameters={}, metrics=[]):
        self.M = M  # equivalent to X, defined on line 31
        self.L = L  # equivalent to y, defined on line 32
        self.parameters = parameters
        self.metrics = metrics
        self.grid_results = []  # create a list for our results
        self.top_scores = []  # create a list for the top scores
        self.top_metrics = {
            k: [] for k in metrics
        }  # create a dictionary that contains a list of the top metrics

        # Initialize the top_scores dictionary that will be used when we save
        # our top performing model results to a JSON file. The dictionary will
        # contain the classifier and its hyperparameters that performed the
        # best.
        for p in parameters:
            self.top_scores.append(
                {
                    "clf": p,
                    "top_scores": dict.fromkeys(metrics, 0),
                    "top_parameters": {k: {} for k in metrics},
                }
            )

        self.top_metrics = {k: [] for k in metrics}

    # Define the actual grid search
    def grid_search(self):

        # Fore each classifier and its associated hyperparameters
        for model, params in self.parameters.items():

            # Print out which model is currently running
            print("")
            print("Running", model.__name__, "model")

            # Use the zip() function to create a list of all of the possible
            # classifier/hyperparameter combinations to test
            keys, values = zip(*params.items())
            parameters_to_run = [
                dict(zip(keys, value)) for value in it.product(*values)
            ]

            # Save the restults to the grid_results list
            for run_hyper in parameters_to_run:
                results = self.__run(model, run_hyper, self.metrics)
                self.grid_results.append(results)

        # For each scoring metric, save the top performing metrics to the
        # top_scores list
        for model in self.top_scores:
            for metric in model["top_scores"]:
                self.top_metrics[metric].append(model["top_scores"][metric])

        return self.top_scores

    def __run(self, a_clf, clf_hyper={}, clf_metrics={}):
        clf = a_clf(**clf_hyper)
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
                    model["top_parameters"][metric] = clf_hyper

        return ret

    # Print out the metrics scores to the terminal for each classifier along
    # with their associated hyperparameters
    def print_scores(self):
        for model in self.top_scores:
            print("")
            print(model["clf"].__name__)

            for metric in model["top_scores"]:
                print(
                    metric,
                    "{:.2f}".format(model["top_scores"][metric]),
                    "-",
                    model["top_parameters"][metric],
                )

    # Set up the plots. Using matplotlib, we create for plots, one for each
    # metric, and plot out the scores for each classifier. This method allows
    # for a very quick understanding of the model performance, but doesn't show
    # any great detail - something I might reconsider in the future.
    def plot_scores(self, save_path):
        clfs_list = [clf.__name__ for clf in models_and_hypers]
        num_plots = len(gridsearch.top_metrics)
        index = 0
        plt.figure(figsize=(16, 10))
        for metric in gridsearch.top_metrics:
            index = index + 1
            plt.subplot(num_plots, 2, index)
            plt.title(metric)
            plt.scatter(clfs_list, gridsearch.top_metrics[metric], s=60, marker="+")
            plt.savefig(f"{save_path}Top Model Scores.png")
        plt.tight_layout(h_pad=2)
        plt.suptitle("Best Scores for Each Model & Metric")
        plt.show()


# %%
# ╔══════════════╗
#   Run gridsearch
# ╚══════════════╝
# Define the metrics we want to test
metrics = ["accuracy", "f1", "recall", "precision"]

# Define the gridsearch using our data
gridsearch = death_to_gridsearch(
    M=M, L=L, parameters=models_and_hypers, metrics=metrics
)

# Run the gridsearch and get the top scores
top_scores = gridsearch.grid_search()

# ╔══════════════════╗
#   Print, Plot & Save
# ╚══════════════════╝

# Print and plot the top scores
gridsearch.print_scores()
gridsearch.plot_scores(
    save_path="/Users/mattfarrow/Documents/GitHub/7335-machine-learning-2/Homework/"
)
# Save top_scores as a JSON file
with open("top_scores.json", "w") as fp:
    json.dump(top_scores, fp, sort_keys=True, indent=4)
