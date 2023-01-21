#!/bin/bash

# Install dependencies
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncursed5-dev xz-utils tk-dev

# Install pyenv
curl https://pyenv.run | bash

# Add pyenv to PATH and initialize
echo 'export PATH="~/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# Update list of available Python versions
pyenv update

# Install Python 3.9
pyenv install 3.9.0

# Set global Python version to 3.9
pyenv global 3.9.0

# Verify installation
python --version

