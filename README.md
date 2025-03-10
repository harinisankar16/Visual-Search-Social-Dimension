# bcog_200 Project Abstract 

## Abstract
In everyday life, we encounter a variety of faces and make inferences about objective (such as age and gender) and subjective attributes (such as trustworthiness). Although the subjective judgements are often inacurate, a variety of subjectives attributes are almost instantaneously and often implictly inferred from faces, and may influence our interactions and behaviour(Peterson et. al., 2022). Now, imagine you are at a party and are trying to find someone to strike a conversation with; amongst the sea of unfamiliar faces, who would you approach? What informs the decision you make during such a search. 

Earlier research has shown that more objective features or attributes such as race and age can be used as features in a visual search task with faces(Craig & Lipp (2018), Levin (2000)). The evidence suggests that emotional expressions have also been used as dimensions for search and the some studies show that angry faces are found more quickly than happy faces(Becker et. al., 2011). There is also research that shows an interaction between race and emotion in a visual search paradigm(Otten, 2016). However, it is not known if more implicit and subjective attributes that can be gleaned from faces can be used to inform visual search. 

In this project I will be using faces that vary on social dimensions, such as trustworthiness and dominance, along with a visual search paradigm to explore whether these social dimensions can be used as features that can be searched for. If this information can be used during a visual search task, we expect the time taken to find the target to increase along with increase in the set size of the search display. It would be interesting to see if there are asymmetries in response time based on whether the task is to find trustworthy faces amongst untrustworthy faces or vice versa. 

## Outline of implementation 
In order to create this experimental paradigm on Python,
The face images used in the study is created and retrieved using a model that is able to generate faces and vary them along various social dimensions. Since the dimensions i am interested in is trustworthiness and dominance, I will be generating artificial face images that vary on these two dimensions while controlling for other attributes that might influence the search due to variation in low-level features. 
I will be creating functions such as a image size manipulator that varies the size of the images of the faces shown based on the set size of search display, and another function that calculates the radial location at which the faces should be displayed. 
I will be using python and PsychoPy to create the experiment flow and display that the participant can interact with and collect their key responses from. 
The response data from participants will be stored in dataframes and analysed and visualised using matplotlib.


### References
Becker, D. V., Anderson, U. S., Mortensen, C. R., Neufeld, S. L., & Neel, R. (2011). The face in the crowd effect unconfounded: Happy faces, not angry faces, are more efficiently detected in single- and multiple-target visual search tasks. Journal of Experimental Psychology: General, 140(4), 637–659. https://doi.org/10.1037/a0024060
Craig, B. M., & Lipp, O. V. (2018). The relationship between visual search and categorization of own- and other-age faces. British Journal of Psychology, 109(4), 736–757. https://doi.org/10.1111/bjop.12297
Levin, D. T. (2000). Race as a Visual Feature: Using Visual Search and Perceptual Discrimination Tasks to Understand Face Categories and the Cross-Race Recognition Deficit. Journal of Experimental Psychology: General, 129(4), 559–574. https://doi.org/10.10371/0096-3445.129.4.559
Otten, M. (2016). Race Guides Attention in Visual Search. PLOS ONE, 11(2), e0149158. https://doi.org/10.1371/journal.pone.0149158
Peterson, J., Griffiths, T., Uddenberg, S., Todorov, A., & Suchow, J. W. (2022). Deep models of superficial face judgments. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.4041458

