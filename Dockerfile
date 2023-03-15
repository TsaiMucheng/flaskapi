FROM continuumio/anaconda3:2021.04

# RUN apt-get update \
#   && apt-get install -y --no-install-recommends iputils-ping telnet vim nano gnupg wget git zip\
#   && apt-get autoremove -yqq --purge \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*

ARG APP_PATH
WORKDIR $APP_PATH
COPY . $APP_PATH
RUN conda env create -f "./environment.yml"