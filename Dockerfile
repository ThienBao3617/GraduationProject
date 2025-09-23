# UBUNTU 24.04 jammy as base image
FROM ubuntu:22.04

# Set up global environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV LIBGL_ALWAYS_SOFTWARE=1
ENV DISPLAY=:0

# Update and install basic tools and GUI libs
RUN apt-get update && apt-get install -y \
    sudo \
    curl \
    wget \
    gnupg2 \
    lsb-release \
    build-essential \
    bash-completion \
    vim \
    nano \
    git \
    zip \
    x11-apps \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxcb1 \
    libxcb-xinerama0 \
    libxkbcommon-x11-0 \
    libgl1 \
    libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

# Initialize user
RUN useradd -ms /bin/bash skytold && \
    echo "skytold ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Grant ownership for docker
ARG UID=1000
ARG GID=1000
RUN getent group skytold || groupadd -g $GID skytold \
    && id -u skytold || useradd -m -u $UID -g $GID skytold
USER skytold

# Set up working directory
WORKDIR /home/skytold
RUN mkdir -p /home/skytold/workspace
VOLUME ["/home/skytold/workspace"]