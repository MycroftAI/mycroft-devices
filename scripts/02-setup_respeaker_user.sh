#!/bin/sh -x

USER=respeaker
GECOS=respeaker
UGID=32011
PASSWORD=mycroft

DEFGROUPS="tty,sudo,adm,dialout,cdrom,plugdev,audio,dip,video"

echo "I: creating default user $USER"
adduser --gecos $GECOS --disabled-login $USER --uid $UGID

echo "I: set user $USER password to $PASSWORD"
echo "$USER:$PASSWORD" | /usr/sbin/chpasswd

mkdir -p /home/$USER/Music
mkdir -p /home/$USER/Pictures
mkdir -p /home/$USER/Videos
mkdir -p /home/$USER/Downloads
mkdir -p /home/$USER/Documents
chown -R $UGID:$UGID /home/$USER

usermod -a -G ${DEFGROUPS} ${USER}
