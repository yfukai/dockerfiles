FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl build-essential git && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv ~/.cargo/bin/uv /usr/local/bin/uv && \
    apt-get purge -y curl build-essential git && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN uv venv && uv pip install marimo