#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import urllib
import tempfile
import shutil
import zipfile

temp_dir = tempfile.mkdtemp()
data_source = "http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip"
zipname = temp_dir + '/Bike-Sharing-Dataset.zip'
urllib.urlretrieve(data_source, zipname)  # 获取数据

zip_ref = zipfile.ZipFile(zipname, 'r')
zip_ref.extractall(temp_dir)
daily_path = temp_dir + '/day.csv'
daily_data = pd.read_csv(daily_path)
zip_ref.close()

print daily_data.head()