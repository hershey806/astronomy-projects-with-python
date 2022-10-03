# Exploring the Theory Behind Sunspots and Utilizing Them to Determine the Rotation Period of the Sun

## Overview of Project

In this project, I explored one of the Sun's most recognizable features: sunspots. Sunspots are areas on the Sun's photosphere that are darker and cooler than their surroudings. Monitoring sunspots allows us to understand how and why solar flares occur. In this project, however, I analyzed the motion of sunspots primarily to determine how the Sun's rotation period changes with latitude. 

My project consisted of three main parts:

1. I tracked the x and y coordinates of several sunspots and created a graph of their motion over time. I used this graph to calculate the rotational period of the Sun at various latitudes. You can find more details about my code and methodology in the ***sunspots.ipynb*** notebook. 

2. I explored the theory and mathematics behind the movement of sunspots. Specifically, I determined which power functions best approximate the movement of sunspots. This data was used in the ***sunspotsAuto.py*** script to determine whether or not to accept a sunspot track. You can find more details about my code and methodology in the ***theorySunspots1.ipynb*** and ***theorySunspots2.ipynb*** notebooks. 

3. I created a machine learning algorithm to automatically detect and track sunspots. You can find more details about my code and methodology in the ***sunspotsAuto.py*** file (which uses code from the ***stara.py*** file). 

## Data and Figures

The main source of data I used for this project was images of the Sun captured by the HMI instrument on SDO. I retrieved these images using the Fido object from in sunpy.net (https://docs.sunpy.org/en/stable/guide/acquiring_data/fido.html#fido-guide). You can see the FITS files of these images in the ***Sun Images*** directory. 

***SunspotsData.pdf*** contains a table showing the rotation period of the Sun at various latitudes that I calculated. The values come from the calculations performed in ***sunspots.ipynb***. 

The ***data*** directory contains the data files used in the machine learning part of my project (***sunspotsAuto.py***). 

Finally, the ***figures*** directory contains images and GIFS created from the code in the notebooks. 

## Conclusion and Significance

The main purpose of this project was to estimate the Sun's rotation period at various latitudes. I was able to successfully accomplish this; you can see the results of my code in ***SunspotsData.pdf***. This part of the project was not coding-intensive, but rather more mathematical in nature. That being said, I became with more proficient with astronomy packages such as SunPy while working on this project. I also learned a lot about the mathematical theory behind the motion of sunspots. 

The hardest part of this project was the automation of sunspot detection (***sunspotsAuto.py***). Prior to this project, I was not very knowledgeable in machine learning, but I was really interested in the idea of being able to automatically identify sunspots. I thus looked into object detection with Python, and eventually decided to use scikit-learn DBS clustering. You can see the results of my algorithm in the ***sunspotsTracked*** gif in the ***figures*** directory. My algorithim was pretty accurate, but occasionally, a sunspot appeared in one image and disappeared in the next, so perhaps a different clustering algorithim would be better. 
