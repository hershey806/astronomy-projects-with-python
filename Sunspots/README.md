# Exploring the Theory Behind Sunspots and Utilizing Them to Determine the Rotation Period of the Sun

## Overview of Project

In this project, I explored one of the Sun's most recognizable features: sunspots. Sunspots are areas on the Sun's photosphere that are darker and cooler than their surroudings. Monitoring sunspots allows us to understand how and why solar flares occur. In this project, however, I analyzed the motion of sunspots primarily to determine how the Sun's rotation period changes with latitude. 

My project consisted of three main parts:

1. I tracked the x and y coordinates of several sunspots and created a graph of their motion over time. I used this graph to calculate the rotational period of the Sun at various latitudes. You can find more details about my code and methodology in the ***sunspots.ipynb*** notebook. 

2. I explored the theory and mathematics behind the movement of sunspots. Specifically, I determined which power functions best approximate the movement of sunspots. This data was used in the ***sunspotsAuto.py*** script to determine whether or not to accept a sunspot track. You can find more details about my code and methodology in the ***theorySunspots1.ipynb*** and ***theorySunspots2.ipynb*** notebooks. 

3. I created a machine learning algorithm to automatically detect and track sunspots. You can find more details about my code and methodology in the ***sunspotsAuto.py*** file (which uses code from the ***stara.py*** file). 

## Data and Figures

The main source of data I used for this project was images of the Sun captured by the HMI instrument on SDO. I retrieved these images using the Fido object from in sunpy.net (https://docs.sunpy.org/en/stable/guide/acquiring_data/fido.html#fido-guide). You can see the FITS files of these images in the ***Sun Images*** directory. 



## Conclusion and Significance
