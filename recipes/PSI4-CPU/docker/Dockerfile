# Dockerfile for PSI4 via conda install

FROM ubuntu:14.04
MAINTAINER Chris J.T. Auld <https://github.com/Azure/batch-shipyard>

# Apt install some developer pre-reqs
RUN apt-get update && \
    apt-get install -y libc-dev

#
# Download and install miniconda
#
ADD http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh /root/
WORKDIR /root

RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda && \
	rm Miniconda3-latest-Linux-x86_64.sh

ENV PATH /miniconda/bin/:$PATH

#
# Update conda, add psi4 conda repository and install gcc-5 and then psi4 via conda
#
RUN \
	conda update --yes --all && \
	conda config --add channels http://conda.anaconda.org/psi4 && \
	conda install --yes gcc-5 && \
    conda install --yes -c psi4 psi4


