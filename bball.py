import pybaseball as pyball
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pybaseball import statcast
data = statcast(start_dt='2017-06-24', end_dt='2017-06-27')
print(data.head(2).to_string())
#f = open("C:/Users/214090/Documents/Workbench/baseball/pyball.csv", "w")
#f.write(data.head(2).to_csv())
#f.close()
j = open("C:/Users/214090/Documents/Workbench/baseball/pyball.json","w")
j.write(data.to_json())
j.close()
#pitching_data = pyball.team_pitching(1900,2016)
#print("data shape: {}").format(pitching_data.shape)
#
#print(pitching_data.head())