# H2O-CPU
This recipe shows how to run [H2O](https://www.h2o.ai/) on
a single node using CPU only. This uses the daily build of the H2O 'Deepwater' branch which supports GPU acceleration and various pre-built DNN models. 

## Configuration
Please see refer to this [set of sample configuration files](./config) for
this recipe.

### Pool Configuration
The pool configuration should enable the following properties:
* `max_tasks_per_node` must be set to 1 or omitted

Other pool properties such as `publisher`, `offer`, `sku`, `vm_size` and
`vm_count` can be set to your desired values.

### Global Configuration
The global configuration should set the following properties:
* `docker_images` array must have a reference to a valid H2O CPU-enabled
Docker image. [opsh2oai/h2o-deepwater](https://github.com/h2oai/deepwater#pre-release-docker-image) can
be used for this recipe.

### Jobs Configuration
The jobs configuration should set the following properties within the `tasks`
array which should have a task definition containing:
* `image` should be the name of the Docker image for this container invocation,
e.g., `opsh2oai/h2o-deepwater`
* `command` should contain the command to pass to the Docker run invocation.
We provide an example which uses a `le-net` convolutional neural network to train over a sample dataset. The `H2O` instance is launched as part of the Python script that is executed. Note the use of the `"gpu": true` flag in the job-config.

## H2O Diagnostics
if you are running the job interactively then in most cases you should execute the job tailing `stdout.txt`. If you are having issues then you can also change to tailing `stderr.txt` to help diagnose. This is because H2O within Python writes to both depending on whether it is logging normal vs. error state conditions. 

## Dockerfile and supplementary files
The `docker` image is the standard `H2O Deepwater` daily build. Details can be found [here](https://github.com/h2oai/deepwater#pre-release-docker-image).
The `lenet-demo.py` script is based off one of the `Deepwater` unit test [scripts](https://github.com/h2oai/h2o-3/tree/master/h2o-py/tests/testdir_algos/deepwater). It trains a [Le-net CNN](http://deeplearning.net/tutorial/lenet.html) over the [cat-dog-mouse dataset](https://h2o-public-test-data.s3.amazonaws.com/bigdata/laptop/deepwater/imagenet/cat_dog_mouse.tgz)

You must agree to the Apache 2.0 [H2O License](https://github.com/h2oai/h2o-3/blob/master/LICENSE)
prior to use.
