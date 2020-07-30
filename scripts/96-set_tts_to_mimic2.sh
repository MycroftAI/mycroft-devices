# If the local Mimic2 cache overlay has been included, 
# the default TTS module must be set to mimic2 for it to be used.

UGID=32011
USER=mycroft

# TODO - host this properly
cache_zip_url='https://frozenmazegames.se/Mimic2-local-cache.zip'

dir='/opt/mycroft/preloaded_cache/Mimic2'
mkdir -p $dir
pushd $dir
wget $cache_zip_url
unzip Mimic2-local-cache.zip
rm Mimic2-local-cache.zip
popd

MYCROFT_CONF_PATH="/home/$USER/.mycroft/mycroft.conf"
(cat $MYCROFT_CONF_PATH || echo "{}") | jq '. + {"tts": {"module": "mimic2"}}' > /tmp/mycroft.conf
cp /tmp/mycroft.conf $MYCROFT_CONF_PATH
chown mycroft:mycroft $MYCROFT_CONF_PATH
