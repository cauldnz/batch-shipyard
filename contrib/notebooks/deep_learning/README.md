# Distributed Deep Learning with Batch Shipyard
Deep learning has proven to provide state of the art results across many
domains. To really take advantage of deep learning you need to be able to
train your network on GPUs and even better on a cluster of GPUs. The
orchestration necessary to distribute the work combined with the
dependencies of deep learning frameworks can prove cumbersome and can take
up considerable time. In this tutorial we will take you through some simple
examples on how to use Batch Shipyard for deep learning. We will start
with a simple single node case and expand to doing a hyperparameter search
across multiple nodes.

The tutorial is given in the form of Jupyter notebooks. You can follow
using the free [Azure notebooks](https://notebooks.azure.com) service and
either uploading the notebooks from this repo or simply cloning the
notebooks from [here](https://notebooks.azure.com/masalvar/libraries/ddlwbs).
You can also clone the repository and run them locally on your own Jupyter
notebook server. We will be using [CNTK](https://github.com/Microsoft/CNTK)
in this tutorial but Batch Shipyard can be used with any deep learning
framework.

The tutorial is split into 9 sections. These are:

- [`01_Setup`](01_Setup.ipynb): Here we introduce Batch Shipyard, setup all
the necessary Azure resources using the
[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) and
allocate our pool of compute nodes
- [`02_Single_GPU_Training`](02_Single_GPU_Training.ipynb): In this tutorial
we cover how to train a simple convolution neural network on a single node
- [`03_Scoring_model`](03_Scoring_model.ipynb): Here we will use the
previously trained model to score data in the notebook environment but also
on a node in our pool
- [`04_Parameter_Sweep`](04_Parameter_Sweep.ipynb): In this tutorial we
cover a small parameter sweep scenario where we will pass different
hyperparameters to each of the models and evaluate their performance
- [`05_Advanced_Auto_Model_Selection`](05_Advanced_Auto_Model_Selection.ipynb):
In Batch Shipyard it is possible to create tasks that are dependant on the
results of other tasks. In this notebook we carry out a parameter sweep but
this time the results are evaluated in a task rather than all the results
being downloaded to the notebook and being evaluated there.
- [`06_Advanced_Tensorboard`](06_Advanced_Tensorboard.ipynb): Demonstrates
the use of Tensorboard
- [`07_Advanced_Parallel_and_Distributed`](07_Advanced_Parallel_and_Distributed.ipynb):
Trains a DNN using data parallelism across multiple nodes using MPI.
- [`08_Keras_Single_GPU_Training_With_Tensorflow`](08_Keras_Single_GPU_Training_With_Tensorflow.ipynb):
Batch Shipyard is Deep learning framework agnostic. In this notebook we
train a DNN using Keras and Tensorflow.
- [`09_Clean_Up`](09_Clean_Up.ipynb): Finally we will deallocate the pool
we created and delete all the resources we allocated in Azure
