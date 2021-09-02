# Chapter 10 : Softmax function and Cross Entropy

# Softmax function
# used for classification neural network

import torch
import torch.nn as nn
import numpy as np

# calculate softmax using numpy
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis = 0)

x = np.array([2.0, 1.0, 0.1])
outputs = softmax(x)
print("softmax numpy:", outputs)


# calculate softmax in PyTorch
x = torch.tensor([2.0, 1.0, 0.1])
outputs = torch.softmax(x, dim = 0)
print(outputs)



# Notes:
# Sigmoid => used in single class classification
# softmax => used in binary class classification
# cross entropy => binary and multi class classification


