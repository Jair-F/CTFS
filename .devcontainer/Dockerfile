# Force x86_64 platform so Docker Desktop uses Rosetta 2 emulation on Apple Silicon
FROM --platform=linux/amd64 mcr.microsoft.com/vscode/devcontainers/base:ubuntu-24.04
USER root

# Installing uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 1. Enable 32-bit architecture support (i386)
# 2. Install x86 compilation libraries, gdb-multiarch, and qemu-user helpers
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        python3 \
        python3-pip \
        git \
        gpg \
        tmux \
        vim \
        socat \
        ncat \
        gdb \
        gdb-multiarch \
        gcc \
        gcc-multilib \
        g++-multilib \
        libc6:i386 \
        libstdc++6:i386 \
        qemu-user \
        qemu-user-static && \
    rm -rf /var/lib/apt/lists/*

ADD requirements.txt .

# Install pwndbg
RUN curl --proto '=https' --tlsv1.2 -LsSf 'https://install.pwndbg.re' | sh -s -- -t pwndbg-gdb
RUN uv pip install --break-system-packages --system -r requirements.txt