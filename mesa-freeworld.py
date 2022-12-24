import subprocess

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
    subprocess.run(["sudo", "pacman", "-U", package], check=True, input=bytes("y\n", "utf-8"))
