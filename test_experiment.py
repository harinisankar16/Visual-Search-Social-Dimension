# test run of experiment
# tests set size of 12
# displays 11 distractor and 1 target in random locations in the ring
# press any key to exit display

from psychopy import visual, core, event
from psychopy import monitors
from psychopy.tools.monitorunittools import pix2deg
import pandas as pd
import random
from pathlib import Path
import os
from typing import Literal
import math

# READ IN STIMULI DATABASE
file_name = "test_data.csv"  # relative path

# read in the data from the csv to a dataframe
stim_data = pd.read_csv(file_name, dtype={"image_name": str, "attr_valence": int})

# image location
image_file_location = "stimuli/test_images"  # CHANGED FOR UPLOADING TO GIT

# SETTING UP MONITOR
width_cm: float = 30.41
viewing_distance_cm: float = 57
resolution_px: tuple[int, int] = (1440, 900)  # my mac1
screen: int = 0
units: Literal["deg", "rad"] = "deg"
bg_color: str = "white"
full_screen: bool = True
center_deg: tuple[float, float] = (0, 0)

monitor = monitors.Monitor("testMonitor")
monitor.setSizePix(resolution_px)
monitor.setWidth(width_cm)
monitor.setDistance(viewing_distance_cm)
monitor.saveMon()

width_deg = pix2deg(resolution_px[0], monitor)
height_deg = pix2deg(resolution_px[1], monitor)

# finding the location coordinates for a display size of 12

radius = 7.78  # later in a utils file, make code that calculates radius
img_width = 3.2  # subsequently calculates the image with based on radius
num_locations = 12
delta = 0.4  # arbitrarily set through trial and error to move the position of the few images in the oblique locations that were slightly overlapping
theta = 2 * math.pi / num_locations

image_pos = []
for location in range(num_locations):
    cur_theta = theta * location
    dx = round(radius * math.cos(cur_theta), 2)
    dy = round(radius * math.sin(cur_theta), 2)
    if location in [2, 10]:
        dx = dx - delta
    if location in [4, 8]:
        dx = dx + delta
    if location in [1, 5]:
        dy = dy - delta
    elif location in [7, 11]:
        dy = dy + delta
    image_pos.append((dx, dy))


# randomly selecting images to display
set_size = 12
num_distractors = set_size - 1
target_valence = 1
distractor_valence = -target_valence


def distractor_images(num_distractors, distractor_valence, df=stim_data):
    filtered_df = df[df["attr_valence"] == distractor_valence]
    distractor_images = filtered_df.sample(
        n=num_distractors, random_state=42
    )  # random_state is optional for reproducibility
    return distractor_images


def target_image(targ_valence, num_target=1, df=stim_data):
    filtered_df = df[df["attr_valence"] == targ_valence]
    target_image = filtered_df.sample(n=num_target, random_state=42)
    return target_image


distractors = distractor_images(
    num_distractors=num_distractors, distractor_valence=distractor_valence
)  # get list of distractors
target = target_image(targ_valence=target_valence)  # get list of targets


# randomize location of distractors and target
image_set = pd.concat([target, distractors]).reset_index(drop=False)
rand_index = random.sample(range(0, 12), 12)

# initialise window
win = visual.Window(
    monitor=monitor,
    size=resolution_px,
    color=bg_color,
    units=units,
    screen=screen,
    fullscr=full_screen,
)

# draw fixation cross
fix_cross = visual.TextStim(
    win,
    text="+",  # The symbol for the fixation cross
    color="white",  # Color of the cross
    height=0.5,  # Adjust size as needed
    pos=(0, 0),  # Position at the center of the screen
)

fix_cross.draw()

# draw images
for location, index in enumerate(rand_index):

    cur_image_row = image_set.iloc[index]
    image_name = cur_image_row["image_name"]
    image_path = os.path.join(image_file_location, image_name)

    image = visual.ImageStim(
        win,
        image_path,
        autoLog=False,
        units="deg",
        size=(img_width, img_width),
        pos=image_pos[location],
    )
    image.draw()


win.flip()
event.waitKeys()  # press any key to exit
