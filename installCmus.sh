#!/bin/bash

# This will automate compiling and installing cmus on Fedora
# Run this from the directory with the cmus source code (What was extracted from the .tar file)

# After install, open cmus and type ':set output_plugin=pulse'
#                                   ':add ~/Music'

sudo dnf install ncurses ncurses-devel

sudo dnf install ffmpeg-libs ffmpeg-devel libcue libcue-devel pulseaudio-libs pulseaudio-libs-devel libsamplerate-devel libsamplerate

sudo make clean
sudo ./configure
sudo make 
sudo make install
