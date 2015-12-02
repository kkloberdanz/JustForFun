#!/bin/bash

xrandr | grep maximum

gtf 1440 900 59.9

xrandr --newmode "1440x900_59.90"  106.29  1440 1520 1672 1904  900 901 904 932  -HSync +Vsync

xrandr --addmode DVI-0 1440x900_59.90

xrandr --output DVI-0 --mode 1440x900_59.90
