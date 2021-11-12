#!/usr/local/bin/python3

import os
import subprocess
import shutil
import pandas as pd

# # comment it after already downloaded
#subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True)

df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])

print(f"\nColumns:\n{df.columns}")

#print(f"\nOrganisms:\n{df['#Organism/Name'].unique()}")

print(f"\nGroup:\n{df['Group'].unique()}")
print("We want to have 'Fungi' from the column 'Group'.\n")

print(f"\nSize:\n{df['Size (Mb)'].unique()}\n")

df_fungal_100 = df.loc[df["Group"].str.contains("Fungi")]


df_fungal_100 = df_fungal_100[df_fungal_100["Size (Mb)"].gt(100)]

print(df_fungal_100[["#Organism/Name", "Group", "Size (Mb)"]])

print(f"\nSpecies names:\n{df_fungal_100['#Organism/Name']}\n")
print(f"\nSpecies names:\n{df_fungal_100['#Organism/Name'].unique()}\n")


df_heli = df.loc[df["#Organism/Name"].str.contains("Heliconius")]

print(df_heli["#Organism/Name"])

print(f"How many? > {len(df_heli['#Organism/Name'].unique())} unique")



