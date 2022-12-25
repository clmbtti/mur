import subprocess

# Use the yes command to automatically respond "y" to the prompt
yes_cmd = ["yes"]

# Start the yes command in the background
yes_process = subprocess.Popen(yes_cmd, stdout=subprocess.PIPE)

packages = [
    "https://archlinux.org/packages/extra/x86_64/mesa/download",
    "https://archlinux.org/packages/extra/x86_64/vulkan-mesa-layers/download",
    "https://archlinux.org/packages/extra/x86_64/opencl-mesa/download",
    "https://archlinux.org/packages/multilib/x86_64/lib32-mesa/download",
    "https://archlinux.org/packages/extra/x86_64/vulkan-intel/download",
    "https://archlinux.org/packages/extra/x86_64/vulkan-radeon/download",
    "https://archlinux.org/packages/extra/x86_64/vulkan-swrast/download",
    "https://archlinux.org/packages/extra/x86_64/mesa-vdpau/download",
    "https://archlinux.org/packages/extra/x86_64/libva-mesa-driver/download"
]

for package in packages:
    # Use the `stdin` argument to pass the output of the yes command as the input to pacman
    subprocess.run(["sudo", "pacman", "-U", package], check=True, stdin=yes_process.stdout)

# Terminate the yes command
yes_process.terminate()
