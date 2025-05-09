from dataclasses import dataclass, feild
from psychopy import visual, core, event, monitors, gui
from psychopy.tools.monitorunittools import pix2deg, deg2pix
from typing import Literal

VIEWING_DISTANCE_IN_CM = 57
MONITOR_WIDTH_IN_CM = 30.41
RESOLUTION = (1440, 900)
UNITS = "deg"
BACKGROUND_COLOR = "White"


@dataclass
class Display:
    viewing_distance: int = 57
    monitor_width: int = 30.41
    resolution: tuple[int, int] = (1440, 900)
    units: Literal["cm", "deg", "pix"] = "deg"
    background_color: tuple[float, float, float] | str = "Grey"


@dataclass
class TrialConfig:
    fix_duration: float = 1
    num_trials: int = 2
    trial_type = [
        (1, -1),
        (-1, 1),
    ]  # first value is target valence, second value is distractor valence
    set_size: int = 12  # number of images in a given display
    img_size: float = 3.2  # in deg units


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
