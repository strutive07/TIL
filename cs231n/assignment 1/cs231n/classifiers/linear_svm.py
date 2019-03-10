import numpy as np
from random import shuffle

def svm_loss_naive(W, X, y, reg):
  """
  Structured SVM loss function, naive implementation (with loops).

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  dW = np.zeros(W.shape) # initialize the gradient as zero

  # compute the loss and the gradient
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  for i in range(num_train):
    scores = X[i].dot(W) # shape : (1, 10)
    correct_class_score = scores[y[i]] # 정답 score
    for j in range(num_classes):
      if j == y[i]:
        continue
      margin = scores[j] - correct_class_score + 1 # note delta = 1
      if margin > 0:
        loss += margin
        dW[:, j] += X[i, :] # analytic gradient for incorrect targets
        dW[:, y[i]] -= X[i, :] # analytic gradient for correct target
     
  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train
    
  # Add regularization to the loss.
  loss += reg * np.sum(W * W)
  dW /= num_train
  dW += reg * W

  return loss, dW


def svm_loss_vectorized(W, X, y, reg):
  """
  Structured SVM loss function, vectorized implementation.

  Inputs and outputs are the same as svm_loss_naive.
  """
  loss = 0.0
  dW = np.zeros(W.shape) # initialize the gradient as zero
  C = W.shape[1]
  N = X.shape[0]
  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the structured SVM loss, storing the    #
  # result in loss.                                                           #
  #############################################################################
    
  scores = np.dot(X, W)    # shape (N, C)
  correct_scores = scores[np.arange(N), y]  # shape (N, )
  margins = np.maximum(scores - correct_scores.reshape(N, 1) + 1.0, 0)  # shape (N, C)
  margins[np.arange(N), y] = 0 # target 제외
  loss = np.sum(margins) / N # 모든 elem 값 더하기
  loss += 0.5 * reg * np.sum(W * W) # regularization
    
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

 

  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the gradient for the structured SVM     #
  # loss, storing the result in dW.                                           #
  #                                                                           #
  # Hint: Instead of computing the gradient from scratch, it may be easier    #
  # to reuse some of the intermediate values that you used to compute the     #
  # loss.                                                                     #
  #############################################################################
  dscores = np.zeros_like(scores)  # (N, C)
  dscores[margins > 0] = 1  
  dscores[np.arange(N), y] -= np.sum(dscores, axis=1)   #  (N, 1) = (N, 1)

  dW = np.dot(X.T, dscores) 
  dW /= N
  dW += reg * W 
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

  return loss, dW
