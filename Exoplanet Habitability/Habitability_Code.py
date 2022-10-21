#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: harshambardekar
"""

import pandas as pd

import numpy as np

import csv 

df =  pd.read_csv('dataset.csv',low_memory=False)

# Removing exoplanets with a controversial flag of 1

df = df.loc[df['pl_controv_flag'] != 1]

df.reset_index(drop = True, inplace = True)

# Converting the columns with dates to datetime objects so they can be sorted numerically by Pandas

df['rowupdate'] = pd.to_datetime(df['rowupdate'])

df['releasedate'] = pd.to_datetime(df['releasedate'])

# Removing duplicates and only keeping the most recent entry for an exoplanet with multiple entries

df = df.sort_values(by=['rowupdate','releasedate'], ascending=True)

df = df.drop_duplicates(subset=['pl_name'],keep='last')

df.reset_index(drop = True,inplace=True)

# Total number of unique exoplanets

total_number = len(df)

print('Total number of unique exoplanets: {}'.format(total_number))

for i in range(0,len(df)):
    
    # The values for luminosity in the dataset are represented as logs, so
    # if there is a value, the actual luminosity (in solar luminosities)
    # is 10 to the power of that value
    
    if pd.notna(df['st_lum'][i]):
        df['st_lum'][i]=10**(df['st_lum'][i])
        
    # If there's not a luminosity value, but there are stellar radius and
    # temperature values, the luminosity can be calculated using the
    # Stefan-Boltzmann law, with all untis in terms of the Sun's physical
    # parameters (the Sun's temperature is 5778 K and the stellar radius is
    # already in terms of the Sun's radius)
    
    if ((pd.isna(df['st_lum'][i])) & ((pd.notna(df['st_teff'][i])) & (pd.notna(df['st_rad'][i])))):
        df['st_lum'][i]=(df['st_rad'][i]**2) * ((df['st_teff'][i]/5778)**4)
    
    # Otherwise, at least the luminosity and at least one of the stellar radius
    # and stellar temperature are missing, so it is impossible to calculate 
    # the star's luminosity
    
    else:
        pass
    
# After the luminosity calculations have been performed,
# exoplanets with no values for their star's luminosity must be removed

df=df.loc[pd.notna(df['st_lum'])]

df.reset_index(drop = True, inplace = True)

no_lumo = total_number-len(df)

print('Number of exoplanets for which luminosity could not be determined: {}'.format(no_lumo))

# Creating a new column for absolute magnitude, based on the relation
# between absolute magnitude and luminosity
# 4.83 is visual absolute magnitude of the Sun
# and the star's luminosity is already in terms of the Sun's luminosity

df['st_abs_mag'] = 4.83 + (-2.5*np.log10(df['st_lum']))

df['st_spectype']=df['st_spectype'].astype(str)

df['bol_mag'] = 0

# The for loop below adds a bolometric magnitude for the host star of each planet
# BC is the bolometric correction, which is used to convert from absolute magnitude
# visual absolute magnitude to bolometric magnitude
# See the sources for where the bolometric corrections come from

for i in range(0,len(df)):
    BC = 0
    if (df['st_teff'][i] >= 2400 and df['st_teff'][i] <= 3700) or df['st_spectype'][i][0] == 'M':
        BC = -2.0
    elif (df['st_teff'][i] >= 3700 and df['st_teff'][i] <= 5200) or df['st_spectype'][i][0] == 'K':
        BC = -0.8
    elif (df['st_teff'][i] >= 5200 and df['st_teff'][i] <= 6000) or df['st_spectype'][i][0] == 'G':
        BC = -0.4
    elif (df['st_teff'][i] >= 6000 and df['st_teff'][i] <= 7500) or df['st_spectype'][i][0] == 'F':
        BC = -0.15
    elif (df['st_teff'][i] >= 7500 and df['st_teff'][i] <= 10000) or df['st_spectype'][i][0] == 'A':
        BC = -0.3
    elif (df['st_teff'][i] >= 10000 and df['st_teff'][i] <= 30000) or df['st_spectype'][i][0] == 'B':
        BC = -2.0
    df['bol_mag'][i] = df['st_abs_mag'][i] + BC
    
# Creating a new column for BOLOMETRIC luminosity, based on BOLOMETRIC Magnitude
# (This is different from st_lum and st_abs_mag)
# The bolometric luminosity must be used for the CHZ calculations
# 4.74 is the bolometric magnitude of the Sun

df['bol_lum'] = 10**((df['bol_mag']-4.74)/-2.5)

# Defining the inner boundary of the CHZ (formula from Tom Morris)

df['inner_CHZ'] = np.sqrt(df['bol_lum']/1.1)

# Defining the outer boundary of the CHZ (formula from Tom Morris)

df['outer_CHZ'] = np.sqrt(df['bol_lum']/0.53)

# Creating a new column to determine if planets are habitable

df['Habitable'] = None

planets = []

for i in range(0,len(df)):
    
    # First if statement checks if there are values for the planet's 
    # semi-major axis and eccentricity
    
    if ((pd.notna(df['pl_orbsmax'][i])) & (pd.notna(df['pl_orbeccen'][i]))):
        
        # If the eccentricity is less than 0.2, the average distance from the planet
        # to its star can be approximated by its semi-major axis (pl_orbsmax)
        # If the average distance is in the CHZ range, we say the planet is
        # habitable
        
        if df['pl_orbeccen'][i] <= 0.2:
            if ((df['pl_orbsmax'][i] >= df['inner_CHZ'][i]) & (df['pl_orbsmax'][i] <= df['outer_CHZ'][i])):
                df['Habitable'][i] = 'Yes'
                planets.append(df['pl_name'][i])
            else:
                df['Habitable'][i] = 'No'
                
        # If the eccentricity is greater than 0.2, we must use a formula for
        # the average distance (see sources) and then check if this 
        # average distance is in the CHZ range
        
        else:
            avg_dist = df['pl_orbsmax'][i] * (1+((df['pl_orbeccen'][i]**2)/2))
            if ((avg_dist >= df['inner_CHZ'][i]) & (avg_dist <= df['outer_CHZ'][i])):
                df['Habitable'][i] = 'Yes'
                planets.append(df['pl_name'][i])
            else:
                df['Habitable'][i] = 'No'
                
    # If there is no value for the planet's semi-major axis, but there are values
    # for its orbital period, eccentricity, and the star's mass, we can use
    # Kepler's 3rd Law to calculate its semi-major axis, and then perform
    # the eccentricity check again to determine the average orbiting distance
    # and then determine if this average distance is in the CHZ
    
    elif ((pd.isna(df['pl_orbsmax'][i])) & (pd.notna(df['pl_orbeccen'][i])) & (pd.notna(df['pl_orbper'][i])) & (pd.notna(df['st_mass'][i]))):
          
          # Convering the orbital period from days to years
          
          orb_per_year = df['pl_orbper'][i]/365
          
          # Using Kepler's Third Law: T^2/a^3 = 1/M, with T in years, a in AU
          # and M in solar masses, so a = cbrt(T^2 * M)
         
          df['pl_orbsmax'][i] = np.cbrt((orb_per_year**2)*df['st_mass'][i])
          
          if df['pl_orbeccen'][i] <= 0.2:
              if ((df['pl_orbsmax'][i] >= df['inner_CHZ'][i]) & (df['pl_orbsmax'][i] <= df['outer_CHZ'][i])):
                  df['Habitable'][i] = 'Yes'
                  planets.append(df['pl_name'][i])
              else:
                  df['Habitable'][i] = 'No'
        
          else:
              avg_dist = df['pl_orbsmax'][i] * (1+((df['pl_orbeccen'][i]**2)/2))
              if ((avg_dist >= df['inner_CHZ'][i]) & (avg_dist <= df['outer_CHZ'][i])):
                  df['Habitable'][i] = 'Yes'
                  planets.append(df['pl_name'][i])
              else:
                  df['Habitable'][i] = 'No'
    
    # Otherwise, there are too many values missing to determine if the planet
    # is habitable. CND = Can Not Determine
    
    else:
        df['Habitable'][i] = 'CND'
        
df.to_csv('dataset_with_habitability.csv')

habitable_df = df.loc[df['Habitable']=='Yes']
habitable_df.reset_index(drop=True,inplace=True)
number_habitable = len(habitable_df)
print('Number of habitable exoplanets: {}'.format(number_habitable))
habitable_df.to_csv('habitable_data.csv')

not_habitable = df.loc[df['Habitable']=='No']
number_nothabitable = len(not_habitable)
print('Number of not habitable exoplanets: {}'.format(number_nothabitable))

CND = df.loc[df['Habitable']=='CND']
number_CND = len(CND)
print('Number of exoplanets whose habitability could not be determined (including ones missing luminosity): {}'.format(number_CND+no_lumo))


with open('habitable_exoplanets.csv', 'w', newline='') as csvfile:
    fieldnames = ['number', 'pl_name']
    planet_count = 0

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for planet in planets:
        planet_count += 1
        writer.writerow({'number': planet_count, 'pl_name': planet})
