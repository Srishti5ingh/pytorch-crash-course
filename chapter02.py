# Chapter 2 : Tensor Basics

import numpy as np
import torch

#x = torch.empty(1)         # scalar with empty value
#x = torch.empty(3)         # 1D vector with empty values
#x = torch.empty(2,2)       # 2D vector with empty values
#x = torch.rand(2,2)        # 2D vector with random values
#x = torch.ones(2,2)        # 2D array with 1s

#x = torch.ones(2,2, dtype=torch.int)        # 2D array with 1s as int type values
#print(x.dtype)

#x = torch.ones(2,2, dtype=torch.float16)
#print(x.size())

#x = torch.tensor([2.5, 1.2])            # Print list as tensor
#print(x)

# tensor operations
# x = torch.rand(2,2)
# y = torch.rand(2,2)
# print(x)
# print(y)
# z = x+y
# z = torch.add(x,y)
# z = torch.sub(x,y)
# z = torch.mul(x,y)
# z = x / y
# z = torch.div(x,y)
# print(z)

# x = torch.rand(2,2)
# y = torch.rand(2,2)
# y.add_(x)
# y.mul_(x)
# print(y)

# tensor lists
# x = torch.rand(5,3)
# print(x)
# #print(x[1, :])          # all values
# print(x[1, 1].item())


# reshaping tensor
# x = torch.rand(4, 4)
# print(x)
# y = x.view(16)
# print(y)
# y = x.view(-1, 8)
# print(y.size())

# tensor to numpy
# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(b)
#
# a.add_(1)
# print(a)
# print(b)

# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)
#
# a += 1
# print(a)
# print(b)

# variable that needs to be optimized
x = torch.ones(5, requires_grad=True)
print(x)





