import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv
import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px

df=pd.read_csv("final.csv")


rows = []

with open("final.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
stars_data_rows = rows[1:]

stars_data_rows[1:3]


star = []


for distance in df.Distance:
    if distance == 100:
        star.append(True)
    else:
        star.append(False)
        
is_dist = pd.Series(star)
star_dist=df[is_dist]

star_dist.reset_index(inplace=True,drop=True)
star_dist.head()


star_dist.shape

gravity_star=[]

for i in star_dist.Gravity:
  if i>=150 and i<=350:
    gravity_star.append(True)
  else:
    gravity_star.append(False)
    
print( len(gravity_star))
gravity_star = pd.Series(gravity_star)
final_stars = star_dist[gravity_star]
final_stars.head()

df.to_csv("Filter_stars.csv")
 