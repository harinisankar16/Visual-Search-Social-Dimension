from psychopy import visual, core, event, monitors, gui
from psychopy.tools.monitorunittools import pix2deg, deg2pix
from typing import Literal

VIEWING_DISTANCE_IN_CM = 57
MONITOR_WIDTH_IN_CM = 30.41
RESOLUTION = (1440, 900)
UNITS = "deg"
BACKGROUND_COLOR = "White"


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
