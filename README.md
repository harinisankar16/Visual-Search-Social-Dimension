# bcog_200 Project Abstract 

## Abstract

In everyday life, we encounter a variety of faces and make inferences about objective (such as age and gender) and subjective attributes (such as trustworthiness). Although the subjective judgements are often inacurate, these subjectives attributes are almost instantaneously and often implictly inferred from faces, and may influence our interactions and behaviour (Peterson et. al., 2022). Now, imagine you are at a party and are trying to find someone to strike a conversation with; amongst the sea of unfamiliar faces, who would you approach? What informs the decision you make during such a search. 

Earlier research has shown that more objective attributes of faces such as race and age can be used as features in a visual search task (Craig & Lipp, 2018; Levin, 2000). The evidence suggests that emotional expressions can also been used as features for search and the some studies show that happy faces are found more quickly than angry faces (Becker et. al., 2011). There is also research that shows an interaction between race and emotion in a visual search paradigm (Otten, 2016). However, it is not known if more implicit and subjective attributes that can be gleaned from faces can be used to inform visual search. 

In this project I will be using faces that vary on social dimensions, particularly trustworthiness and dominance. The face images will be created using a model that is able to generate faces and vary them along various social dimensions. Since the dimensions I am interested in is trustworthiness and dominance, artificial face images that vary on these two dimensions are used as stimuli. Other attributes that might influence the search due to variation in low-level features are controlled for. This stimuli presented in a visual search paradigm will be used to explore whether these social dimensions can be used as features that can be searched for. If this information can be used during a visual search task, we expect the time taken to find the target to increase along with increase in the set size of the search display. If such a search is not possible, the response time would be higher across set sizes and the accuracy of the search would also be low. Additionally, it would be interesting to see if there are asymmetries in response time based on whether the task is to find trustworthy faces amongst untrustworthy faces or vice versa. 

## Implementation plan
#### Functions/class methods to create 
✅ - done ; ✴️ - currently in progress 
- Location of images to be displayed
    - to find the position on the screen to present the faces at ✅
    - the display should be such that the face images are presented along the circumference of a circle with radius R(✅)
    - and the faces are equidistant from each other (and not overlapping) (✅)
    - this changes with the set size of the display, therefore a function to calculate those locations based on the set size is needed (✴️)
- Randomizers that can randomly select
    - the faces from the list of available faces according to the target and distractor valence (trustworthy or untrustworthy) (✅)
    - set size of the display (and consequently the image positions as described above) (✴️)
    - the location at which the target face is presented (✅)
    - the location of the target dot besides the face - left or right side of the face
    - selecting distractor type for a given trial or a block of trials (✴️ - currently hardcoded, needs to be automated)
        - i.e if the target is a trustworthy face, the distractors have to be either neutral or untrustworthy
        - vice versa for untrustworthy faces. 
        - once the target type is selected, only select images from outside of that type.
        - unsure of the level at which this is to be implemented (trial or block level) 
- Target dot placement
    - a function to find the specific face marker locations from the database containing the image name and the location of the markers
    - converts the location from the coordinate system that cv2 uses to the coordinate system that PsychoPy Uses
    - converts the pixel locations to degree units 
    - draws a dot at a set distance from that location 
- response collection 
    - function that records the key response 
    - and the response time (current time - time at the onset of the display of the trial)
    - saves data about the participant ID, trial type(whether the target was trustworthy or untrustworthy), correct target location (or correct response), set size, reaction time, current date, experiment start and end time 
#### Classes to create
- Display 
    - sets the size of the display
    - viewing distance
    - color of the display
    - units of measurement 
    - initializes a monitor with these parameters
- Instructions
    - reads in the text from the instructions.txt
    - present the instructions at the start of the experiment 
    - display break and end experiment messages
- Targets
    - sets the size of target
    - sets the location
    - finds and places target dot at specified location 
- Trial 
    - displays the screen for one trial 
    - based on the parameters from the Target class
    - starts the timer for the response on each trial and ends when valid key response is made
    - Key response
    - sets valid keys for response (e.g. "f" if the target dot is on the left side of the face and "J" if its on the right side of the face)
    - record key response
    - record response time

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

## Available files
### test_experiment.py
- skeleton script that displays 12 faces (1 trustworthy target, untrustworthy distractors)
- download stim_folder onto same location as the script to access images 
- download test_data.csv onto same location as script
- To run: open script on psychopy coder and hit run (toggle to pilot mode so no data files are saved)
- press any key to exit display 

### test_data.csv
- Has the metadata of the images in test_images and the coordinate positions of the face markers that will be later used to draw the target dot next to the faces. 

### stimuli/test_images
- In lieu of uploading the full stimuli folder to this public repository, this is a selected sample that can be used to run test_experiment.py. 
- This means that the randomizer will only be able to select images within this folder and currently only contains 1 trustworthy target ( so changing the target valence in the code to untrustworthy will not work) - This will change in the future! 




## References

Becker, D. V., Anderson, U. S., Mortensen, C. R., Neufeld, S. L., & Neel, R. (2011). The face in the crowd effect unconfounded: Happy faces, not angry faces, are more efficiently detected in single- and multiple-target visual search tasks. Journal of Experimental Psychology: General, 140(4), 637–659. https://doi.org/10.1037/a0024060
Craig, B. M., & Lipp, O. V. (2018). The relationship between visual search and categorization of own- and other-age faces. British Journal of Psychology, 109(4), 736–757. https://doi.org/10.1111/bjop.12297
Levin, D. T. (2000). Race as a Visual Feature: Using Visual Search and Perceptual Discrimination Tasks to Understand Face Categories and the Cross-Race Recognition Deficit. Journal of Experimental Psychology: General, 129(4), 559–574. https://doi.org/10.10371/0096-3445.129.4.559
Otten, M. (2016). Race Guides Attention in Visual Search. PLOS ONE, 11(2), e0149158. https://doi.org/10.1371/journal.pone.0149158
Peterson, J., Griffiths, T., Uddenberg, S., Todorov, A., & Suchow, J. W. (2022). Deep models of superficial face judgments. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.4041458

