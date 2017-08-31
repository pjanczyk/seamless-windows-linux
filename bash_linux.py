# Copyright (C) 2017  Piotr Janczyk
# Connecting to Linux VM using ssh from WSL

import os
import sys
import path_translation

# Config
linux_user = "pj"
linux_hostname = "pj-ubuntu"
linux_shell = "bash"

if len(sys.argv) == 1:
    working_directory = "~"
elif len(sys.argv) == 2 and sys.argv[1] != "--help":
    working_directory = path_translation.windows_to_linux(sys.argv[1])
else:
    print("Usage:  bash-linux [WORKING_DIRECTORY]")
    exit(0)

# There is only 64-bit version of bash.exe (WSL).
# From perspective of 64-bit program it's located in "%windir%\System32\",
# but from perspective of 32-bit program it's located in "%windir%\Sysnative\".
# (see: Windows File System Redirector)
is_64bits = sys.maxsize > 2 ** 32

if is_64bits:
    wsl_bash = r"%windir%\System32\bash.exe"
else:
    wsl_bash = r"%windir%\Sysnative\bash.exe"

command = '{} -c "ssh -t {}@{} \'cd \\"{}\\"; {}\'"'.format(
    wsl_bash, linux_user, linux_hostname, working_directory, linux_shell
)
# e.g. %windir%\System32\bash.exe -c "ssh -t john@192.168.0.2 'cd \"/c/Users/John\"; bash'"

os.system(command)
