# -*- coding: utf-8 -*-
import os
import subprocess
import glob
from typing import List

def get_dir() -> str:
    return os.path.sep.join(__file__.split(os.path.sep)[:-1])

def get_scripts(directory: str) -> List[str]:
    return glob.glob(os.path.join(directory, '**', '*.ahk'), recursive=True)

if __name__ == '__main__':
    cwd = get_dir()
    os.chdir(cwd)
    for i in get_scripts(cwd):
        subprocess.run(f'cmd /k "{i}"')