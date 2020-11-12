# Mycroft devices

This repo contains [debos](https://github.com/go-debos/debos) recipes for building Mycroft installation images.

## Available recipes

- mycroft-mark-2-rpi4-ubuntu.yml: Mycroft Mark-2 image based on Ubuntu 20.04. This aims to be stable and allow reproducable builds.
- mycroft-mark-2-rpi4-neon.yml: Mycroft Mark-2 image based on KDE neon repositories. This is an "unstable" build using the latest and greatest version of packages available.
- mycroft-picroft.yml: Placeholder for a future automatic Picroft build.

## Build instructions

This will detail the build instructions using the debos docker, if you wish instructions for running debos natively can be found in the [official readme](https://github.com/go-debos/debos#sypnosis)


Fetch the debos docker container

```
docker pull godebos/debos
```

The docker needs some special access so the docker commandline becomes

```sh
docker run --rm --device /dev/kvm --user $(id -u) \
           --group-add=$(getent group kvm | cut -d : -f 3) \
           --workdir /recipes \
           --mount "type=bind,source=$(pwd),destination=/recipes" \
           --security-opt label=disable godebos/debos \
           -e ROOT_DEV:/dev/sda2 \
           RECIPE \
           -m 7450M
```

Where:
- `/dev/sda2` defines the root device, in this case booting from USB
- `RECIPE` is one of the listed recipes above (ex mycroft-mark-2-rpi4-ubuntu.yml)
- `-m` flag defines memory limit allocated to the Docker container
