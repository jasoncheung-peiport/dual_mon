# Run Program in Linux

Move to the program directory

    cd peiport/dual_mon/

Activate Venv

    conda activate dual

Run Script

    python main.py

# Python Version

    3.12.7

# Dependencies

    opencv-python

    screeninfo

    python-vlc

    pyinstaller

# Convert Python to exe (Pyinstaller)

    pyinstaller --onefile --windowed --icon=peiport_logo.ico --name "peiport" main.py

# Pi Setup

## Hide the idle mouse

1.  Install unclutter

        sudo apt install unclutter

2.  cd to the autostart file

    The path to the autostart file might vary across different operating systems.

        sudo nano /etc/xdg/lxsession/rpd-x/autostart

3.  Add @unclutter command to the file

    adjust the idle time. (-idle 1 -> 1 second)

        @unclutter -idle 5 -root

4.  Save and Exit

    Overwrite

        Ctrl + O

    Agree

        Enter

    Exit

        Ctrl + X

5.  Restart

        sudo reboot

6.  Error Handling

    unclutter: could not open display

        DISPLAY=:0.0 ; export DISPLAY

## Hide the Taskbar

    sudo nano .config/lxpanel-pi/panels/panel

set autohide from 0 to 1

    autohide=1

# Git Commands

## Clone project

    git clone https://github.com/jasoncheung-peiport/dual_mon.git

## Discard all changes

    git reset --hard

## Update from origin

    git pull origin
