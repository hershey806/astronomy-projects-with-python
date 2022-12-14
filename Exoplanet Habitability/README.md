## Important Note ##

I worked on this research project as part of the Aspiring Scholars Directed Research Program (ASDRP). Some of the code and methodology presented here is different than what I use at ASDRP due to IP reasons. 

## Introduction

In this project, I analyzed a large database of exoplanets to determine what characteristics of an exoplanet favor habitability. To do this, I first calculated each exoplanet's host star’s bolometric luminosity. I then used the bolometric luminosity to determine the inner and outer bounds of each host star's Circumstellar Habitable Zone (CHZ). Then, I checked each exoplanet to see if its average orbiting distance was within the CHZ of its host star. If it was, I deemed the exoplanet to be habitable. I then analyzed several key attributes of the habitable exoplanets visually using histograms. Using the histograms, I was able to either support or reject my initial hypothesis about the characteristics of habitable exoplanets. 

To learn more about my methodology and the theoretical aspect of project, please read through the sources listed below; the most important formulas - those used to determine the CHZ - come from Tom Morris's book "The Principals of Planetary Biology."

For more information about my code, please see the ***CHZ_code.py*** file. I added comments to explain each step of the process.

For more information about how I created the histograms, please see the ***Charts.ipynb*** notebook. 

## Data

The main source of data for this research project was the NASA Exoplanet Archive: ***https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS***. I was not able to put the dataset in Github because it was too large. However, if you do download the dataset and run my code on it, please note that you may get slightly different results because the dataset is regularly updated, and the results I obtained were from the July 2022 version of the dataset. 

***full_dataset_with_habitability.csv*** contains the entire dataset with the columns added from my code (the last 6 columns: Standard Absolute Magnitude, Bolometric Magnitude, Bolometric Luminosity, Inner CHZ Bound, Outer CHZ Bound, and Habitability). 

***habitable_exoplanets.csv*** contains solely the names of the 55 exoplanets deemed to be habitable by my code. 

***habitable_exoplanets_data.csv*** shows the dataset with all the columns but only for the 55 exoplanets deemed to be habitable. This file was the file I used to generate the histograms in ***Charts.ipynb***. 

## Results

A brief summary of the results of my research (excluding figures) is shown below. 

Total number of unique exoplanets: 5045  
Number number of habitable exoplanets: 55  
Number number of not habitable exoplanets: 880  
Number of exoplanets whose habitability could not be determined (CND): 4110  
Number of exoplanets whose host star's luminosity could not be determined (part of CND): 681

Additionally, in the ***figures*** directory, you can see the figures generated by ***Charts.ipynb***. You may have to click "Download" to view them because of the background color (clicking "Download" won't directly download them; it just takes you to the raw image). 

From Figures 4, 6, and 7, we can see that the majority of the habitable exoplanets had low orbital eccentricities, semi-major axes between 0 and 3 AU, and host stars with relatively low surface temperatures. These all agree with what we would expect; habitable exoplanets should have low orbital eccentricities to ensure that they don't stray out of the CHZ of their host stars. Additionally, habitable exoplanets should have host stars with relatively surface temperatures (like the Sun) to ensure that their surfaces are not too hot to sustain liquid water. 

## Sources

NASA Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS

“Brightness, Magnitudes, and Luminosity: A Tutorial (Prof. Harriet Dinerstein, Ast 307, 4/21/14)”: https://www.as.utexas.edu/astronomy/education/fall15/wheeler/secure/MagnitudeTutorial.pdf

Principles of Planetary Biology Chapter 5: Astronomical Circumstances: https://www.planetarybiology.com/planetarybio_text/07_astronomical_circumstances.pdf

"Transformations from Theoretical Hertzsprung-Russell Diagrams to Color-Magnitude Diagrams: Effective Temperatures, B-V Colors, and Bolometric Corrections": https://ui.adsabs.harvard.edu/abs/1996ApJ...469..355F/abstract
