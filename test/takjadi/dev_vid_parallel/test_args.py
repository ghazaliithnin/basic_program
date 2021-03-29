# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:21:02 2020

@author: user
"""
import cv2
import sys
import time
import argparse
import numpy as np
import subprocess as sp
import multiprocessing as mp

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", default="Kiiara.mp4", type=str)
parser.add_argument("--x264", default=False, type=bool)
parser.add_argument("--extension", choices=["mp4", "avi", "mkv"], default="avi")
parser.add_argument("--extra_flags", default="", type=str)

args = parser.parse_args()