import requests
import numpy as np
import pandas as pd
import timeit as ti

pengUrl = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"

# pengContent = requests.get(pengUrl).content

pengData = pd.read_csv(pengUrl, header=0)
print(pengData)

species = pengData['species'].values
island = pengData['island'].values
bill_length = pengData['bill_length_mm'].values
bill_depth = pengData['bill_depth_mm'].values
flipper_length = pengData['flipper_length_mm'].values
body_mass = pengData['body_mass_g'].values
sex = pengData['sex'].values

# print(gender)

#Doing it now
spec = set(species)
dic = {}

for sp in species:
	dic[sp] = np.nanmean(body_mass[species==sp])

#Or

diction = {sp:np.nanmean(body_mass[species==sp]) for sp in set(species)}

print(diction)


l = [abs(body_mass[i]-dic[species[i]]) for i in range(body_mass.size)]
print(l)



area = [(bill_length[i]*bill_depth[i]*0.5) for i in range(body_mass.size)]
print(area)

gendered = {species[i]:(np.nanmean(body_mass[sex=='male']), np.nanmean(body_mass[sex!='male'])) for i in range(species.size)}
print(gendered)
