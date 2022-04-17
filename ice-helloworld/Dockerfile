FROM ubuntu:16.04 as build

ARG DEBIAN_FRONTEND=noninteractive

# Installing ZeroC Ice
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv B6391CB2CFBA643D && \
    echo "deb http://download.zeroc.com/Ice/3.7/ubuntu16.04 stable main" > /etc/apt/sources.list.d/ice.list && \
    apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y zeroc-ice-all-dev=3.7.7-* && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install base utilities
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

# Installing conda-pack
RUN conda update python -y && \
    conda install -y conda-pack && \
    conda clean -a

RUN mkdir -p /home/code

COPY environment.yml environment-dev.yml Hello.ice /home/code/

# Creating conda environments
RUN conda env create -n apps -f /home/code/environment.yml && \
    conda-pack -n apps -o /tmp/env.tar && \
    mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
    /venv/bin/conda-unpack && \
    rm /tmp/env.tar && \
    conda env update -n apps -f /home/code/environment-dev.yml && \
    conda-pack -n apps -o /tmp/env.tar && \
    mkdir /venv-dev && cd /venv-dev && tar -xf /tmp/env.tar && \
    /venv-dev/bin/conda-unpack && \
    rm /tmp/env.tar && \
    conda env remove -n apps && \
    conda clean -a

ENV PATH="/venv-dev/bin:${PATH}"

# Compiling slice file
RUN cd /home/code && \
    slice2py Hello.ice && \
    PYTHONDONTWRITEBYTECODE=1 python -c 'import Demo'

ENV PYTHONPATH="/home/code:${PYTHONPATH}"

FROM ubuntu:16.04 as runtime

ARG DEBIAN_FRONTEND=noninteractive

# Installing ZeroC Ice
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv B6391CB2CFBA643D && \
    echo "deb http://download.zeroc.com/Ice/3.7/ubuntu16.04 stable main" > /etc/apt/sources.list.d/ice.list && \
    apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y python3-zeroc-ice=3.7.7-* && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=build /venv/ /venv/
COPY --from=build /home/code/ /dependencies/
ENV PATH="/venv/bin:${PATH}"
ENV PYTHONPATH="/dependencies/:${PYTHONPATH}"

COPY client.py server.py /app/

WORKDIR /app
