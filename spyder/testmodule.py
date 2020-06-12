# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:19:54 2020

@author: Arles
"""

import sys
sys.path.append("E:\GithubRep\cursoPython\cursopython\spyder\compression")

from compression import filetozip
from compression import filetorar 

filetozip.compresszip('archivo')
filetorar.compressrar('archivo')