# PSI4-CPU
This recipe shows how to run [PSI4](http://www.psicode.org) on
a single node using CPU only. This uses the [Anaconda](https://docs.anaconda.com/) packaging mechanism to deploy PSI4 and as such is using pre-built binaries.

## Configuration
Please see refer to this [set of sample configuration files](./config) for
this recipe.

### Pool Configuration
The pool configuration should enable the following properties:
* `max_tasks_per_node` should be set to 1 or omitted. Under the sample configuration the job specifies running `nproc` number of threads for OpenMP and MKL. i.e. The job should saturate the machine resources. You may instead elect to change the threads assigned per job and run multiple tasks per note.

Other pool properties such as `publisher`, `offer`, `sku`, `vm_size` and
`vm_count` can be set to your desired values. PSI4 does not currently provide native GU support.

### Global Configuration
The global configuration should set the following properties:
* `docker_images` array must have a reference to a valid image with PSI4 installed. A docker image is provided [cauldnz/psi4](https://hub.docker.com/r/cauldnz/psi4/) and the [Dockerfile](./docker) is avilable too.

### Jobs Configuration
The jobs configuration should set the following properties within the `tasks`
array which should have a task definition containing:
* `image` should be the name of the Docker image for this container invocation,
e.g., `cauldnz/psi4`
* `command` should contain the command to pass to the Docker run invocation.
We provide an example showing both the input/output `Psithon` file and Python `PsiAPI` call semantics.

## Dockerfile and supplementary files
The `docker` image used is [here](https://hub.docker.com/r/cauldnz/psi4/) and is a non-automated push of the [Docker](./docker) file in this repo. We provide botn an `input.dat` command file and a Python script in [scripts](./scripts). These both run a Hartree–Fock SCF computation for the water molecule using a cc-pVDZ basis set per the [PSI4 Tutorial](http://www.psicode.org/psi4manual/1.1/index_tutorials.html)

You must agree to the following licenses prior to use:
* [PSI4] (http://www.psicode.org/psi4manual/1.1/introduction.html#license)
* [Miniconda] (https://conda.io/docs/license.html)
