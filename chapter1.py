# Chapter 1 : Pytorch installation

import torch
import numpy as np

# print("hello pytorch")
# print(torch.cuda.is_available())

# chapter 2 part
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5, device=device)
    y = torch.ones(5)
    y = y.to(device)
    z = x + y
    print(z)
    #z.numpy()          # can only handle cpu tensor
    z = z.to("cpu")
