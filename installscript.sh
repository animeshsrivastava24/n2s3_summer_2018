#'''This code is a part of the NESSY PROJECT'''
#'''Developed by ANIMESH'''
#INSTALLATION BASH FILE FOR THE REQUIREMENTS OF GUI

# 1. KEEP UBUNTU OR DEBIAN UP TO DATE

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade
sudo apt-get -y autoremove


# 2. INSTALL THE DEPENDENCIES

# Build tools:
sudo apt-get install -y build-essential cmake

# Python:
sudo apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy

# GUI Tkinter:
sudo apt-get install python-tk

