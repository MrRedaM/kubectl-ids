#!/bin/bash

sudo apt update
sudo apt install python3-pip -y
pip install kubernetes
#sudo ln -s /usr/bin/python3 /usr/bin/python
sudo chmod +x ./kubectl-ids.py
sudo cp ./kubectl-ids.py /usr/local/bin/kubectl-ids