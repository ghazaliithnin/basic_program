# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:16:36 2020

@author: user
"""
import glob, os
import pandas as pd

#df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "my_files2*.csv"))))

#print(os.path.isdir("log"))
path = "log"
all_files = glob.glob(os.path.join(path, "*.csv"))

df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)