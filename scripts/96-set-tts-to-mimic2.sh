# If the local Mimic2 cache overlay has been included, 
# the default TTS module must be set to mimic2 for it to be used.

USER=gez
# TODO - host this properly
cache_zip_url=''

dir='/opt/mycroft/preloaded_cache/Mimic2'
mkdir -p $dir
pushd $dir
wget $cache_zip_url
unzip Mimic2-local-cache.zip
rm Mimic2-local-cache.zip
popd

/home/$USER/mycroft-core/bin/mycroft-config set tts.module mimic2
