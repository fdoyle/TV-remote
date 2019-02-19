#!/usr/bin/env bash
sudo apt-get install libcec-dev build-essential python-dev
pip3 install --user git+https://github.com/trainman419/python-cec.git@0.2.7#egg=cec
pip3 install websockets
pip3 install sqlitedict
pip3 install netifaces