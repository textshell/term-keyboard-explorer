Explorations into keyboard responses by linux terminal implementations

Requirements:
=============
* needs to run as root to access /dev/uinput
* needs access to the x server via DISPLAY
* python3-libevdev (libevdev in pypi)

Usage:
======

This is best run in a VM, because it changes keyboard configuration and injects lots of key strokes.

Make sure neither the terminal implementation nor your window manager intercept key strokes.

Run `explorer.py` in a terminal with focus.

Example in a VM
===============
* Setup a VM with buster
* Allow graphical login as root ([possibly like this](https://economictheoryblog.com/2015/11/08/how-to-enable-gui-root-login-in-debian-8/))
* install python3-libevdev and matchbox-window-manager
* setup .xsession
```
matchbox-window-manager -use_titlebar no &

xterm -e /root/startup.sh
```
* and startup.sh
```
#! /bin/bash

echo "auto mode?"
read a
if [ "$a" = "1" ] ; then
    /path/to/term-keyboard-explorer/explorer.py
    echo finished, press any key to logout
    read b
else
    bash
fi
```
* Login as root using .xsession as X11 session script.
