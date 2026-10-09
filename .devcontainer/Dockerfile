FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-24.04
USER root

# installing uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN sudo apt update && sudo apt upgrade -y
RUN sudo apt install -y python3 python3-pip git gpg tmux socat

ADD requirements.txt .

RUN uv pip install --break-system-packages --system -r requirements.txt
