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

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.utils import (
    participant_gui,
    setup,
    load_stimdata,
    get_trial_imgs,
    display_instructions,
    do_trial,
    Trial,
    save_data,
    fix_cross,
    make_block,
    show_break_instr,
    show_block_instr,
)
from src.config import TrialConfig

NUM_TRIALS_PER_BLOCK = 4
IMAGE_FILE_PATH = "stimuli/WM_images"
STIM_DATA = "stim_data.csv"  # relative path
DATA_PATH = "data"


# ----------------------------------------------------------------------------


def main() -> None:

    # open gui to get participant id
    participant_id = participant_gui()

    # setup
    monitor, win = setup()

    # load stim_data
    stim_data = load_stimdata(STIM_DATA)

    # create all block and set_size conditions
    all_trials = make_block(num_trials_per_block=NUM_TRIALS_PER_BLOCK)
    first_block = all_trials[0][0]

    # display instructions
    display_instructions(win=win, instr_file="instructions.txt")
    show_block_instr(win=win, block_type=first_block)

    # start overall clock
    trial_clock = core.Clock()

    # create trials and do main task
    trial_data = []

    previous_block_type = None

    for block_type, set_size, trial_index in all_trials:
        if block_type != previous_block_type:
            if previous_block_type is not None:
                show_break_instr(win=win, instr_file="break_instructions.txt")
                show_block_instr(win=win, block_type=block_type)
            previous_block_type = block_type

        image_data = get_trial_imgs(
            stim_data, set_size=set_size, trial_type=TrialConfig.trial_type[block_type]
        )
        trial = Trial(
            win=win,
            image_data=image_data,
            set_size=set_size,
        )
        this_resp = None
        while this_resp is None:
            fix_cross(win=win)  # in seconds
            key_resp, this_resp, corr_resp = do_trial(
                win, trial.image_stims, trial.marker_stims, trial.target_marker_pos
            )

        trial_timestamp = trial_clock.getTime()

        trial_data.append(
            [
                participant_id,
                trial_index,
                block_type,
                set_size,
                trial_timestamp,
                image_data,
                trial.target_pos,
                trial.target_marker_pos,
                key_resp[0],
                key_resp[1],
                corr_resp,
            ]
        )

        event.clearEvents()

    # save_data
    save_data(trial_data, participant_id=participant_id)

    display_instructions(win=win, instr_file="end_instructions.txt")


if __name__ == "__main__":
    main()
