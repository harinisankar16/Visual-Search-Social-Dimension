# Visual search for faces along social dimensions

![Sample visual search display](harinisankar16/Visual-Search-Social-Dimension/visual_search_display.png)

This repository contains the demo and full version of the visual search across social dimensions experiment
The demos are built using [PsychoPy](https://www.psychopy.org/), a Python library for creating psychology experiments.


## Abstract

In everyday life, we encounter a variety of faces and make inferences about objective (such as age and gender) and subjective attributes (such as trustworthiness). Although the subjective judgements are often inacurate, these subjectives attributes are almost instantaneously and often implictly inferred from faces, and may influence our interactions and behaviour (Peterson et. al., 2022). Now, imagine you are at a party and are trying to find someone to strike a conversation with; amongst the sea of unfamiliar faces, who would you approach? What informs the decision you make during such a search.  

In this project I will be using faces that vary on social dimensions, particularly trustworthiness. The face images will be created using a model that is able to generate faces and vary them along various social dimensions. Other attributes that might influence the search due to variation in low-level features are controlled for. If a person's perceived trustworthiness  can be used during a visual search task, we expect the time taken to find the target to increase along with increase in the set size of the search display. If such a search is not possible, the response time would be higher across set sizes and the accuracy of the search would also be low. Additionally, it would be interesting to see if there are asymmetries in response time based on whether the task is to find trustworthy faces amongst untrustworthy faces or vice versa. 

## Psychopy setup and experiment running 

- install [psychopy](https://www.psychopy.org/download.html) according to your device specification
- open psychopy coder window (by default psychopy opens a builder window, a coder window and a runner window,toggle to the coder window)
- download the experiment and stimuli files following the same structure as this repository
- open the folder using the file browser icon
- you should be able to see all the files and folders as you would in a typical code editor
- select the file you want to run (eg : test_experiment.py) to open the code
- run the file by pressing the green play button.
- psychopy takes a few moments to load and run files so be patient! you will see the experiment window pop up automatically 

#### Alternate setup option  
- You can pip install Psychopy onto your environment and run the experiment directly from your code editor 
However, this is a little tricky to do on recent mac operating systems and does not work as intended
- there are fixes to this issue on the psychopy forums, but if you do not already have psychopy installed and running regularly, it is much easier to use the application version as described above.

## Demo Files 

### test_experiment.py
- simple script that displays 12 faces (1 trustworthy target, untrustworthy distractors)
- download stimuli/test_images 
- download test_data.csv onto the main folder (maintain folder structure from the repository)
- To run: open script on psychopy coder and hit run 
- press any key to exit display 

### test_data.csv
- Has the metadata of the images in test_images and the coordinate positions of the face markers that will be later used to draw the target dot next to the faces. 

### stimuli/test_images
- A smaller subset of the stimuli folder that contains images to run test_experiment.py

## Full experiment files

### full_experiment.py
- runs the full visual search experiment for a specified number of trials and trial condition
- requires stimuli from stimuli/WM_images and stim_data.csv to run
- saves data in the data folder with the date stamp and participant id number 
- before the experiment begins, a small pop up window will prompt you to enter a participant id number. Enter a value to proceed to the experiment.

### config.py
- contains the default configuration data for the psychopy experiment window, trial configuration and setup 

### utils.py
- contains the functions that are called when running the experiment. 
- as of 05-09-25, still working on creating a main.py file to run the experiment and you will see that the full_experiment.py contains all the functions needed for it to run inside it but full_experiment.py can be run without issues. 

### stim_data.csv
- contains the metadata of all the images in stimuli/WM_images and the coordinate positions of the face markers for each image

### data
- stores the output csv file once the experiment is complete. 





## Experiment flow

- Instructions 
- Trials (divided into blocks where the target is either a trustworthy or untrustworthy face)
    -   each trial 
        - random set size 4, 6, 8, 12
        - random target location 
        - random target dot location 
        - present stimuli
        - collect response 
- End experiment 
- Post experiment - data analysis 

## References

- Becker, D. V., Anderson, U. S., Mortensen, C. R., Neufeld, S. L., & Neel, R. (2011). The face in the crowd effect unconfounded: Happy faces, not angry faces, are more efficiently detected in single- and multiple-target visual search tasks. Journal of Experimental Psychology: General, 140(4), 637–659. https://doi.org/10.1037/a0024060
- Craig, B. M., & Lipp, O. V. (2018). The relationship between visual search and categorization of own- and other-age faces. British Journal of Psychology, 109(4), 736–757. https://doi.org/10.1111/bjop.12297
Levin, D. T. (2000). Race as a Visual Feature: Using Visual Search and Perceptual Discrimination Tasks to Understand Face Categories and the Cross-Race Recognition Deficit. Journal of Experimental Psychology: General, 129(4), 559–574. https://doi.org/10.10371/0096-3445.129.4.559
- Otten, M. (2016). Race Guides Attention in Visual Search. PLOS ONE, 11(2), e0149158. https://doi.org/10.1371/journal.pone.0149158
Peterson, J., Griffiths, T., Uddenberg, S., Todorov, A., & Suchow, J. W. (2022). Deep models of superficial face judgments. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.4041458

