# This is no longer necessary - Manjaro has released a repository with MESA nonfree. Follow instructions [here](https://mesa-freeworld.github.io/mesa-nonfree/).


# MUR: MESA Unattended Recovery

## This is a simple python script that can be used to download Mesa packages directly from Arch Linux servers to an installation of Manjaro. The original objective is to return proprietary codecs that Manjaro as an enterprise distribution cannot ship due to restrictive licences and codecs. The inspiration for the project comes from the mesa-freeworld package from the RPM Fusion repository, which attempts to address the missing hardware codecs for AMD graphics cards.

## Be aware of this before running this script for the first time: It was developed to be as automated as possible to be used eventually later in a graphical interface. When running the script, the downloaded files will be temporarily stored in /tmp and deleted once the script has finished.

## Instructions:
1. Download the file `mur` from the [repository](https://github.com/clmbtti/mur/releases).
2. Make executable with: `chmod +x ./mur`
3. Run it with: `./mur`

## Tip: If you are going to save this script on your personal computer in order to readily invoke it as a command in a terminal window, then make sure that the file has "execute permission" as instructed earlier, and that it resides in ~/.local/bin, which on Manjaro is part of your ${PATH}. To accomplish that, follow the next two steps:
4. Move the file to ~/.local/bin using: `mv mur ~/.local/bin/`
5. Now you can run `mur` from any terminal window by just typing its name.
