#!../../env/bin/python

#import janitor
import matplotlib.pyplot as plt
import missingno
import numpy as np
import pandas as pd
import pyreadr
import seaborn as sns
import session_info
import upsetplot

sns.set(
    rc = {
        "figure.figsize": (10, 10)
    }
)

sns.set_style("whitegrid")

raw = "../data/raw"

pima_indians_diabetes = pd.read_csv(f"{raw}/diabetes.csv")
riskfactors = pyreadr.read_r(f"{raw}/riskfactors.rda")['riskfactors']
pedestrian =  pyreadr.read_r(f"{raw}/pedestrian.rda")['pedestrian']
oceanbuoys = pyreadr.read_r(f"{raw}/oceanbuoys.rda")['oceanbuoys']