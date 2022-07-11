# -*- coding: utf-8 -*-
import os
import glob
import time
from typing import Iterable, List
from webbrowser import get

def get_dir() -> str:
    return os.path.sep.join(__file__.split(os.path.sep)[:-1])

def get_scripts(directory: str) -> List[str]:
    return glob.glob(os.path.join(directory, '**', '*.ahk'), recursive=True)

if __name__ == '__main__':
    for i in get_scripts(get_dir()):
        os.system(i)