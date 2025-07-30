FROM ubuntu:24.04

ARG UNAME="dotfiler"

RUN apt-get update \
    && apt-get install -y python3 python3-pip curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash ${UNAME}
USER ${UNAME}
WORKDIR /home/${UNAME}
