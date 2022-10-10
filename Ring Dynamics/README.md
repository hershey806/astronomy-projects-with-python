# Ring Dynamics: Visualizing the Roche limit, Identifying Resonances, and Analyzing Shepherd Moons #

## Overview of Project ##

This project consisted of 3 main parts:

1. I used the ***rebound*** package to visualize an N-body simulation (a simulation of many particles under the influence of gravity and other forces). Specifically, I created a simulation to analyze what happens when a moon approaches the Roche limit of its parent body (Saturn, in this case). This was the main part of this project. You can find more details about my code and methodology in the ***ringDynamics.ipynb*** notebook. 

2. I used a dataset to analyze resonsnces between Saturn's moons ring particles. Using Kepler's Third Law and information about the resonances (ratio of orbital periods), I was able to determine the location of several resonances in Saturn's rings and identify the features that corresponded to them. For example, I determined that the 2:1 resonance with the moon Mimas corresponded to the Cassini Division! You can find more details about my code and methodology in the ***ringDynamics.ipynb*** notebook. 

3. Lastly, I briefly examined the effect of moons on Saturn's rings. I analyzed how Saturn's moons can create bending waves and density waves in its rings, and how some of Saturn's moons act as shepherd moons. 

## Data and Figures ##

I didn't use a specific source of data for the main part of this project; the rebound package had everything I needed to set up the simulation. I was able to "snapshot" the simulation at various stages, after which I combined the images to create a GIF: ***roche_Limit.gif***, which you can find in the ***figures*** directory. 

For the resonances part of this project, I used an existing dataset in the form of a csv. You can find the link to the data in the References section in the ***ringDynamics.ipynb*** notebook. Additionally, I used several labeled images of Saturn's rings, which you can find in the ***figures*** directory, to determine the features at several resonances. 

## Conclusion and Significance ##

The main purpose of this project was to visualize what happens to a moon as it approaches the Roche limit of its parent body. I was able to sucessfully do this using the rebound package; you can see the visualization in the ***rocheLimit.gif*** file in the ***figures*** directory. This project was fairly intensive in terms of both coding and theory; I had to learn how to use a package I was completely unfamiliar with. However, it was definitely worth it because I am happy with how the GIF turned out. 

The other parts of this project (resonances and the effects of moons on rings) were not very challenging, but still fun to explore. I was able to create a table showing the ratios between the orbital periods of pairs of Saturn's moons, and then use this table to identify locations of resonances.  
