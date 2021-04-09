# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:11:01 2021

@author: Employee
"""
import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def gradient_descent(X, y, params, learning_rate, iterations):
    m = len(y)
    
    for i in range(iterations):
        params = params - (learning_rate/m) * (X.T @ (sigmoid(X @ params) - y)) 
        

    return (params)


def predict(X, params):
    return np.round(sigmoid(X @ params))


x = np.atleast_2d(np.linspace(.25, .07, 50)).T
y = np.atleast_2d(np.concatenate((np.ones(25), np.zeros(25)))).T
m=len(y)
X = np.hstack((np.ones((m,1)),x))
n = np.size(X,1)
params = np.zeros((n,1))

iterations = 1500
learning_rate = 0.03

paramsOut = gradient_descent(X,y,params,learning_rate, iterations)


predict(X, paramsOut)


(1 / (1 + np.log(-(X[:,0]*params[0] + X[:,1]*params[1])) ))

params = params - (learning_rate/m) * X.T @ ((1 / (1 + np.log(-(X[:,0]*params[0] + X[:,1]*params[1])))) - y.T).T





y = np.reshape((correctRecord), (-1,1))
x = np.reshape((stimTimRec), (-1,1))
    
    

if len(x[:,0]) < len(x[0,:]):
    x = x.T
if len(y[:,0]) < len(y[0,:]):
    y = y.T








X = np.array([[ 1.     ,     0.2       ],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.19066667],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.18133333],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.172     ],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.16266667],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.15333333],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.144     ],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.13466667],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.12533333],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.116     ],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.10666667],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.09733333],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.088     ],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.07866667],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.06933333],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.68365026],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.68365026],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.68365026],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.68365026],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.68365026],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.68365026],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ],
 [ 1.     ,     0.68365026],
 [ 1.     ,    -0.1       ],
 [ 1.     ,     1.        ]])

correctRecord = []
for ii in range(66):
    if X[ii,1] == 1:
        correctRecord.append(1)
    elif X[ii,1] <0: 
        correctRecord.append(0)
    else:
        correctRecord.append(round(random()))

plt.scatter(X[:,1].T, correctRecord)

weights = sqrt(np.arange(1,len(correctRecord)+1, 1))
weights = weights / sum(weights)
weights = weights * len(correctRecord)
weights = np.atleast_2d(weights).T
y = np.atleast_2d(y).T
X = np.append(X, weights, 1)
X = np.append(X, y, 1)


params = np.array([0,0])
m = len(X[:,1])

iterations = 1500
learning_rate = .03
y = np.array(correctRecord)
for i in range(iterations):
    params = params - (learning_rate/m) * (X.T @ ((1/(1+np.exp(-(X[:,0]*params[0] + X[:,1]*params[1]))))*X[:,2] - y)) 
    
predProbs = (1/(1+np.exp(-(X[:,0]*params[0] + X[:,1]*params[1]))))

plt.scatter(X[:,1], predProbs)          

        if sum(y[len(y)-10:len(y)])>=8:
            curStimTim = curStimTim - .005;                     
        