"""
doorbell-mp3/doorbell.py
Doorbell code by Aaron Dunigan AtLee, Sept. 2019.
Written for Jay Pierson.
Plays an assigned mp3 file when one of two buttons (relays) is triggered.
"""

# Import modules 
from gpiozero import Button
import pygame
from functools import partial
from signal import pause

# Global constants
# GPIO pin numbers for relay inputs
FRONT_DOOR_PIN = 2
REAR_DOOR_PIN = 24
# Paths for corresponding sounds.  
# Unless an absolute path is specified, these should be placed
# in the same folder as this script. 
FRONT_DOOR_SOUND_PATH = "./front1.mp3"
REAR_DOOR_SOUND_PATH = "./rear1.mp3"
# Initialize the pygame mixer.
pygame.mixer.init()
PLAYER = pygame.mixer.music

# Function definitions
def play_music(filename):
    """ Play the given mp3 file specified by filename. """
    # Use a try-except loop to identify errors.
    try:
        # Load and play the song
        PLAYER.load(filename)
        PLAYER.play()
    except FileNotFoundError:
        print("Couldn't find file " + filename)

# Main code
# Print statement will go to log file to delineate each execution of the script.
print()
print("Starting doorbell script.")
# Create Button objects for each door
front_door = Button(FRONT_DOOR_PIN)
rear_door = Button(REAR_DOOR_PIN)
# Assign actions for when each button is pressed (relay is closed):
# The partial() construct is needed to pass the filename parameter.
# See https://docs.python.org/3.5/library/functools.html for details.
front_door.when_pressed = partial(play_music, FRONT_DOOR_SOUND_PATH)
rear_door.when_pressed = partial(play_music, REAR_DOOR_SOUND_PATH)
# Pause to wait for a signal.
# This is needed because if the script exits, the 'when_pressed' callbacks
# are no longer registered.  So now the script waits indefinitely for someone
# to ring the doorbell.
pause()
