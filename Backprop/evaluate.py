"""
This file serves as a evaluation interface for the network
"""
# Built in
import os
import sys
sys.path.append('../utils/')
# Torch

# Own
import flag_reader
from class_wrapper import Network
from model_maker import Backprop
from utils import data_reader
from utils.helper_functions import load_flags
from utils.evaluation_helper import plotMSELossDistrib
# Libs
import numpy as np
import matplotlib.pyplot as plt


def evaluate_from_model(model_dir, multi_flag=False):

    """
    Evaluating interface. 1. Retreive the flags 2. get data 3. initialize network 4. eval
    :param model_dir: The folder to retrieve the model
    :return: None
    """
    # Retrieve the flag object
    print("Retrieving flag object for parameters")
    if (model_dir.startswith("models")):
        model_dir = model_dir[7:]
        print("after removing prefix models/, now model_dir is:", model_dir)
    flags = load_flags(os.path.join("models", model_dir))
    flags.eval_model = eval_flags.eval_model                    # Reset the eval mode
    flags.batch_size = 1                            # For backprop eval mode, batchsize is always 1
    flags.lr = 0.05
    flags.eval_batch_size = eval_flags.eval_batch_size
    flags.train_step = eval_flags.train_step

    # Get the data
    train_loader, test_loader = data_reader.read_data(flags)
    print("Making network now")

    # Make Network
    ntwk = Network(Backprop, flags, train_loader, test_loader, inference_mode=True, saved_model=flags.eval_model)
    print("number of trainable parameters is :")
    pytorch_total_params = sum(p.numel() for p in ntwk.model.parameters() if p.requires_grad)
    print(pytorch_total_params)
    # Evaluation process
    print("Start eval now:")
    if multi_flag:
        pred_file, truth_file = ntwk.evaluate(save_dir='/work/sr365/multi_eval/Backprop/sine_wave', save_all=True)
    else:
        pred_file, truth_file = ntwk.evaluate()

    # Plot the MSE distribution
    plotMSELossDistrib(pred_file, truth_file, flags)
    print("Evaluation finished")


def evaluate_all(models_dir="models"):
    """
    This function evaluate all the models in the models/. directory
    :return: None
    """
    for file in os.listdir(models_dir):
        if os.path.isfile(os.path.join(models_dir, file, 'flags.obj')):
            evaluate_from_model(os.path.join(models_dir, file))
    return None


if __name__ == '__main__':
    # Read the flag, however only the flags.eval_model is used and others are not used
    eval_flags = flag_reader.read_flag()

    print(eval_flags.eval_model)
    # Call the evaluate function from model
    #evaluate_all()
    evaluate_from_model(eval_flags.eval_model, multi_flag=True)
    #evaluate_from_model(eval_flags.eval_model)

