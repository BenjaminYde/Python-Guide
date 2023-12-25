# Ubuntu 22.04.3 LTS
# Python 3.10.12

FROM ubuntu:22.04
LABEL Author="benjamin.yde@gmail.com"

ENV DEBIAN_FRONTEND="noninteractive"

# Development APT packages
RUN apt -qq update && \
    apt -qq install -y --no-install-recommends \
        apt-utils \
        bash-completion \
        curl \
        git \
        iputils-ping \
        nano \
        openssh-client \
        python-is-python3 \
        python3 \
        python3-pip \
        sudo \
        zsh \
        && \
    apt -qq clean && \
    apt -qq autoclean && \
    apt -qq remove && \
    apt -qq autoremove -y && \
    rm -rf /var/lib/apt/lists

# PIP runtime packages
RUN python3 -m pip install -q --retries 10000 --timeout 60 --no-cache-dir \
    click==8.1.3 \
    ipykernel==6.27.1 \
    requests==2.31.0 \
    Flask==3.0.0
    
# Create User
RUN \
    useradd -u 1000 pythondev && \
    echo "pythondev:pythondev" | chpasswd && \
    adduser pythondev sudo && \
    mkdir -p /home/pythondev && \
    mkdir -p /home/pythondev/Documents && \
    mkdir -p /home/pythondev/Downloads && \
    chown -R pythondev /home/pythondev && \
    printf "\npythondev ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
ENV \
    USER=pythondev \
    PATH=/home/pythondev/.local/bin:$PATH

USER pythondev
WORKDIR /home/pythondev

# ZSH
RUN \
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
    rm .zshrc && \
    touch .zshrc && \
    echo "export ZSH=\"/home/pythondev/.oh-my-zsh\"" >> .zshrc && \
    echo "export ZSH_THEME=\"eastwood\"" >> .zshrc && \
    echo "plugins=(git)" >> .zshrc && \
    echo "source /home/pythondev/.oh-my-zsh/oh-my-zsh.sh" >> .zshrc

ENTRYPOINT ["/usr/bin/zsh"]