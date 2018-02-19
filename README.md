# insight-donation-analysis
This repository was the focus of a coding challenge for the Insight Fellows Program concerning analysis of political donors. The goal was to take donation data from an encoded data set and be able to extract elements from it as relatets to repeated donations.


The program exits of two python scripts located in the src/ folder. Here you will find donation-analytics.py and register.py

donation-analytics.py is responsible for input and output and provides the needed structures to the code.

register.py had all of the data structures and functions needed to analyse the donation data

The data is read in via one line at a time to be flexable for the data streaming into the program. Each donation is then organized into a data structure for donation and indexed into a hashmap with the key based on the name and zip code. Collisions were manually dealt with by creating a new but repeatable key if two elements collided. 

When two donations are added from the same person, then the code creates a new hashmap to keep track of what donations have come from which zip code at which year to which recipiant. Those 3 terms were thus used as the key and nesassary metrics were accounted for so that they could be printed out in the desired format.

The code relies on 3 standard input text files. First being the Donation data, the second being the percentile desired, and the 3rd being an empty text file to be written to.

As the scaffolding is set up the data and precentile should be located in the Input folder and the file being written to should be in the output folder, but as long as the correct files are linked to the program, their directory locations shouldnt matter.