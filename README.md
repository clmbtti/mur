# MUR: MESA Unattended Recovery

## This is a simple python script that can be used to download Mesa packages directly from Arch Linux servers to an installation of Manjaro. The original objective is to return proprietary codecs that Manjaro as an enterprise distribution cannot ship due to restrictive licences and codecs. The inspiration for the project comes from the mesa-freeworld package from the RPM Fusion repository, which attempts to address the missing hardware codecs for AMD graphics cards.

## Be aware of this before running this script for the first time: It was developed to be as automated as possible to be used eventually later in a graphical interface. When running the script, the downloaded files will be temporarily stored in /tmp and deleted once the script has finished.

## Instructions:
1. Download the file.
2. Make executable with: `chmod +x ./mur.py`
3. Run it with: `./mur.py`
