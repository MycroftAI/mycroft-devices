UGID=32011
USER=pine

# Unpack mycroft-core-setup-aarch64.tar.gz to user home
tar -xzf /var/tmp/mycroft-core-setup-aarch64.tar.gz -C /home/$USER/
rm /var/tmp/mycroft-core-setup-aarch64.tar.gz

mkdir -p /opt/mycroft/skills
mkdir -p /var/log/mycroft
mkdir -p /home/$USER/.mycroft
chown -R $UGID:$UGID /home/$USER
chown -R $UGID:$UGID /opt/mycroft
chown -R $UGID:$UGID /var/log/mycroft


# Install mimic
dpkg --install /var/tmp/mimic-arm64_1.2.0.2+1559651054-1.deb
