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
