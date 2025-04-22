import pandas as pd
import math
from psychopy import visual, core, event, monitors, gui
from psychopy.tools.monitorunittools import pix2deg, deg2pix
from typing import Literal
import ast
import os
import random
import datetime
import sys
import csv


# constants
SEED = 42
VIEWING_DISTANCE_IN_CM = 57
MONITOR_WIDTH_IN_CM = 30.41
RESOLUTION = (1440, 900)
UNITS = "deg"
BACKGROUND_COLOR = "White"

IMAGE_FILE_PATH = "/Users/harini/Library/CloudStorage/OneDrive-UniversityofIllinois-Urbana/Research/Visual search project/stimuli/WM_images"  # CHANGE THIS WHEN UPLOADING TO GIT
STIM_DATA = "stim_data.csv"  # relative path
DATA_PATH = "/Users/harini/Library/CloudStorage/OneDrive-UniversityofIllinois-Urbana/Research/Visual search project/data"
FIXATION_DUR = 1
NUM_TRIALS = 2
TRIAL_TYPE = [
    (1, -1),
    (1, 0),
    (-1, 1),
    (-1, 0),
]  # all possible trial types, first value is target valence, second value is distractor valence

SET_SIZE = 12
IMG_SIZE = 3.2


def setup():
    monitor = create_monitor(
        monitor_name="testMonitor",
        width_in_cm=MONITOR_WIDTH_IN_CM,
        viewing_distance_in_cm=VIEWING_DISTANCE_IN_CM,
        resolution=RESOLUTION,
    )
    window = create_window(monitor=monitor)

    return monitor, window


def create_monitor(
    monitor_name: str,
    width_in_cm: float,
    viewing_distance_in_cm: float,
    resolution: tuple[int, int],
) -> monitors.Monitor:
    monitor = monitors.Monitor(name=monitor_name)
    monitor.setSizePix(resolution)
    monitor.setWidth(width_in_cm)
    monitor.setDistance(viewing_distance_in_cm)
    monitor.saveMon()
    return monitor


def create_window(
    monitor: monitors.Monitor,
    units: Literal["cm", "deg", "pix"] = UNITS,
    screen_num: int = 0,
    full_screen: bool = True,
    background_color: str = BACKGROUND_COLOR,
    size=RESOLUTION,
) -> visual.Window:
    window = visual.Window(
        monitor=monitor,
        size=size,
        color=background_color,
        units=units,
        screen=screen_num,
        fullscr=full_screen,
    )
    return window


# ---------------------------------------------------------------------------------------------


def participant_gui():
    pgui = gui.Dlg()
    pgui.addField("Participant ID")
    pgui.show()

    return pgui.data[0]


def create_participant_file(participant_id, data_path=DATA_PATH):
    date = datetime.datetime.now()
    date = date.strftime("%y%m%d")
    file_path = os.path.join(data_path, f"{date}_{participant_id}.csv")
    filepathexists = os.path.exists(file_path)
    if filepathexists:
        sys.exit("Filename" + file_path + "already_exists")

    return file_path


def load_stimdata(csv):
    stim_data = pd.read_csv(csv, dtype={"image_name": str, "attr_valence": int})
    # TODO: put inside of a preprocess function
    columns_to_transform = [f"d{i}" for i in range(68)]
    for col in columns_to_transform:
        stim_data[col] = stim_data[col].apply(ast.literal_eval)

    return stim_data


def get_img_locations(set_size=SET_SIZE):

    num_locations = set_size
    radius = 7.78  # later in a utils file, make code that calculates radius
    delta = 0.4  # arbitrarily set through trial and error to move the position of the few images in the oblique locations that were slightly overlapping
    theta = 2 * math.pi / num_locations

    image_pos_list = []
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
        image_pos_list.append((dx, dy))

    return image_pos_list


# function to convert marker coordinates to degree coordinates
# move_dist is used to move the marker location by that distance in DEG away from the face so that the target can be presented to the left or the right of the ear.
# it is set to 0 if not specified so that the marker is on the original location.(set to 0.5 otherwise)
def pixel_to_deg_coords(
    x_pix,
    y_pix,
    image_size_pix=1024,
    image_size_deg=10.0,
    # image_pos=(0, 0),
    move_dist=0,
):
    center = image_size_pix / 2
    scale = image_size_deg / image_size_pix  # degrees per pixel
    x_centered = x_pix - center
    y_centered = y_pix - center
    x_deg = x_centered * scale
    y_deg = y_centered * scale
    if x_deg > 0:
        x_deg += move_dist
    else:
        x_deg -= move_dist

    return x_deg, y_deg


def get_trial_imgs(
    df, set_size=SET_SIZE, trial_type=TRIAL_TYPE[0]
):  # TRIAL_TYPE[0] = trustworthy target, untrusworthy distractor

    num_distractors = set_size - 1
    target_valence = trial_type[0]
    distractor_valence = trial_type[1]

    distractor_df = df[df["attr_valence"] == distractor_valence]
    distractor_images = distractor_df.sample(n=num_distractors)
    target_df = df[df["attr_valence"] == target_valence]
    target_image = target_df.sample(n=1)

    image_set = pd.concat([target_image, distractor_images]).reset_index(drop=False)

    image_data = (
        []
    )  # create a list of dictionaries containing the image name and marker positions(in deg)

    for row in image_set.itertuples(index=False):
        x1, y1 = row.d1  # left ear marker
        x2, y2 = row.d15  # right ear marker

        x1_deg, y1_deg = pixel_to_deg_coords(
            x1, y1, image_size_deg=IMG_SIZE, move_dist=0.5
        )
        x2_deg, y2_deg = pixel_to_deg_coords(
            x2, y2, image_size_deg=IMG_SIZE, move_dist=0.5
        )

        if row.attr_valence == target_valence:
            image_type = "target"
        else:
            image_type = "distractor"

        image_data.append(
            {
                "image_name": row.image_name,
                "image_type": image_type,
                "left_marker": (x1_deg, y1_deg),
                "right_marker": (x2_deg, y2_deg),
            }
        )

    # later to retrieve
    # image = image_data[0]  - first entry in image_data
    # x = trial["d1_deg"][0] - getting the x coordinate for the left marker
    # y = trial["d1_deg"][1] - getting the y coordinate for the left marker

    return image_data


def display_instructions(win, instr_file):
    with open(instr_file, "r") as file:
        instr_text = file.read()

    instr = visual.TextStim(win, text=instr_text, color="black", height=0.7, pos=(0, 0))
    instr.draw()
    win.flip()
    event.waitKeys(keyList=["space"])


class Trial:
    def __init__(self, win, image_data, img_pos_list, set_size, img_size=IMG_SIZE):
        self.locations = img_pos_list
        self.rand_index = random.sample(range(0, set_size), set_size)
        self.image_data = image_data
        self.img_size = img_size
        self.win = win
        self.rand_marker_loc = [
            random.randint(0, 1) for _ in range(set_size)
        ]  # randomize target marker location
        self.image_stims, self.targ = self.make_imagestims()
        self.marker_stims, self.mark = self.make_markerstims()
        self.target_pos, self.target_marker_pos = self.get_target_data()

    def make_imagestims(self):
        image_stims = []
        for location, index in enumerate(self.rand_index):
            cur_image = self.image_data[index]
            image_name = cur_image["image_name"]
            image_path = os.path.join(IMAGE_FILE_PATH, image_name)

            cur_pos = self.locations[location]

            stim = visual.ImageStim(
                self.win,
                image=image_path,
                units="deg",
                size=(self.img_size, self.img_size),
                pos=cur_pos,
                autoLog=False,
            )
            image_stims.append(stim)

            if cur_image["image_type"] == "target":
                target_pos = location

        return image_stims, target_pos

    def make_markerstims(self):

        marker_stims = []
        for location, index in enumerate(self.rand_index):
            cur_image = self.image_data[index]
            cur_pos = self.locations[location]
            cur_marker_loc = self.rand_marker_loc[location]

            marker_side = (
                cur_image["left_marker"]
                if cur_marker_loc == 0
                else cur_image["right_marker"]
            )

            x_marker = marker_side[0]
            y_marker = marker_side[1]

            marker = visual.TextStim(
                self.win,
                text="+",
                color="blue",
                height=0.4,
                pos=(x_marker + cur_pos[0], y_marker + cur_pos[1]),
            )
            marker_stims.append(marker)

            if cur_image["image_type"] == "target":
                target_marker_pos = cur_marker_loc

        return marker_stims, target_marker_pos

    def get_target_data(self):
        for location, index in enumerate(self.rand_index):
            cur_image = self.image_data[index]
            if cur_image["image_type"] == "target":
                target_pos = location
                target_marker = self.rand_marker_loc[location]
                target_marker_pos = "left" if target_marker == 0 else "right"
        return target_pos, target_marker_pos


def fix_cross(win, fixation_duration):
    fix_cross = visual.TextStim(
        win,
        text="+",
        color="black",
        height=0.5,
        pos=(0, 0),
    )
    fix_cross.draw()
    win.flip()
    core.wait(fixation_duration)


def do_trial(win, image_stims, marker_stims):
    for stim in image_stims:
        stim.draw()

    for marker in marker_stims:
        marker.draw()

    clock = core.Clock()
    win.flip()
    key_resp = event.waitKeys(keyList=["left", "right"], timeStamped=clock)
    key_resp = key_resp[
        0
    ]  # for some reason key_resp returns [[key, timestamp]] so i'm flattening it to remove the extra brackets
    if key_resp:
        this_resp = 1

    return key_resp, this_resp


def check_corr_resp(key_resp, target_marker_pos):
    if key_resp[0] == target_marker_pos:
        corr_resp = 1
    else:
        corr_resp = 0
    return corr_resp


def save_data(data, participant_id):
    file_path = create_participant_file(participant_id=participant_id)

    headers = ["target_pos", "target_marker_pos", "key_pressed", "rt", "iscorrect"]

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


# --------------------------------------------------------------------------------------------------


def main() -> None:

    participant_id = participant_gui()

    # setup
    monitor, win = setup()
    stim_data = load_stimdata(STIM_DATA)
    img_pos_list = get_img_locations(set_size=SET_SIZE)

    # instructions
    display_instructions(win=win, instr_file="instructions.txt")

    # main task
    trial_data = []
    for trial in range(NUM_TRIALS):
        image_data = get_trial_imgs(
            stim_data, set_size=SET_SIZE, trial_type=TRIAL_TYPE[0]
        )
        trial = Trial(
            win=win,
            image_data=image_data,
            img_pos_list=img_pos_list,
            set_size=SET_SIZE,
            img_size=IMG_SIZE,
        )
        this_resp = None
        while this_resp is None:
            fix_cross(win=win, fixation_duration=FIXATION_DUR)  # in seconds
            key_resp, this_resp = do_trial(win, trial.image_stims, trial.marker_stims)

        corr_resp = check_corr_resp(
            key_resp=key_resp, target_marker_pos=trial.target_marker_pos
        )
        trial_data.append(
            [
                trial.target_pos,
                trial.target_marker_pos,
                key_resp[0],
                key_resp[1],
                corr_resp,
            ]
        )

        event.clearEvents()

    save_data(trial_data, participant_id=participant_id)

    display_instructions(win=win, instr_file="end_instructions.txt")
    # debriefing

    # consent

    # practice
    # instructions again

    # save data


if __name__ == "__main__":
    main()
