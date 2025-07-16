import os, sys, shutil
from xdg import BaseDirectory
import xdg.util

print(f"xdg_cache_home: {BaseDirectory.xdg_cache_home}")
print(f"xdg_config_dirs: {BaseDirectory.xdg_config_dirs}")
print(f"xdg_config_home: {BaseDirectory.xdg_config_home}")
print(f"xdg_data_dirs: {BaseDirectory.xdg_data_dirs}")
print(f"xdg_data_home: {BaseDirectory.xdg_data_home}")
print(f"xdg_state_home: {BaseDirectory.xdg_state_home}")

for directory in BaseDirectory.xdg_config_dirs:
    contents = os.listdir(directory)
    for element in contents:
        if "systemd" in element:
            print(element)
            print(contents.index(element))

print(xdg.util.which("ls"))
print(xdg.util.which("zsh"))