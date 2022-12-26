#!/usr/bin/env python
import subprocess
import os

PACKAGES = [
    "mesa",
    "vulkan-mesa-layers",
    "opencl-mesa",
    "lib32-mesa",
    "vulkan-intel",
    "vulkan-radeon",
    "vulkan-swrast",
    "mesa-vdpau",
    "libva-mesa-driver",
]

ARCH = subprocess.run(["uname", "-m"], capture_output=True, text=True).stdout.strip()
URL_PREFIX = f"https://archlinux.org/packages/@REPO@/{ARCH}"
URL_SUFFIX = "download"

CACHE_DIR = f"/tmp/package_cache"

# Create the cache directory inside /tmp if it does not exist
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Set permissions to allow the current user to create and modify files in it
os.chmod(CACHE_DIR, 0o755)

# Generate a list of package URLs using a list comprehension
PACKAGES_URL = [
    f"{URL_PREFIX.replace('@REPO@', 'multilib')}/{package}/{URL_SUFFIX}"
    if package.startswith("lib32-")
    else f"{URL_PREFIX.replace('@REPO@', 'extra')}/{package}/{URL_SUFFIX}"
    for package in PACKAGES
    if subprocess.run(["pacman", "-Qi", package], capture_output=True, text=True).returncode == 0
]

# Start the yes command in the background to automatically respond "y" to the prompt
yes_process = subprocess.Popen(["yes", "y"], stdout=subprocess.PIPE)

# Run the pacman command, using the output of the yes command as the input
subprocess.run(
    ["sudo", "pacman", "--cachedir", CACHE_DIR, "-U"] + PACKAGES_URL,
    stdin=yes_process.stdout,
)

# Terminate the yes command
yes_process.terminate()

# Delete the cache directory
subprocess.run(["rm", "-rf", CACHE_DIR])
