import sys
import subprocess
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

path = sys.argv[1]

# get all commits from path repository
data = subprocess.check_output(
  f' git --no-pager --git-dir {path}.git log --pretty=format:"%ad" ',
  shell=True,
  universal_newlines=True
)

timeline = np.zeros((7, 53)) # draws a graph with days in a week per weeks in a year
commits = np.zeros((7, 24)) # draws a graph with days in a week per hours in a day

dates = {}
i = 0

for line in data.splitlines():
  dates[i] = datetime.strptime(line, '%a %b %d %X %Y %z') # converts string to date object
  calendar = dates[i].isocalendar() # gets week info as (year, week number, day number)

  realDayNumber = calendar[2] - 1 # isocalender gives numbers with indexes starting from 1
  realWeekNumber = calendar[1] - 1

  timeline[realDayNumber][realWeekNumber] += 1 # adds a point in graph for each commit in week
  commits[realDayNumber][dates[i].hour] += 1 # adds a point in graph for each commit in hour

  i += 1

# draws timeline graph and saves it as an image file
print(timeline)
plt.imshow(timeline)
plt.savefig('timeline.png')

# TODO: draws commits graph and save it as a scatter plot
print(commits)
