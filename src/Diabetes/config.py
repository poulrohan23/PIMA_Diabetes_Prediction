from pathlib import Path
import numpy
import pandas as pd
import seaborn as sns
import matplotlib as plt
import tensorflow


data_dir_raw = Path(C:\Users\poulr\PycharmProjects\Diabetes\data\diabetes.csv')
data_diabetes = pd.read_csv(data_dir_raw / 'diabetes.csv')