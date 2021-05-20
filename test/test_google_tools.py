import pandas as pd
import numpy as np
import os

os.chdir("../")

from src.hill_cg.hill import *
from notebooks.google_or_tools_tsp import *



dat = pd.read_csv("https://raw.githubusercontent.com/optimizacion-2-2021-1-gh-classroom/practica-2-segunda-parte-jlrzarcor/main/datasets/tsp.csv")
dat1 = dat.to_numpy()
ciudades = dat1[0:10, :]

# Distancia de nuestro de método
hc_best_dist = best_solution(ciudades)


# Distancia de Google OR-tools
tsp_sol = main(ciudades)

test = 1 - hc_best_dist[0]/tsp_sol

def test_distance():
     assert test < 1e-1
