#imports
from pybaseball import statcast
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# collect Statcast data on all pitches from the months of May and June
data = statcast('2017-05-01', '2017-05-03')
print(data.shape)

data2 = data.dropna(subset=['launch_angle', 'launch_speed', 'estimated_ba_using_speedangle'])
data2.shape
fig, ax = plt.subplots(figsize=(8, 8)) 
sns.despine(fig, left=True, bottom=True)
sns.scatterplot(x="launch_speed", y="launch_angle",
                hue="estimated_ba_using_speedangle", 
                palette='viridis', 
                data=data2, ax=ax)
ax.set_title("Hit probability by Launch Angle and Exit Velocity");

data2['hr'] = data2.events=='home_run'

fig, ax = plt.subplots(figsize=(8, 8))
sns.despine(fig, left=True, bottom=True)
sns.scatterplot(x="launch_speed", y="launch_angle",
                hue="hr", 
                palette='binary', 
                data=data2, ax=ax)
ax.set_title("Home Runs by Launch Angle and Exit Velocity");

data2.groupby(pd.cut(data2.launch_speed, 6)).mean()

groups = data2.groupby(pd.cut(data2.launch_speed, 30))
ax = groups['estimated_woba_using_speedangle'].mean().plot()
ax.set_xlabel('Launch Speed', fontsize=14)
ax.set_ylabel('Expected wOBA Value', fontsize=14);

plt.show()