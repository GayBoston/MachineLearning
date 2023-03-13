import requests
import numpy as np
import pandas as pd
import timeit as ti
import matplotlib.pyplot as plt
import sklearn

pengUrl = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"


pengData = pd.read_csv(pengUrl, header=0)
print(pengData)

species = pengData['species'].values
island = pengData['island'].values
bill_length = pengData['bill_length_mm'].values
bill_depth = pengData['bill_depth_mm'].values
flipper_length = pengData['flipper_length_mm'].values
body_mass = pengData['body_mass_g'].values
sex = pengData['sex'].values

plt.figure(figsize=(6,2))
for s in set(species):
	plt.plot(bill_length[species==s], bill_depth[species==s], 'o', label=s)
plt.legend()
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Width (mm)")
plt.show()