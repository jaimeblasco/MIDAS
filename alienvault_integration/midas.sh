#!/bin/bash

MIDAS_LAUNCHER="/Users/bsmartt/Dev/MIDAS_dev/midas/launcher.py"
cd ~
mkdir .midas
cd .midas/
echo '[*] Starting MIDAS launcher...'
sudo python $MIDAS_LAUNCHER
echo '[+] MIDAS has finished.'