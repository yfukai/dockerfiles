FROM nvidia/cuda:12.3.2-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.12 python3.12-venv python3.12-dev \
    curl git build-essential && \
    ln -s /usr/bin/python3.11 /usr/bin/python3 && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv ~/.cargo/bin/uv /usr/local/bin/uv && \
    apt-get purge -y curl git build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN uv venv && uv pip install marimo

