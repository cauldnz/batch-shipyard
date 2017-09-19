from __future__ import print_function
import sys, os
import h2o
from h2o.estimators.deepwater import H2ODeepWaterEstimator

h2o.init()
frame = h2o.import_file(("cat_dog_mouse.csv"))
print(frame.head(5))
model = H2ODeepWaterEstimator(epochs=100, learning_rate=1e-3, network='lenet', score_interval=0, train_samples_per_iteration=1000)
model.train(x=[0],y=1, training_frame=frame)
model.show()
error = model.model_performance(train=True).mean_per_class_error()
print(error)
h2o.remove_all() 