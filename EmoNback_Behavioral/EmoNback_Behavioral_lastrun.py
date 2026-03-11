#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Wed Mar 11 14:31:51 2026
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from setupLogic
# Import modules at the very top
import os
import re
import csv
import pandas as pd
from psychopy import data

# Get root folder
expRoot = os.getcwd()

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'EmoNback_Behavioral'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'Please enter the Subject ID:': '',
    'Please enter the Session Number:': [1, 2],
    'Enter subject\'s handedness:': ['Right', 'Left'],
    'Please select version:': [1,2,3,4],
    'Initial run:': [1, 2],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1728, 1117]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/sub-%s_ses-%s_emoback' % (expInfo['Please enter the Subject ID:'], expInfo['Please enter the Session Number:'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/akashrathi/Documents/EDC_Tasks/EmoNback/EmoNback_Behavioral/EmoNback_Behavioral_lastrun.py',
        savePickle=False, saveWideText=False,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='cti_monitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        expInfo['frameRate'] = 60
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('Continue') is None:
        # initialise Continue
        Continue = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue',
        )
    if deviceManager.getDevice('Continue_2') is None:
        # initialise Continue_2
        Continue_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue_2',
        )
    if deviceManager.getDevice('Continue_3') is None:
        # initialise Continue_3
        Continue_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue_3',
        )
    if deviceManager.getDevice('Continue_4') is None:
        # initialise Continue_4
        Continue_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue_4',
        )
    if deviceManager.getDevice('Continue_5') is None:
        # initialise Continue_5
        Continue_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue_5',
        )
    if deviceManager.getDevice('Continue_6') is None:
        # initialise Continue_6
        Continue_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue_6',
        )
    if deviceManager.getDevice('Continue_7') is None:
        # initialise Continue_7
        Continue_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue_7',
        )
    if deviceManager.getDevice('response') is None:
        # initialise response
        response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response',
        )
    if deviceManager.getDevice('Continue_8') is None:
        # initialise Continue_8
        Continue_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue_8',
        )
    if deviceManager.getDevice('Continue_9') is None:
        # initialise Continue_9
        Continue_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Continue_9',
        )
    if deviceManager.getDevice('Finish') is None:
        # initialise Finish
        Finish = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Finish',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "SetupExperiment" ---
    # Run 'Begin Experiment' code from setupLogic
    # Version selected
    selectedVersion = int(expInfo['Please select version:'])
    versionFolder = f"NBackProcLists/v{selectedVersion}"
    versionPath = os.path.join(expRoot, versionFolder)
    
    # Set initial run to variable
    initialRun = expInfo["Initial run:"]
    
    # Paths to runs
    run1Folder = os.path.join(versionPath, 'run1')
    run2Folder = os.path.join(versionPath, 'run2')
    
    # Numeric sort function for blocks
    def numeric_sort(value):
        match = re.search(r'block(\d+)', value, re.IGNORECASE)
        return int(match.group(1)) if match else 0
    
    # Sorted list of block CSV files
    blockFilesRun1 = sorted(
        [f for f in os.listdir(run1Folder) if f.endswith('.csv')],
        key=numeric_sort
    )
    blockFilesRun2 = sorted(
        [f for f in os.listdir(run2Folder) if f.endswith('.csv')],
        key=numeric_sort
    )
    
    # Initial block index
    blockIndex1 = 0
    blockIndex2 = 0
    
    # Get number of blocks per run
    num_blocks_run1 = len(blockFilesRun1)
    num_blocks_run2 = len(blockFilesRun2)
    
    # Load current block CSV dynamically
    blockFile1 = os.path.join(run1Folder, blockFilesRun1[blockIndex1])
    blockFile2 = os.path.join(run2Folder, blockFilesRun2[blockIndex2])
    
    # Handedness logic
    if expInfo["Enter subject's handedness:"].lower() == 'right':
        matchKey = '1'
        noMatchKey = '2'
        leftSideOfScreen = "MATCH\nPOINTER"
        rightSideOfScreen = "NO MATCH\nMIDDLE"
    else:
        matchKey = '2'
        noMatchKey = '1'
        leftSideOfScreen = "NO MATCH\nMIDDLE"
        rightSideOfScreen = "MATCH\nPOINTER"
    
    # Make sure data directory exists
    dataDir = 'data'
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    
    # Filename (NO extension yet)
    filename = u'data/sub-%s_ses-%s_emoback' % (
        expInfo['Please enter the Subject ID:'],
        expInfo['Please enter the Session Number:']
    )
    
    # Add extension
    filename = filename + '.csv'
    
    # -------------------------------
    # CSV headers
    # -------------------------------
    
    headers = [
        'Version',
        'Run',
        'BlockNumber',
        'TrialNumber',
        'BlockType',
        'Condition_Label',
        'Stimulus',
        'TargetStimulus',
        'TargetFlag',
        'Response',
        'RT',
        'Accuracy',
        'Handedness',
        'Date',
        'Time',
        'TimeSinceStart'
    ]
    
    # -------------------------------
    # Create file if needed
    # -------------------------------
    
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
    
    
    # --- Initialize components for Routine "TitlePage" ---
    Continue = keyboard.Keyboard(deviceName='Continue')
    NbackTitle = visual.TextBox2(
         win, text='N-back', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='NbackTitle',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions" ---
    Continue_2 = keyboard.Keyboard(deviceName='Continue_2')
    Instruction = visual.TextBox2(
         win, text='There are two games in this part of the study. \n\nThey are "0-Back" and "2-Back"\n\nYou will see the words "Target" or "2-back" before each game starts.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Instruction',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions_2" ---
    Continue_3 = keyboard.Keyboard(deviceName='Continue_3')
    Instruction_2 = visual.TextBox2(
         win, text='For "0-Back", press MATCH if you see a picture that is the same as the target picture. \nPress NO MATCH if it is not the same.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.25), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Instruction_2',
         depth=-1, autoLog=True,
    )
    Target = visual.TextBox2(
         win, text='Target          =', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.15, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Target',
         depth=-2, autoLog=True,
    )
    TargetImage = visual.ImageStim(
        win=win,
        name='TargetImage', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0.15, 0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "Instructions_3" ---
    Continue_4 = keyboard.Keyboard(deviceName='Continue_4')
    Instruction_3 = visual.TextBox2(
         win, text='For "2-back", press MATCH if the picture you see is the same as two pictures back. \nPress NO MATCH if not. ', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.25), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Instruction_3',
         depth=-1, autoLog=True,
    )
    Green_Border = visual.Rect(
        win=win, name='Green_Border',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=(-0.50, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='limegreen', fillColor='limegreen',
        opacity=1.0, depth=-2.0, interpolate=True)
    Image_2Back = visual.ImageStim(
        win=win,
        name='Image_2Back', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.50, 0), draggable=False, size=(0.13, 0.13),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    Image_1Back = visual.ImageStim(
        win=win,
        name='Image_1Back', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.30, 0), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Image_ToMatch = visual.ImageStim(
        win=win,
        name='Image_ToMatch', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    LEFTSIDESCREEN_CAPTION = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.20, -0.25), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='limegreen', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='LEFTSIDESCREEN_CAPTION',
         depth=-6, autoLog=True,
    )
    RIGHTSIDESCREEN_CAPTION = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.20, -0.25), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='RIGHTSIDESCREEN_CAPTION',
         depth=-7, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions_4" ---
    Continue_5 = keyboard.Keyboard(deviceName='Continue_5')
    Instruction_4 = visual.TextBox2(
         win, text='Please respond while the picture is on the screen.\n\nPress your POINTER finger for MATCH.\nPress your MIDDLE finger for NO MATCH.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Instruction_4',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions_5" ---
    Continue_6 = keyboard.Keyboard(deviceName='Continue_6')
    Instruction_5 = visual.TextBox2(
         win, text='Pay close attention when the plus sign turns purple\nto see what game you are playing!', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Instruction_5',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Waiting4Scanner" ---
    Continue_7 = keyboard.Keyboard(deviceName='Continue_7')
    Scanner_Instruction = visual.TextBox2(
         win, text='The task will begin momentarily. Waiting for scanner. Get ready…', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Scanner_Instruction',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "CueFix_Run1" ---
    Cue_Fix = visual.TextBox2(
         win, text='+', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.1,
         size=(1, 1), borderWidth=0.0,
         color=(1.0000, -1.0000, 1.0000), colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Cue_Fix',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "Cue2Back" ---
    Cue_2Back = visual.TextBox2(
         win, text='2-Back', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Cue_2Back',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "Cue0Back" ---
    Cue_Target = visual.TextBox2(
         win, text='Target          =', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.15, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Cue_Target',
         depth=-1, autoLog=True,
    )
    Cue_TargetImage = visual.ImageStim(
        win=win,
        name='Cue_TargetImage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, 0), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Zero_back = visual.TextBox2(
         win, text='0-back', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.25, 0.25), draggable=False,      letterHeight=0.03,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Zero_back',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Stim" ---
    StimulusImage = visual.ImageStim(
        win=win,
        name='StimulusImage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    LeftScreenResponse = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.20, -0.25), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='LeftScreenResponse',
         depth=-2, autoLog=True,
    )
    RightScreenResponse = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.20, -0.25), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='RightScreenResponse',
         depth=-3, autoLog=True,
    )
    response = keyboard.Keyboard(deviceName='response')
    
    # --- Initialize components for Routine "Fix" ---
    End_Fix = visual.TextBox2(
         win, text='+', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.1,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='End_Fix',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "EndBlock_Run1" ---
    
    # --- Initialize components for Routine "Fix15Sec" ---
    Fix_15_Sec = visual.TextBox2(
         win, text='+', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.1,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Fix_15_Sec',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "Fix5Sec" ---
    Fix_5_Sec = visual.TextBox2(
         win, text='+', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.1,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Fix_5_Sec',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions_6" ---
    Continue_8 = keyboard.Keyboard(deviceName='Continue_8')
    Instruction_6 = visual.TextBox2(
         win, text='Great Job!\nAgain, the games will switch. \n\nPay close attention when the plus sign turns purple \nto see what game you are playing!', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Instruction_6',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions_7" ---
    Continue_9 = keyboard.Keyboard(deviceName='Continue_9')
    Instruction_7 = visual.TextBox2(
         win, text='Please respond while the picture is on the screen. \n\nPress your POINTER finger for MATCH.\nPress your MIDDLE finger for NO MATCH.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Instruction_7',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Waiting4Scanner" ---
    Continue_7 = keyboard.Keyboard(deviceName='Continue_7')
    Scanner_Instruction = visual.TextBox2(
         win, text='The task will begin momentarily. Waiting for scanner. Get ready…', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Scanner_Instruction',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "CueFix_Run2" ---
    Cue_Fix_2 = visual.TextBox2(
         win, text='+', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.1,
         size=(1, 1), borderWidth=0.0,
         color=(1.0000, -1.0000, 1.0000), colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Cue_Fix_2',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "Cue2Back" ---
    Cue_2Back = visual.TextBox2(
         win, text='2-Back', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Cue_2Back',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "Cue0Back" ---
    Cue_Target = visual.TextBox2(
         win, text='Target          =', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.15, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Cue_Target',
         depth=-1, autoLog=True,
    )
    Cue_TargetImage = visual.ImageStim(
        win=win,
        name='Cue_TargetImage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, 0), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Zero_back = visual.TextBox2(
         win, text='0-back', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.25, 0.25), draggable=False,      letterHeight=0.03,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Zero_back',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Stim" ---
    StimulusImage = visual.ImageStim(
        win=win,
        name='StimulusImage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    LeftScreenResponse = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.20, -0.25), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='LeftScreenResponse',
         depth=-2, autoLog=True,
    )
    RightScreenResponse = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.20, -0.25), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='RightScreenResponse',
         depth=-3, autoLog=True,
    )
    response = keyboard.Keyboard(deviceName='response')
    
    # --- Initialize components for Routine "Fix" ---
    End_Fix = visual.TextBox2(
         win, text='+', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.1,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='End_Fix',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "EndBlock_Run2" ---
    
    # --- Initialize components for Routine "Goodbye" ---
    Finish = keyboard.Keyboard(deviceName='Finish')
    All_Done = visual.TextBox2(
         win, text='All done!', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.03,
         size=(1, 1), borderWidth=0.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='All_Done',
         depth=-1, autoLog=True,
    )
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "SetupExperiment" ---
    # create an object to store info about Routine SetupExperiment
    SetupExperiment = data.Routine(
        name='SetupExperiment',
        components=[],
    )
    SetupExperiment.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for SetupExperiment
    SetupExperiment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    SetupExperiment.tStart = globalClock.getTime(format='float')
    SetupExperiment.status = STARTED
    thisExp.addData('SetupExperiment.started', SetupExperiment.tStart)
    SetupExperiment.maxDuration = None
    # keep track of which components have finished
    SetupExperimentComponents = SetupExperiment.components
    for thisComponent in SetupExperiment.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SetupExperiment" ---
    SetupExperiment.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            SetupExperiment.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SetupExperiment.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SetupExperiment" ---
    for thisComponent in SetupExperiment.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for SetupExperiment
    SetupExperiment.tStop = globalClock.getTime(format='float')
    SetupExperiment.tStopRefresh = tThisFlipGlobal
    thisExp.addData('SetupExperiment.stopped', SetupExperiment.tStop)
    thisExp.nextEntry()
    # the Routine "SetupExperiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "TitlePage" ---
    # create an object to store info about Routine TitlePage
    TitlePage = data.Routine(
        name='TitlePage',
        components=[Continue, NbackTitle],
    )
    TitlePage.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue
    Continue.keys = []
    Continue.rt = []
    _Continue_allKeys = []
    NbackTitle.reset()
    # Run 'Begin Routine' code from skip_run_1_logic_13
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for TitlePage
    TitlePage.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    TitlePage.tStart = globalClock.getTime(format='float')
    TitlePage.status = STARTED
    thisExp.addData('TitlePage.started', TitlePage.tStart)
    TitlePage.maxDuration = None
    # keep track of which components have finished
    TitlePageComponents = TitlePage.components
    for thisComponent in TitlePage.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TitlePage" ---
    TitlePage.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue* updates
        waitOnFlip = False
        
        # if Continue is starting this frame...
        if Continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue.frameNStart = frameN  # exact frame index
            Continue.tStart = t  # local t and not account for scr refresh
            Continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue.started')
            # update status
            Continue.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue.status == STARTED and not waitOnFlip:
            theseKeys = Continue.getKeys(keyList=['2','3','space'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_allKeys.extend(theseKeys)
            if len(_Continue_allKeys):
                Continue.keys = _Continue_allKeys[-1].name  # just the last key pressed
                Continue.rt = _Continue_allKeys[-1].rt
                Continue.duration = _Continue_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *NbackTitle* updates
        
        # if NbackTitle is starting this frame...
        if NbackTitle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NbackTitle.frameNStart = frameN  # exact frame index
            NbackTitle.tStart = t  # local t and not account for scr refresh
            NbackTitle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NbackTitle, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NbackTitle.started')
            # update status
            NbackTitle.status = STARTED
            NbackTitle.setAutoDraw(True)
        
        # if NbackTitle is active this frame...
        if NbackTitle.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            TitlePage.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TitlePage.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TitlePage" ---
    for thisComponent in TitlePage.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for TitlePage
    TitlePage.tStop = globalClock.getTime(format='float')
    TitlePage.tStopRefresh = tThisFlipGlobal
    thisExp.addData('TitlePage.stopped', TitlePage.tStop)
    # check responses
    if Continue.keys in ['', [], None]:  # No response was made
        Continue.keys = None
    thisExp.addData('Continue.keys',Continue.keys)
    if Continue.keys != None:  # we had a response
        thisExp.addData('Continue.rt', Continue.rt)
        thisExp.addData('Continue.duration', Continue.duration)
    thisExp.nextEntry()
    # the Routine "TitlePage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions" ---
    # create an object to store info about Routine Instructions
    Instructions = data.Routine(
        name='Instructions',
        components=[Continue_2, Instruction],
    )
    Instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_2
    Continue_2.keys = []
    Continue_2.rt = []
    _Continue_2_allKeys = []
    Instruction.reset()
    # Run 'Begin Routine' code from skip_run_1_logic
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Instructions
    Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions.tStart = globalClock.getTime(format='float')
    Instructions.status = STARTED
    thisExp.addData('Instructions.started', Instructions.tStart)
    Instructions.maxDuration = None
    # keep track of which components have finished
    InstructionsComponents = Instructions.components
    for thisComponent in Instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    Instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_2* updates
        waitOnFlip = False
        
        # if Continue_2 is starting this frame...
        if Continue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_2.frameNStart = frameN  # exact frame index
            Continue_2.tStart = t  # local t and not account for scr refresh
            Continue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_2.started')
            # update status
            Continue_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_2.status == STARTED and not waitOnFlip:
            theseKeys = Continue_2.getKeys(keyList=['2','3','space'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_2_allKeys.extend(theseKeys)
            if len(_Continue_2_allKeys):
                Continue_2.keys = _Continue_2_allKeys[-1].name  # just the last key pressed
                Continue_2.rt = _Continue_2_allKeys[-1].rt
                Continue_2.duration = _Continue_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instruction* updates
        
        # if Instruction is starting this frame...
        if Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction.frameNStart = frameN  # exact frame index
            Instruction.tStart = t  # local t and not account for scr refresh
            Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction.started')
            # update status
            Instruction.status = STARTED
            Instruction.setAutoDraw(True)
        
        # if Instruction is active this frame...
        if Instruction.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in Instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions
    Instructions.tStop = globalClock.getTime(format='float')
    Instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions.stopped', Instructions.tStop)
    # check responses
    if Continue_2.keys in ['', [], None]:  # No response was made
        Continue_2.keys = None
    thisExp.addData('Continue_2.keys',Continue_2.keys)
    if Continue_2.keys != None:  # we had a response
        thisExp.addData('Continue_2.rt', Continue_2.rt)
        thisExp.addData('Continue_2.duration', Continue_2.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_2" ---
    # create an object to store info about Routine Instructions_2
    Instructions_2 = data.Routine(
        name='Instructions_2',
        components=[Continue_3, Instruction_2, Target, TargetImage],
    )
    Instructions_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_3
    Continue_3.keys = []
    Continue_3.rt = []
    _Continue_3_allKeys = []
    Instruction_2.reset()
    Target.reset()
    # Run 'Begin Routine' code from skip_run_1_logic_2
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Instructions_2
    Instructions_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_2.tStart = globalClock.getTime(format='float')
    Instructions_2.status = STARTED
    thisExp.addData('Instructions_2.started', Instructions_2.tStart)
    Instructions_2.maxDuration = None
    # keep track of which components have finished
    Instructions_2Components = Instructions_2.components
    for thisComponent in Instructions_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_2" ---
    Instructions_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_3* updates
        waitOnFlip = False
        
        # if Continue_3 is starting this frame...
        if Continue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_3.frameNStart = frameN  # exact frame index
            Continue_3.tStart = t  # local t and not account for scr refresh
            Continue_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_3.started')
            # update status
            Continue_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_3.status == STARTED and not waitOnFlip:
            theseKeys = Continue_3.getKeys(keyList=['2','3','space'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_3_allKeys.extend(theseKeys)
            if len(_Continue_3_allKeys):
                Continue_3.keys = _Continue_3_allKeys[-1].name  # just the last key pressed
                Continue_3.rt = _Continue_3_allKeys[-1].rt
                Continue_3.duration = _Continue_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instruction_2* updates
        
        # if Instruction_2 is starting this frame...
        if Instruction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_2.frameNStart = frameN  # exact frame index
            Instruction_2.tStart = t  # local t and not account for scr refresh
            Instruction_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_2.started')
            # update status
            Instruction_2.status = STARTED
            Instruction_2.setAutoDraw(True)
        
        # if Instruction_2 is active this frame...
        if Instruction_2.status == STARTED:
            # update params
            pass
        
        # *Target* updates
        
        # if Target is starting this frame...
        if Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Target.frameNStart = frameN  # exact frame index
            Target.tStart = t  # local t and not account for scr refresh
            Target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Target.started')
            # update status
            Target.status = STARTED
            Target.setAutoDraw(True)
        
        # if Target is active this frame...
        if Target.status == STARTED:
            # update params
            pass
        
        # *TargetImage* updates
        
        # if TargetImage is starting this frame...
        if TargetImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TargetImage.frameNStart = frameN  # exact frame index
            TargetImage.tStart = t  # local t and not account for scr refresh
            TargetImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargetImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TargetImage.started')
            # update status
            TargetImage.status = STARTED
            TargetImage.setAutoDraw(True)
        
        # if TargetImage is active this frame...
        if TargetImage.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_2" ---
    for thisComponent in Instructions_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_2
    Instructions_2.tStop = globalClock.getTime(format='float')
    Instructions_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_2.stopped', Instructions_2.tStop)
    # check responses
    if Continue_3.keys in ['', [], None]:  # No response was made
        Continue_3.keys = None
    thisExp.addData('Continue_3.keys',Continue_3.keys)
    if Continue_3.keys != None:  # we had a response
        thisExp.addData('Continue_3.rt', Continue_3.rt)
        thisExp.addData('Continue_3.duration', Continue_3.duration)
    thisExp.nextEntry()
    # the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_3" ---
    # create an object to store info about Routine Instructions_3
    Instructions_3 = data.Routine(
        name='Instructions_3',
        components=[Continue_4, Instruction_3, Green_Border, Image_2Back, Image_1Back, Image_ToMatch, LEFTSIDESCREEN_CAPTION, RIGHTSIDESCREEN_CAPTION],
    )
    Instructions_3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_4
    Continue_4.keys = []
    Continue_4.rt = []
    _Continue_4_allKeys = []
    Instruction_3.reset()
    LEFTSIDESCREEN_CAPTION.reset()
    LEFTSIDESCREEN_CAPTION.setText(leftSideOfScreen)
    RIGHTSIDESCREEN_CAPTION.reset()
    RIGHTSIDESCREEN_CAPTION.setText(rightSideOfScreen)
    # Run 'Begin Routine' code from skip_run_1_logic_3
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Instructions_3
    Instructions_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_3.tStart = globalClock.getTime(format='float')
    Instructions_3.status = STARTED
    thisExp.addData('Instructions_3.started', Instructions_3.tStart)
    Instructions_3.maxDuration = None
    # keep track of which components have finished
    Instructions_3Components = Instructions_3.components
    for thisComponent in Instructions_3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_3" ---
    Instructions_3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_4* updates
        waitOnFlip = False
        
        # if Continue_4 is starting this frame...
        if Continue_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_4.frameNStart = frameN  # exact frame index
            Continue_4.tStart = t  # local t and not account for scr refresh
            Continue_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_4.started')
            # update status
            Continue_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_4.status == STARTED and not waitOnFlip:
            theseKeys = Continue_4.getKeys(keyList=['2','3','space'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_4_allKeys.extend(theseKeys)
            if len(_Continue_4_allKeys):
                Continue_4.keys = _Continue_4_allKeys[-1].name  # just the last key pressed
                Continue_4.rt = _Continue_4_allKeys[-1].rt
                Continue_4.duration = _Continue_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instruction_3* updates
        
        # if Instruction_3 is starting this frame...
        if Instruction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_3.frameNStart = frameN  # exact frame index
            Instruction_3.tStart = t  # local t and not account for scr refresh
            Instruction_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_3.started')
            # update status
            Instruction_3.status = STARTED
            Instruction_3.setAutoDraw(True)
        
        # if Instruction_3 is active this frame...
        if Instruction_3.status == STARTED:
            # update params
            pass
        
        # *Green_Border* updates
        
        # if Green_Border is starting this frame...
        if Green_Border.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Green_Border.frameNStart = frameN  # exact frame index
            Green_Border.tStart = t  # local t and not account for scr refresh
            Green_Border.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Green_Border, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Green_Border.started')
            # update status
            Green_Border.status = STARTED
            Green_Border.setAutoDraw(True)
        
        # if Green_Border is active this frame...
        if Green_Border.status == STARTED:
            # update params
            pass
        
        # *Image_2Back* updates
        
        # if Image_2Back is starting this frame...
        if Image_2Back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Image_2Back.frameNStart = frameN  # exact frame index
            Image_2Back.tStart = t  # local t and not account for scr refresh
            Image_2Back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Image_2Back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Image_2Back.started')
            # update status
            Image_2Back.status = STARTED
            Image_2Back.setAutoDraw(True)
        
        # if Image_2Back is active this frame...
        if Image_2Back.status == STARTED:
            # update params
            pass
        
        # *Image_1Back* updates
        
        # if Image_1Back is starting this frame...
        if Image_1Back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Image_1Back.frameNStart = frameN  # exact frame index
            Image_1Back.tStart = t  # local t and not account for scr refresh
            Image_1Back.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Image_1Back, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Image_1Back.started')
            # update status
            Image_1Back.status = STARTED
            Image_1Back.setAutoDraw(True)
        
        # if Image_1Back is active this frame...
        if Image_1Back.status == STARTED:
            # update params
            pass
        
        # *Image_ToMatch* updates
        
        # if Image_ToMatch is starting this frame...
        if Image_ToMatch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Image_ToMatch.frameNStart = frameN  # exact frame index
            Image_ToMatch.tStart = t  # local t and not account for scr refresh
            Image_ToMatch.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Image_ToMatch, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Image_ToMatch.started')
            # update status
            Image_ToMatch.status = STARTED
            Image_ToMatch.setAutoDraw(True)
        
        # if Image_ToMatch is active this frame...
        if Image_ToMatch.status == STARTED:
            # update params
            pass
        
        # *LEFTSIDESCREEN_CAPTION* updates
        
        # if LEFTSIDESCREEN_CAPTION is starting this frame...
        if LEFTSIDESCREEN_CAPTION.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LEFTSIDESCREEN_CAPTION.frameNStart = frameN  # exact frame index
            LEFTSIDESCREEN_CAPTION.tStart = t  # local t and not account for scr refresh
            LEFTSIDESCREEN_CAPTION.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LEFTSIDESCREEN_CAPTION, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'LEFTSIDESCREEN_CAPTION.started')
            # update status
            LEFTSIDESCREEN_CAPTION.status = STARTED
            LEFTSIDESCREEN_CAPTION.setAutoDraw(True)
        
        # if LEFTSIDESCREEN_CAPTION is active this frame...
        if LEFTSIDESCREEN_CAPTION.status == STARTED:
            # update params
            pass
        
        # *RIGHTSIDESCREEN_CAPTION* updates
        
        # if RIGHTSIDESCREEN_CAPTION is starting this frame...
        if RIGHTSIDESCREEN_CAPTION.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RIGHTSIDESCREEN_CAPTION.frameNStart = frameN  # exact frame index
            RIGHTSIDESCREEN_CAPTION.tStart = t  # local t and not account for scr refresh
            RIGHTSIDESCREEN_CAPTION.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RIGHTSIDESCREEN_CAPTION, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RIGHTSIDESCREEN_CAPTION.started')
            # update status
            RIGHTSIDESCREEN_CAPTION.status = STARTED
            RIGHTSIDESCREEN_CAPTION.setAutoDraw(True)
        
        # if RIGHTSIDESCREEN_CAPTION is active this frame...
        if RIGHTSIDESCREEN_CAPTION.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_3" ---
    for thisComponent in Instructions_3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_3
    Instructions_3.tStop = globalClock.getTime(format='float')
    Instructions_3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_3.stopped', Instructions_3.tStop)
    # check responses
    if Continue_4.keys in ['', [], None]:  # No response was made
        Continue_4.keys = None
    thisExp.addData('Continue_4.keys',Continue_4.keys)
    if Continue_4.keys != None:  # we had a response
        thisExp.addData('Continue_4.rt', Continue_4.rt)
        thisExp.addData('Continue_4.duration', Continue_4.duration)
    thisExp.nextEntry()
    # the Routine "Instructions_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_4" ---
    # create an object to store info about Routine Instructions_4
    Instructions_4 = data.Routine(
        name='Instructions_4',
        components=[Continue_5, Instruction_4],
    )
    Instructions_4.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_5
    Continue_5.keys = []
    Continue_5.rt = []
    _Continue_5_allKeys = []
    Instruction_4.reset()
    # Run 'Begin Routine' code from skip_run_1_logic_4
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Instructions_4
    Instructions_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_4.tStart = globalClock.getTime(format='float')
    Instructions_4.status = STARTED
    thisExp.addData('Instructions_4.started', Instructions_4.tStart)
    Instructions_4.maxDuration = None
    # keep track of which components have finished
    Instructions_4Components = Instructions_4.components
    for thisComponent in Instructions_4.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_4" ---
    Instructions_4.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_5* updates
        waitOnFlip = False
        
        # if Continue_5 is starting this frame...
        if Continue_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_5.frameNStart = frameN  # exact frame index
            Continue_5.tStart = t  # local t and not account for scr refresh
            Continue_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_5.started')
            # update status
            Continue_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_5.status == STARTED and not waitOnFlip:
            theseKeys = Continue_5.getKeys(keyList=['2','3','space'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_5_allKeys.extend(theseKeys)
            if len(_Continue_5_allKeys):
                Continue_5.keys = _Continue_5_allKeys[-1].name  # just the last key pressed
                Continue_5.rt = _Continue_5_allKeys[-1].rt
                Continue_5.duration = _Continue_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instruction_4* updates
        
        # if Instruction_4 is starting this frame...
        if Instruction_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_4.frameNStart = frameN  # exact frame index
            Instruction_4.tStart = t  # local t and not account for scr refresh
            Instruction_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_4.started')
            # update status
            Instruction_4.status = STARTED
            Instruction_4.setAutoDraw(True)
        
        # if Instruction_4 is active this frame...
        if Instruction_4.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_4.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_4.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_4" ---
    for thisComponent in Instructions_4.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_4
    Instructions_4.tStop = globalClock.getTime(format='float')
    Instructions_4.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_4.stopped', Instructions_4.tStop)
    # check responses
    if Continue_5.keys in ['', [], None]:  # No response was made
        Continue_5.keys = None
    thisExp.addData('Continue_5.keys',Continue_5.keys)
    if Continue_5.keys != None:  # we had a response
        thisExp.addData('Continue_5.rt', Continue_5.rt)
        thisExp.addData('Continue_5.duration', Continue_5.duration)
    thisExp.nextEntry()
    # the Routine "Instructions_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_5" ---
    # create an object to store info about Routine Instructions_5
    Instructions_5 = data.Routine(
        name='Instructions_5',
        components=[Continue_6, Instruction_5],
    )
    Instructions_5.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_6
    Continue_6.keys = []
    Continue_6.rt = []
    _Continue_6_allKeys = []
    Instruction_5.reset()
    # Run 'Begin Routine' code from skip_run_1_logic_5
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Instructions_5
    Instructions_5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_5.tStart = globalClock.getTime(format='float')
    Instructions_5.status = STARTED
    thisExp.addData('Instructions_5.started', Instructions_5.tStart)
    Instructions_5.maxDuration = None
    # keep track of which components have finished
    Instructions_5Components = Instructions_5.components
    for thisComponent in Instructions_5.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_5" ---
    Instructions_5.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_6* updates
        waitOnFlip = False
        
        # if Continue_6 is starting this frame...
        if Continue_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_6.frameNStart = frameN  # exact frame index
            Continue_6.tStart = t  # local t and not account for scr refresh
            Continue_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_6.started')
            # update status
            Continue_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_6.status == STARTED and not waitOnFlip:
            theseKeys = Continue_6.getKeys(keyList=['2','3','space'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_6_allKeys.extend(theseKeys)
            if len(_Continue_6_allKeys):
                Continue_6.keys = _Continue_6_allKeys[-1].name  # just the last key pressed
                Continue_6.rt = _Continue_6_allKeys[-1].rt
                Continue_6.duration = _Continue_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instruction_5* updates
        
        # if Instruction_5 is starting this frame...
        if Instruction_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_5.frameNStart = frameN  # exact frame index
            Instruction_5.tStart = t  # local t and not account for scr refresh
            Instruction_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_5.started')
            # update status
            Instruction_5.status = STARTED
            Instruction_5.setAutoDraw(True)
        
        # if Instruction_5 is active this frame...
        if Instruction_5.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_5.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_5.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_5" ---
    for thisComponent in Instructions_5.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_5
    Instructions_5.tStop = globalClock.getTime(format='float')
    Instructions_5.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_5.stopped', Instructions_5.tStop)
    # check responses
    if Continue_6.keys in ['', [], None]:  # No response was made
        Continue_6.keys = None
    thisExp.addData('Continue_6.keys',Continue_6.keys)
    if Continue_6.keys != None:  # we had a response
        thisExp.addData('Continue_6.rt', Continue_6.rt)
        thisExp.addData('Continue_6.duration', Continue_6.duration)
    thisExp.nextEntry()
    # the Routine "Instructions_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Waiting4Scanner" ---
    # create an object to store info about Routine Waiting4Scanner
    Waiting4Scanner = data.Routine(
        name='Waiting4Scanner',
        components=[Continue_7, Scanner_Instruction],
    )
    Waiting4Scanner.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_7
    Continue_7.keys = []
    Continue_7.rt = []
    _Continue_7_allKeys = []
    Scanner_Instruction.reset()
    # Run 'Begin Routine' code from skip_run_1_logic_6
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Waiting4Scanner
    Waiting4Scanner.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Waiting4Scanner.tStart = globalClock.getTime(format='float')
    Waiting4Scanner.status = STARTED
    thisExp.addData('Waiting4Scanner.started', Waiting4Scanner.tStart)
    Waiting4Scanner.maxDuration = None
    # keep track of which components have finished
    Waiting4ScannerComponents = Waiting4Scanner.components
    for thisComponent in Waiting4Scanner.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting4Scanner" ---
    Waiting4Scanner.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_7* updates
        waitOnFlip = False
        
        # if Continue_7 is starting this frame...
        if Continue_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_7.frameNStart = frameN  # exact frame index
            Continue_7.tStart = t  # local t and not account for scr refresh
            Continue_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_7.started')
            # update status
            Continue_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_7.status == STARTED and not waitOnFlip:
            theseKeys = Continue_7.getKeys(keyList=['5'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_7_allKeys.extend(theseKeys)
            if len(_Continue_7_allKeys):
                Continue_7.keys = _Continue_7_allKeys[-1].name  # just the last key pressed
                Continue_7.rt = _Continue_7_allKeys[-1].rt
                Continue_7.duration = _Continue_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Scanner_Instruction* updates
        
        # if Scanner_Instruction is starting this frame...
        if Scanner_Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scanner_Instruction.frameNStart = frameN  # exact frame index
            Scanner_Instruction.tStart = t  # local t and not account for scr refresh
            Scanner_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scanner_Instruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scanner_Instruction.started')
            # update status
            Scanner_Instruction.status = STARTED
            Scanner_Instruction.setAutoDraw(True)
        
        # if Scanner_Instruction is active this frame...
        if Scanner_Instruction.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Waiting4Scanner.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting4Scanner.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting4Scanner" ---
    for thisComponent in Waiting4Scanner.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Waiting4Scanner
    Waiting4Scanner.tStop = globalClock.getTime(format='float')
    Waiting4Scanner.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Waiting4Scanner.stopped', Waiting4Scanner.tStop)
    # check responses
    if Continue_7.keys in ['', [], None]:  # No response was made
        Continue_7.keys = None
    thisExp.addData('Continue_7.keys',Continue_7.keys)
    if Continue_7.keys != None:  # we had a response
        thisExp.addData('Continue_7.rt', Continue_7.rt)
        thisExp.addData('Continue_7.duration', Continue_7.duration)
    thisExp.nextEntry()
    # the Routine "Waiting4Scanner" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    BlockLoop_Run1 = data.TrialHandler2(
        name='BlockLoop_Run1',
        nReps=num_blocks_run1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(BlockLoop_Run1)  # add the loop to the experiment
    thisBlockLoop_Run1 = BlockLoop_Run1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop_Run1.rgb)
    if thisBlockLoop_Run1 != None:
        for paramName in thisBlockLoop_Run1:
            globals()[paramName] = thisBlockLoop_Run1[paramName]
    
    for thisBlockLoop_Run1 in BlockLoop_Run1:
        currentLoop = BlockLoop_Run1
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop_Run1.rgb)
        if thisBlockLoop_Run1 != None:
            for paramName in thisBlockLoop_Run1:
                globals()[paramName] = thisBlockLoop_Run1[paramName]
        
        # --- Prepare to start Routine "CueFix_Run1" ---
        # create an object to store info about Routine CueFix_Run1
        CueFix_Run1 = data.Routine(
            name='CueFix_Run1',
            components=[Cue_Fix],
        )
        CueFix_Run1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Cue_Fix.reset()
        # Run 'Begin Routine' code from run_Block_1
        currentRun = 1
        currentBlock = BlockLoop_Run1.thisN
        # Run 'Begin Routine' code from skip_loop_logic
        if initialRun == 2:
            BlockLoop_Run1.finished = True
            continueRoutine = False
        # store start times for CueFix_Run1
        CueFix_Run1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        CueFix_Run1.tStart = globalClock.getTime(format='float')
        CueFix_Run1.status = STARTED
        thisExp.addData('CueFix_Run1.started', CueFix_Run1.tStart)
        CueFix_Run1.maxDuration = None
        # keep track of which components have finished
        CueFix_Run1Components = CueFix_Run1.components
        for thisComponent in CueFix_Run1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "CueFix_Run1" ---
        # if trial has changed, end Routine now
        if isinstance(BlockLoop_Run1, data.TrialHandler2) and thisBlockLoop_Run1.thisN != BlockLoop_Run1.thisTrial.thisN:
            continueRoutine = False
        CueFix_Run1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Cue_Fix* updates
            
            # if Cue_Fix is starting this frame...
            if Cue_Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Cue_Fix.frameNStart = frameN  # exact frame index
                Cue_Fix.tStart = t  # local t and not account for scr refresh
                Cue_Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cue_Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cue_Fix.started')
                # update status
                Cue_Fix.status = STARTED
                Cue_Fix.setAutoDraw(True)
            
            # if Cue_Fix is active this frame...
            if Cue_Fix.status == STARTED:
                # update params
                pass
            
            # if Cue_Fix is stopping this frame...
            if Cue_Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Cue_Fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Cue_Fix.tStop = t  # not accounting for scr refresh
                    Cue_Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Cue_Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cue_Fix.stopped')
                    # update status
                    Cue_Fix.status = FINISHED
                    Cue_Fix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                CueFix_Run1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CueFix_Run1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "CueFix_Run1" ---
        for thisComponent in CueFix_Run1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for CueFix_Run1
        CueFix_Run1.tStop = globalClock.getTime(format='float')
        CueFix_Run1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('CueFix_Run1.stopped', CueFix_Run1.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if CueFix_Run1.maxDurationReached:
            routineTimer.addTime(-CueFix_Run1.maxDuration)
        elif CueFix_Run1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # set up handler to look after randomisation of conditions etc
        TrialLoop_Run1 = data.TrialHandler2(
            name='TrialLoop_Run1',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(blockFile1), 
            seed=None, 
        )
        thisExp.addLoop(TrialLoop_Run1)  # add the loop to the experiment
        thisTrialLoop_Run1 = TrialLoop_Run1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop_Run1.rgb)
        if thisTrialLoop_Run1 != None:
            for paramName in thisTrialLoop_Run1:
                globals()[paramName] = thisTrialLoop_Run1[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrialLoop_Run1 in TrialLoop_Run1:
            currentLoop = TrialLoop_Run1
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop_Run1.rgb)
            if thisTrialLoop_Run1 != None:
                for paramName in thisTrialLoop_Run1:
                    globals()[paramName] = thisTrialLoop_Run1[paramName]
            
            # --- Prepare to start Routine "Cue2Back" ---
            # create an object to store info about Routine Cue2Back
            Cue2Back = data.Routine(
                name='Cue2Back',
                components=[Cue_2Back],
            )
            Cue2Back.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            Cue_2Back.reset()
            # Run 'Begin Routine' code from skip_loop_logic_2
            if initialRun == 2:
                TrialLoop_Run1.finished = True
                continueRoutine = False
            # store start times for Cue2Back
            Cue2Back.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Cue2Back.tStart = globalClock.getTime(format='float')
            Cue2Back.status = STARTED
            thisExp.addData('Cue2Back.started', Cue2Back.tStart)
            Cue2Back.maxDuration = 2.5
            # skip Routine Cue2Back if its 'Skip if' condition is True
            Cue2Back.skipped = continueRoutine and not (not (BlockType == '2-Back' and ID == 1))
            continueRoutine = Cue2Back.skipped
            # keep track of which components have finished
            Cue2BackComponents = Cue2Back.components
            for thisComponent in Cue2Back.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Cue2Back" ---
            # if trial has changed, end Routine now
            if isinstance(TrialLoop_Run1, data.TrialHandler2) and thisTrialLoop_Run1.thisN != TrialLoop_Run1.thisTrial.thisN:
                continueRoutine = False
            Cue2Back.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > Cue2Back.maxDuration-frameTolerance:
                    Cue2Back.maxDurationReached = True
                    continueRoutine = False
                
                # *Cue_2Back* updates
                
                # if Cue_2Back is starting this frame...
                if Cue_2Back.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Cue_2Back.frameNStart = frameN  # exact frame index
                    Cue_2Back.tStart = t  # local t and not account for scr refresh
                    Cue_2Back.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cue_2Back, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cue_2Back.started')
                    # update status
                    Cue_2Back.status = STARTED
                    Cue_2Back.setAutoDraw(True)
                
                # if Cue_2Back is active this frame...
                if Cue_2Back.status == STARTED:
                    # update params
                    pass
                
                # if Cue_2Back is stopping this frame...
                if Cue_2Back.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Cue_2Back.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Cue_2Back.tStop = t  # not accounting for scr refresh
                        Cue_2Back.tStopRefresh = tThisFlipGlobal  # on global time
                        Cue_2Back.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Cue_2Back.stopped')
                        # update status
                        Cue_2Back.status = FINISHED
                        Cue_2Back.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Cue2Back.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Cue2Back.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Cue2Back" ---
            for thisComponent in Cue2Back.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Cue2Back
            Cue2Back.tStop = globalClock.getTime(format='float')
            Cue2Back.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Cue2Back.stopped', Cue2Back.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Cue2Back.maxDurationReached:
                routineTimer.addTime(-Cue2Back.maxDuration)
            elif Cue2Back.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.500000)
            
            # --- Prepare to start Routine "Cue0Back" ---
            # create an object to store info about Routine Cue0Back
            Cue0Back = data.Routine(
                name='Cue0Back',
                components=[Cue_Target, Cue_TargetImage, Zero_back],
            )
            Cue0Back.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from targetImageLogic
            if BlockType == "0-Back":
                targetImage = TargetStimulus
            else:
                targetImage = 'blackbg.png'
            Cue_Target.reset()
            Cue_TargetImage.setImage(targetImage)
            # Run 'Begin Routine' code from skip_run_1_logic_9
            # Skip this routine if initial run is 2
            if initialRun == 2:
                continueRoutine = False
            Zero_back.reset()
            # store start times for Cue0Back
            Cue0Back.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Cue0Back.tStart = globalClock.getTime(format='float')
            Cue0Back.status = STARTED
            thisExp.addData('Cue0Back.started', Cue0Back.tStart)
            Cue0Back.maxDuration = 2.5
            # skip Routine Cue0Back if its 'Skip if' condition is True
            Cue0Back.skipped = continueRoutine and not (not (BlockType == '0-Back' and ID == 1))
            continueRoutine = Cue0Back.skipped
            # keep track of which components have finished
            Cue0BackComponents = Cue0Back.components
            for thisComponent in Cue0Back.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Cue0Back" ---
            # if trial has changed, end Routine now
            if isinstance(TrialLoop_Run1, data.TrialHandler2) and thisTrialLoop_Run1.thisN != TrialLoop_Run1.thisTrial.thisN:
                continueRoutine = False
            Cue0Back.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > Cue0Back.maxDuration-frameTolerance:
                    Cue0Back.maxDurationReached = True
                    continueRoutine = False
                
                # *Cue_Target* updates
                
                # if Cue_Target is starting this frame...
                if Cue_Target.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Cue_Target.frameNStart = frameN  # exact frame index
                    Cue_Target.tStart = t  # local t and not account for scr refresh
                    Cue_Target.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cue_Target, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cue_Target.started')
                    # update status
                    Cue_Target.status = STARTED
                    Cue_Target.setAutoDraw(True)
                
                # if Cue_Target is active this frame...
                if Cue_Target.status == STARTED:
                    # update params
                    pass
                
                # if Cue_Target is stopping this frame...
                if Cue_Target.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Cue_Target.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Cue_Target.tStop = t  # not accounting for scr refresh
                        Cue_Target.tStopRefresh = tThisFlipGlobal  # on global time
                        Cue_Target.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Cue_Target.stopped')
                        # update status
                        Cue_Target.status = FINISHED
                        Cue_Target.setAutoDraw(False)
                
                # *Cue_TargetImage* updates
                
                # if Cue_TargetImage is starting this frame...
                if Cue_TargetImage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Cue_TargetImage.frameNStart = frameN  # exact frame index
                    Cue_TargetImage.tStart = t  # local t and not account for scr refresh
                    Cue_TargetImage.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cue_TargetImage, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cue_TargetImage.started')
                    # update status
                    Cue_TargetImage.status = STARTED
                    Cue_TargetImage.setAutoDraw(True)
                
                # if Cue_TargetImage is active this frame...
                if Cue_TargetImage.status == STARTED:
                    # update params
                    pass
                
                # if Cue_TargetImage is stopping this frame...
                if Cue_TargetImage.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Cue_TargetImage.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Cue_TargetImage.tStop = t  # not accounting for scr refresh
                        Cue_TargetImage.tStopRefresh = tThisFlipGlobal  # on global time
                        Cue_TargetImage.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Cue_TargetImage.stopped')
                        # update status
                        Cue_TargetImage.status = FINISHED
                        Cue_TargetImage.setAutoDraw(False)
                
                # *Zero_back* updates
                
                # if Zero_back is starting this frame...
                if Zero_back.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Zero_back.frameNStart = frameN  # exact frame index
                    Zero_back.tStart = t  # local t and not account for scr refresh
                    Zero_back.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Zero_back, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Zero_back.started')
                    # update status
                    Zero_back.status = STARTED
                    Zero_back.setAutoDraw(True)
                
                # if Zero_back is active this frame...
                if Zero_back.status == STARTED:
                    # update params
                    pass
                
                # if Zero_back is stopping this frame...
                if Zero_back.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Zero_back.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Zero_back.tStop = t  # not accounting for scr refresh
                        Zero_back.tStopRefresh = tThisFlipGlobal  # on global time
                        Zero_back.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Zero_back.stopped')
                        # update status
                        Zero_back.status = FINISHED
                        Zero_back.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Cue0Back.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Cue0Back.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Cue0Back" ---
            for thisComponent in Cue0Back.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Cue0Back
            Cue0Back.tStop = globalClock.getTime(format='float')
            Cue0Back.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Cue0Back.stopped', Cue0Back.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Cue0Back.maxDurationReached:
                routineTimer.addTime(-Cue0Back.maxDuration)
            elif Cue0Back.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.500000)
            
            # --- Prepare to start Routine "Stim" ---
            # create an object to store info about Routine Stim
            Stim = data.Routine(
                name='Stim',
                components=[StimulusImage, LeftScreenResponse, RightScreenResponse, response],
            )
            Stim.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from targetLogic
            if CorrectResponse == 'Target':
                correctKey = matchKey
            else:
                correctKey = noMatchKey
            
            StimulusImage.setImage(Stimulus)
            LeftScreenResponse.reset()
            LeftScreenResponse.setText(leftSideOfScreen)
            RightScreenResponse.reset()
            RightScreenResponse.setText(rightSideOfScreen)
            # create starting attributes for response
            response.keys = []
            response.rt = []
            _response_allKeys = []
            # Run 'Begin Routine' code from skip_run_1_logic_10
            # Skip this routine if initial run is 2
            if initialRun == 2:
                continueRoutine = False
            # store start times for Stim
            Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Stim.tStart = globalClock.getTime(format='float')
            Stim.status = STARTED
            thisExp.addData('Stim.started', Stim.tStart)
            Stim.maxDuration = None
            # keep track of which components have finished
            StimComponents = Stim.components
            for thisComponent in Stim.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Stim" ---
            # if trial has changed, end Routine now
            if isinstance(TrialLoop_Run1, data.TrialHandler2) and thisTrialLoop_Run1.thisN != TrialLoop_Run1.thisTrial.thisN:
                continueRoutine = False
            Stim.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *StimulusImage* updates
                
                # if StimulusImage is starting this frame...
                if StimulusImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    StimulusImage.frameNStart = frameN  # exact frame index
                    StimulusImage.tStart = t  # local t and not account for scr refresh
                    StimulusImage.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(StimulusImage, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'StimulusImage.started')
                    # update status
                    StimulusImage.status = STARTED
                    StimulusImage.setAutoDraw(True)
                
                # if StimulusImage is active this frame...
                if StimulusImage.status == STARTED:
                    # update params
                    pass
                
                # if StimulusImage is stopping this frame...
                if StimulusImage.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > StimulusImage.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        StimulusImage.tStop = t  # not accounting for scr refresh
                        StimulusImage.tStopRefresh = tThisFlipGlobal  # on global time
                        StimulusImage.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'StimulusImage.stopped')
                        # update status
                        StimulusImage.status = FINISHED
                        StimulusImage.setAutoDraw(False)
                
                # *LeftScreenResponse* updates
                
                # if LeftScreenResponse is starting this frame...
                if LeftScreenResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    LeftScreenResponse.frameNStart = frameN  # exact frame index
                    LeftScreenResponse.tStart = t  # local t and not account for scr refresh
                    LeftScreenResponse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LeftScreenResponse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LeftScreenResponse.started')
                    # update status
                    LeftScreenResponse.status = STARTED
                    LeftScreenResponse.setAutoDraw(True)
                
                # if LeftScreenResponse is active this frame...
                if LeftScreenResponse.status == STARTED:
                    # update params
                    pass
                
                # if LeftScreenResponse is stopping this frame...
                if LeftScreenResponse.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LeftScreenResponse.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        LeftScreenResponse.tStop = t  # not accounting for scr refresh
                        LeftScreenResponse.tStopRefresh = tThisFlipGlobal  # on global time
                        LeftScreenResponse.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'LeftScreenResponse.stopped')
                        # update status
                        LeftScreenResponse.status = FINISHED
                        LeftScreenResponse.setAutoDraw(False)
                
                # *RightScreenResponse* updates
                
                # if RightScreenResponse is starting this frame...
                if RightScreenResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RightScreenResponse.frameNStart = frameN  # exact frame index
                    RightScreenResponse.tStart = t  # local t and not account for scr refresh
                    RightScreenResponse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RightScreenResponse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RightScreenResponse.started')
                    # update status
                    RightScreenResponse.status = STARTED
                    RightScreenResponse.setAutoDraw(True)
                
                # if RightScreenResponse is active this frame...
                if RightScreenResponse.status == STARTED:
                    # update params
                    pass
                
                # if RightScreenResponse is stopping this frame...
                if RightScreenResponse.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RightScreenResponse.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        RightScreenResponse.tStop = t  # not accounting for scr refresh
                        RightScreenResponse.tStopRefresh = tThisFlipGlobal  # on global time
                        RightScreenResponse.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'RightScreenResponse.stopped')
                        # update status
                        RightScreenResponse.status = FINISHED
                        RightScreenResponse.setAutoDraw(False)
                
                # *response* updates
                waitOnFlip = False
                
                # if response is starting this frame...
                if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    response.frameNStart = frameN  # exact frame index
                    response.tStart = t  # local t and not account for scr refresh
                    response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response.started')
                    # update status
                    response.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if response is stopping this frame...
                if response.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        response.tStop = t  # not accounting for scr refresh
                        response.tStopRefresh = tThisFlipGlobal  # on global time
                        response.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response.stopped')
                        # update status
                        response.status = FINISHED
                        response.status = FINISHED
                if response.status == STARTED and not waitOnFlip:
                    theseKeys = response.getKeys(keyList=['2','3'], ignoreKeys=["escape"], waitRelease=False)
                    _response_allKeys.extend(theseKeys)
                    if len(_response_allKeys):
                        response.keys = _response_allKeys[0].name  # just the first key pressed
                        response.rt = _response_allKeys[0].rt
                        response.duration = _response_allKeys[0].duration
                        # was this correct?
                        if (response.keys == str(correctKey)) or (response.keys == correctKey):
                            response.corr = 1
                        else:
                            response.corr = 0
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Stim.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Stim.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Stim" ---
            for thisComponent in Stim.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Stim
            Stim.tStop = globalClock.getTime(format='float')
            Stim.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Stim.stopped', Stim.tStop)
            # check responses
            if response.keys in ['', [], None]:  # No response was made
                response.keys = None
                # was no response the correct answer?!
                if str(correctKey).lower() == 'none':
                   response.corr = 1;  # correct non-response
                else:
                   response.corr = 0;  # failed to respond (incorrectly)
            # store data for TrialLoop_Run1 (TrialHandler)
            TrialLoop_Run1.addData('response.keys',response.keys)
            TrialLoop_Run1.addData('response.corr', response.corr)
            if response.keys != None:  # we had a response
                TrialLoop_Run1.addData('response.rt', response.rt)
                TrialLoop_Run1.addData('response.duration', response.duration)
            # Run 'End Routine' code from recordDataLogic
            # -------------------------------
            # Collect trial data
            # -------------------------------
            
            from datetime import date
            from datetime import datetime
            # Get current date and time
            current_datetime = datetime.now()
            # Format the time as a string (e.g., "14:30:45")
            formatted_time = current_datetime.strftime("%H:%M:%S")
            
            response_key = response.keys if response.keys is not None else 'NA'
            response_rt  = response.rt if response.keys is not None else 'NA'
            accuracy     = response.corr if response.keys is not None else 'NA'
            
            if BlockType == "0-Back":
                target_stim_value = TargetStimulus
            elif BlockType == "2-Back":
                target_stim_value = 'NA'
            
            trial_data = [
                expInfo["Please select version:"],
                currentRun,
                currentBlock+1,
                ID,
                BlockType,
                StimType,
                Stimulus,
                target_stim_value,
                TargetType,
                response_key,
                response_rt,
                accuracy,
                expInfo["Enter subject\'s handedness:"],
                date.today(),
                formatted_time,
                globalClock.getTime()
            ]
            
            # -------------------------------
            # Append to CSV
            # -------------------------------
            
            with open(filename, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(trial_data)
            
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Stim.maxDurationReached:
                routineTimer.addTime(-Stim.maxDuration)
            elif Stim.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            
            # --- Prepare to start Routine "Fix" ---
            # create an object to store info about Routine Fix
            Fix = data.Routine(
                name='Fix',
                components=[End_Fix],
            )
            Fix.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            End_Fix.reset()
            # Run 'Begin Routine' code from skip_run_1_logic_11
            # Skip this routine if initial run is 2
            if initialRun == 2:
                continueRoutine = False
            # store start times for Fix
            Fix.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Fix.tStart = globalClock.getTime(format='float')
            Fix.status = STARTED
            thisExp.addData('Fix.started', Fix.tStart)
            Fix.maxDuration = None
            # keep track of which components have finished
            FixComponents = Fix.components
            for thisComponent in Fix.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Fix" ---
            # if trial has changed, end Routine now
            if isinstance(TrialLoop_Run1, data.TrialHandler2) and thisTrialLoop_Run1.thisN != TrialLoop_Run1.thisTrial.thisN:
                continueRoutine = False
            Fix.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *End_Fix* updates
                
                # if End_Fix is starting this frame...
                if End_Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    End_Fix.frameNStart = frameN  # exact frame index
                    End_Fix.tStart = t  # local t and not account for scr refresh
                    End_Fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(End_Fix, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'End_Fix.started')
                    # update status
                    End_Fix.status = STARTED
                    End_Fix.setAutoDraw(True)
                
                # if End_Fix is active this frame...
                if End_Fix.status == STARTED:
                    # update params
                    pass
                
                # if End_Fix is stopping this frame...
                if End_Fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > End_Fix.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        End_Fix.tStop = t  # not accounting for scr refresh
                        End_Fix.tStopRefresh = tThisFlipGlobal  # on global time
                        End_Fix.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'End_Fix.stopped')
                        # update status
                        End_Fix.status = FINISHED
                        End_Fix.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Fix.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Fix.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Fix" ---
            for thisComponent in Fix.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Fix
            Fix.tStop = globalClock.getTime(format='float')
            Fix.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Fix.stopped', Fix.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Fix.maxDurationReached:
                routineTimer.addTime(-Fix.maxDuration)
            elif Fix.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'TrialLoop_Run1'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "EndBlock_Run1" ---
        # create an object to store info about Routine EndBlock_Run1
        EndBlock_Run1 = data.Routine(
            name='EndBlock_Run1',
            components=[],
        )
        EndBlock_Run1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from skip_run_1_logic_12
        # Skip this routine if initial run is 2
        if initialRun == 2:
            continueRoutine = False
        # store start times for EndBlock_Run1
        EndBlock_Run1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        EndBlock_Run1.tStart = globalClock.getTime(format='float')
        EndBlock_Run1.status = STARTED
        thisExp.addData('EndBlock_Run1.started', EndBlock_Run1.tStart)
        EndBlock_Run1.maxDuration = None
        # keep track of which components have finished
        EndBlock_Run1Components = EndBlock_Run1.components
        for thisComponent in EndBlock_Run1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EndBlock_Run1" ---
        # if trial has changed, end Routine now
        if isinstance(BlockLoop_Run1, data.TrialHandler2) and thisBlockLoop_Run1.thisN != BlockLoop_Run1.thisTrial.thisN:
            continueRoutine = False
        EndBlock_Run1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                EndBlock_Run1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EndBlock_Run1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EndBlock_Run1" ---
        for thisComponent in EndBlock_Run1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for EndBlock_Run1
        EndBlock_Run1.tStop = globalClock.getTime(format='float')
        EndBlock_Run1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('EndBlock_Run1.stopped', EndBlock_Run1.tStop)
        # Run 'End Routine' code from blockLoopLogic_Run1
        # Move to next block
        blockIndex1 += 1
        
        if blockIndex1 >= len(blockFilesRun1):
            BlockLoop_Run1.finished = True
        else:
            # Load current block CSV dynamically
            blockFile1 = os.path.join(run1Folder, blockFilesRun1[blockIndex1])
            # Load data from a CSV file into a list of dictionaries
            csvData1 = data.importConditions(blockFile1)
            # Convert the list of dictionaries to a pandas DataFrame
            df1 = pd.DataFrame(csvData1)
        
        # the Routine "EndBlock_Run1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed num_blocks_run1 repeats of 'BlockLoop_Run1'
    
    
    # --- Prepare to start Routine "Fix15Sec" ---
    # create an object to store info about Routine Fix15Sec
    Fix15Sec = data.Routine(
        name='Fix15Sec',
        components=[Fix_15_Sec],
    )
    Fix15Sec.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    Fix_15_Sec.reset()
    # Run 'Begin Routine' code from skip_run_1_logic_7
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Fix15Sec
    Fix15Sec.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Fix15Sec.tStart = globalClock.getTime(format='float')
    Fix15Sec.status = STARTED
    thisExp.addData('Fix15Sec.started', Fix15Sec.tStart)
    Fix15Sec.maxDuration = None
    # keep track of which components have finished
    Fix15SecComponents = Fix15Sec.components
    for thisComponent in Fix15Sec.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fix15Sec" ---
    Fix15Sec.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fix_15_Sec* updates
        
        # if Fix_15_Sec is starting this frame...
        if Fix_15_Sec.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Fix_15_Sec.frameNStart = frameN  # exact frame index
            Fix_15_Sec.tStart = t  # local t and not account for scr refresh
            Fix_15_Sec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fix_15_Sec, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fix_15_Sec.started')
            # update status
            Fix_15_Sec.status = STARTED
            Fix_15_Sec.setAutoDraw(True)
        
        # if Fix_15_Sec is active this frame...
        if Fix_15_Sec.status == STARTED:
            # update params
            pass
        
        # if Fix_15_Sec is stopping this frame...
        if Fix_15_Sec.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fix_15_Sec.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Fix_15_Sec.tStop = t  # not accounting for scr refresh
                Fix_15_Sec.tStopRefresh = tThisFlipGlobal  # on global time
                Fix_15_Sec.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix_15_Sec.stopped')
                # update status
                Fix_15_Sec.status = FINISHED
                Fix_15_Sec.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Fix15Sec.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fix15Sec.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fix15Sec" ---
    for thisComponent in Fix15Sec.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Fix15Sec
    Fix15Sec.tStop = globalClock.getTime(format='float')
    Fix15Sec.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Fix15Sec.stopped', Fix15Sec.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Fix15Sec.maxDurationReached:
        routineTimer.addTime(-Fix15Sec.maxDuration)
    elif Fix15Sec.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Fix5Sec" ---
    # create an object to store info about Routine Fix5Sec
    Fix5Sec = data.Routine(
        name='Fix5Sec',
        components=[Fix_5_Sec],
    )
    Fix5Sec.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    Fix_5_Sec.reset()
    # Run 'Begin Routine' code from skip_run_1_logic_8
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Fix5Sec
    Fix5Sec.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Fix5Sec.tStart = globalClock.getTime(format='float')
    Fix5Sec.status = STARTED
    thisExp.addData('Fix5Sec.started', Fix5Sec.tStart)
    Fix5Sec.maxDuration = None
    # keep track of which components have finished
    Fix5SecComponents = Fix5Sec.components
    for thisComponent in Fix5Sec.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fix5Sec" ---
    Fix5Sec.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fix_5_Sec* updates
        
        # if Fix_5_Sec is starting this frame...
        if Fix_5_Sec.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Fix_5_Sec.frameNStart = frameN  # exact frame index
            Fix_5_Sec.tStart = t  # local t and not account for scr refresh
            Fix_5_Sec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fix_5_Sec, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fix_5_Sec.started')
            # update status
            Fix_5_Sec.status = STARTED
            Fix_5_Sec.setAutoDraw(True)
        
        # if Fix_5_Sec is active this frame...
        if Fix_5_Sec.status == STARTED:
            # update params
            pass
        
        # if Fix_5_Sec is stopping this frame...
        if Fix_5_Sec.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fix_5_Sec.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Fix_5_Sec.tStop = t  # not accounting for scr refresh
                Fix_5_Sec.tStopRefresh = tThisFlipGlobal  # on global time
                Fix_5_Sec.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix_5_Sec.stopped')
                # update status
                Fix_5_Sec.status = FINISHED
                Fix_5_Sec.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Fix5Sec.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fix5Sec.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fix5Sec" ---
    for thisComponent in Fix5Sec.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Fix5Sec
    Fix5Sec.tStop = globalClock.getTime(format='float')
    Fix5Sec.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Fix5Sec.stopped', Fix5Sec.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Fix5Sec.maxDurationReached:
        routineTimer.addTime(-Fix5Sec.maxDuration)
    elif Fix5Sec.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Instructions_6" ---
    # create an object to store info about Routine Instructions_6
    Instructions_6 = data.Routine(
        name='Instructions_6',
        components=[Continue_8, Instruction_6],
    )
    Instructions_6.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_8
    Continue_8.keys = []
    Continue_8.rt = []
    _Continue_8_allKeys = []
    Instruction_6.reset()
    # Run 'Begin Routine' code from increase_run
    if initialRun == 2:
        initialRun = 3
    # store start times for Instructions_6
    Instructions_6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_6.tStart = globalClock.getTime(format='float')
    Instructions_6.status = STARTED
    thisExp.addData('Instructions_6.started', Instructions_6.tStart)
    Instructions_6.maxDuration = None
    # keep track of which components have finished
    Instructions_6Components = Instructions_6.components
    for thisComponent in Instructions_6.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_6" ---
    Instructions_6.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_8* updates
        waitOnFlip = False
        
        # if Continue_8 is starting this frame...
        if Continue_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_8.frameNStart = frameN  # exact frame index
            Continue_8.tStart = t  # local t and not account for scr refresh
            Continue_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_8.started')
            # update status
            Continue_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_8.status == STARTED and not waitOnFlip:
            theseKeys = Continue_8.getKeys(keyList=['2','3','space'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_8_allKeys.extend(theseKeys)
            if len(_Continue_8_allKeys):
                Continue_8.keys = _Continue_8_allKeys[-1].name  # just the last key pressed
                Continue_8.rt = _Continue_8_allKeys[-1].rt
                Continue_8.duration = _Continue_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instruction_6* updates
        
        # if Instruction_6 is starting this frame...
        if Instruction_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_6.frameNStart = frameN  # exact frame index
            Instruction_6.tStart = t  # local t and not account for scr refresh
            Instruction_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_6.started')
            # update status
            Instruction_6.status = STARTED
            Instruction_6.setAutoDraw(True)
        
        # if Instruction_6 is active this frame...
        if Instruction_6.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_6.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_6.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_6" ---
    for thisComponent in Instructions_6.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_6
    Instructions_6.tStop = globalClock.getTime(format='float')
    Instructions_6.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_6.stopped', Instructions_6.tStop)
    # check responses
    if Continue_8.keys in ['', [], None]:  # No response was made
        Continue_8.keys = None
    thisExp.addData('Continue_8.keys',Continue_8.keys)
    if Continue_8.keys != None:  # we had a response
        thisExp.addData('Continue_8.rt', Continue_8.rt)
        thisExp.addData('Continue_8.duration', Continue_8.duration)
    thisExp.nextEntry()
    # the Routine "Instructions_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_7" ---
    # create an object to store info about Routine Instructions_7
    Instructions_7 = data.Routine(
        name='Instructions_7',
        components=[Continue_9, Instruction_7],
    )
    Instructions_7.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_9
    Continue_9.keys = []
    Continue_9.rt = []
    _Continue_9_allKeys = []
    Instruction_7.reset()
    # store start times for Instructions_7
    Instructions_7.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_7.tStart = globalClock.getTime(format='float')
    Instructions_7.status = STARTED
    thisExp.addData('Instructions_7.started', Instructions_7.tStart)
    Instructions_7.maxDuration = None
    # keep track of which components have finished
    Instructions_7Components = Instructions_7.components
    for thisComponent in Instructions_7.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_7" ---
    Instructions_7.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_9* updates
        waitOnFlip = False
        
        # if Continue_9 is starting this frame...
        if Continue_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_9.frameNStart = frameN  # exact frame index
            Continue_9.tStart = t  # local t and not account for scr refresh
            Continue_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_9.started')
            # update status
            Continue_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_9.status == STARTED and not waitOnFlip:
            theseKeys = Continue_9.getKeys(keyList=['2','3','space'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_9_allKeys.extend(theseKeys)
            if len(_Continue_9_allKeys):
                Continue_9.keys = _Continue_9_allKeys[-1].name  # just the last key pressed
                Continue_9.rt = _Continue_9_allKeys[-1].rt
                Continue_9.duration = _Continue_9_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instruction_7* updates
        
        # if Instruction_7 is starting this frame...
        if Instruction_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_7.frameNStart = frameN  # exact frame index
            Instruction_7.tStart = t  # local t and not account for scr refresh
            Instruction_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_7.started')
            # update status
            Instruction_7.status = STARTED
            Instruction_7.setAutoDraw(True)
        
        # if Instruction_7 is active this frame...
        if Instruction_7.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_7.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_7.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_7" ---
    for thisComponent in Instructions_7.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_7
    Instructions_7.tStop = globalClock.getTime(format='float')
    Instructions_7.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_7.stopped', Instructions_7.tStop)
    # check responses
    if Continue_9.keys in ['', [], None]:  # No response was made
        Continue_9.keys = None
    thisExp.addData('Continue_9.keys',Continue_9.keys)
    if Continue_9.keys != None:  # we had a response
        thisExp.addData('Continue_9.rt', Continue_9.rt)
        thisExp.addData('Continue_9.duration', Continue_9.duration)
    thisExp.nextEntry()
    # the Routine "Instructions_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Waiting4Scanner" ---
    # create an object to store info about Routine Waiting4Scanner
    Waiting4Scanner = data.Routine(
        name='Waiting4Scanner',
        components=[Continue_7, Scanner_Instruction],
    )
    Waiting4Scanner.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Continue_7
    Continue_7.keys = []
    Continue_7.rt = []
    _Continue_7_allKeys = []
    Scanner_Instruction.reset()
    # Run 'Begin Routine' code from skip_run_1_logic_6
    # Skip this routine if initial run is 2
    if initialRun == 2:
        continueRoutine = False
    # store start times for Waiting4Scanner
    Waiting4Scanner.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Waiting4Scanner.tStart = globalClock.getTime(format='float')
    Waiting4Scanner.status = STARTED
    thisExp.addData('Waiting4Scanner.started', Waiting4Scanner.tStart)
    Waiting4Scanner.maxDuration = None
    # keep track of which components have finished
    Waiting4ScannerComponents = Waiting4Scanner.components
    for thisComponent in Waiting4Scanner.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Waiting4Scanner" ---
    Waiting4Scanner.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Continue_7* updates
        waitOnFlip = False
        
        # if Continue_7 is starting this frame...
        if Continue_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue_7.frameNStart = frameN  # exact frame index
            Continue_7.tStart = t  # local t and not account for scr refresh
            Continue_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Continue_7.started')
            # update status
            Continue_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Continue_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Continue_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Continue_7.status == STARTED and not waitOnFlip:
            theseKeys = Continue_7.getKeys(keyList=['5'], ignoreKeys=["escape"], waitRelease=False)
            _Continue_7_allKeys.extend(theseKeys)
            if len(_Continue_7_allKeys):
                Continue_7.keys = _Continue_7_allKeys[-1].name  # just the last key pressed
                Continue_7.rt = _Continue_7_allKeys[-1].rt
                Continue_7.duration = _Continue_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Scanner_Instruction* updates
        
        # if Scanner_Instruction is starting this frame...
        if Scanner_Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Scanner_Instruction.frameNStart = frameN  # exact frame index
            Scanner_Instruction.tStart = t  # local t and not account for scr refresh
            Scanner_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Scanner_Instruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Scanner_Instruction.started')
            # update status
            Scanner_Instruction.status = STARTED
            Scanner_Instruction.setAutoDraw(True)
        
        # if Scanner_Instruction is active this frame...
        if Scanner_Instruction.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Waiting4Scanner.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Waiting4Scanner.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Waiting4Scanner" ---
    for thisComponent in Waiting4Scanner.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Waiting4Scanner
    Waiting4Scanner.tStop = globalClock.getTime(format='float')
    Waiting4Scanner.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Waiting4Scanner.stopped', Waiting4Scanner.tStop)
    # check responses
    if Continue_7.keys in ['', [], None]:  # No response was made
        Continue_7.keys = None
    thisExp.addData('Continue_7.keys',Continue_7.keys)
    if Continue_7.keys != None:  # we had a response
        thisExp.addData('Continue_7.rt', Continue_7.rt)
        thisExp.addData('Continue_7.duration', Continue_7.duration)
    thisExp.nextEntry()
    # the Routine "Waiting4Scanner" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    BlockLoop_Run2 = data.TrialHandler2(
        name='BlockLoop_Run2',
        nReps=num_blocks_run2, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(BlockLoop_Run2)  # add the loop to the experiment
    thisBlockLoop_Run2 = BlockLoop_Run2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop_Run2.rgb)
    if thisBlockLoop_Run2 != None:
        for paramName in thisBlockLoop_Run2:
            globals()[paramName] = thisBlockLoop_Run2[paramName]
    
    for thisBlockLoop_Run2 in BlockLoop_Run2:
        currentLoop = BlockLoop_Run2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop_Run2.rgb)
        if thisBlockLoop_Run2 != None:
            for paramName in thisBlockLoop_Run2:
                globals()[paramName] = thisBlockLoop_Run2[paramName]
        
        # --- Prepare to start Routine "CueFix_Run2" ---
        # create an object to store info about Routine CueFix_Run2
        CueFix_Run2 = data.Routine(
            name='CueFix_Run2',
            components=[Cue_Fix_2],
        )
        CueFix_Run2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Cue_Fix_2.reset()
        # Run 'Begin Routine' code from run_Block_2
        currentRun = 2
        currentBlock = BlockLoop_Run2.thisN
        # store start times for CueFix_Run2
        CueFix_Run2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        CueFix_Run2.tStart = globalClock.getTime(format='float')
        CueFix_Run2.status = STARTED
        thisExp.addData('CueFix_Run2.started', CueFix_Run2.tStart)
        CueFix_Run2.maxDuration = None
        # keep track of which components have finished
        CueFix_Run2Components = CueFix_Run2.components
        for thisComponent in CueFix_Run2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "CueFix_Run2" ---
        # if trial has changed, end Routine now
        if isinstance(BlockLoop_Run2, data.TrialHandler2) and thisBlockLoop_Run2.thisN != BlockLoop_Run2.thisTrial.thisN:
            continueRoutine = False
        CueFix_Run2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Cue_Fix_2* updates
            
            # if Cue_Fix_2 is starting this frame...
            if Cue_Fix_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Cue_Fix_2.frameNStart = frameN  # exact frame index
                Cue_Fix_2.tStart = t  # local t and not account for scr refresh
                Cue_Fix_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Cue_Fix_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cue_Fix_2.started')
                # update status
                Cue_Fix_2.status = STARTED
                Cue_Fix_2.setAutoDraw(True)
            
            # if Cue_Fix_2 is active this frame...
            if Cue_Fix_2.status == STARTED:
                # update params
                pass
            
            # if Cue_Fix_2 is stopping this frame...
            if Cue_Fix_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Cue_Fix_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Cue_Fix_2.tStop = t  # not accounting for scr refresh
                    Cue_Fix_2.tStopRefresh = tThisFlipGlobal  # on global time
                    Cue_Fix_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cue_Fix_2.stopped')
                    # update status
                    Cue_Fix_2.status = FINISHED
                    Cue_Fix_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                CueFix_Run2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CueFix_Run2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "CueFix_Run2" ---
        for thisComponent in CueFix_Run2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for CueFix_Run2
        CueFix_Run2.tStop = globalClock.getTime(format='float')
        CueFix_Run2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('CueFix_Run2.stopped', CueFix_Run2.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if CueFix_Run2.maxDurationReached:
            routineTimer.addTime(-CueFix_Run2.maxDuration)
        elif CueFix_Run2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # set up handler to look after randomisation of conditions etc
        TrialLoop_Run2 = data.TrialHandler2(
            name='TrialLoop_Run2',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(blockFile2), 
            seed=None, 
        )
        thisExp.addLoop(TrialLoop_Run2)  # add the loop to the experiment
        thisTrialLoop_Run2 = TrialLoop_Run2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop_Run2.rgb)
        if thisTrialLoop_Run2 != None:
            for paramName in thisTrialLoop_Run2:
                globals()[paramName] = thisTrialLoop_Run2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrialLoop_Run2 in TrialLoop_Run2:
            currentLoop = TrialLoop_Run2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop_Run2.rgb)
            if thisTrialLoop_Run2 != None:
                for paramName in thisTrialLoop_Run2:
                    globals()[paramName] = thisTrialLoop_Run2[paramName]
            
            # --- Prepare to start Routine "Cue2Back" ---
            # create an object to store info about Routine Cue2Back
            Cue2Back = data.Routine(
                name='Cue2Back',
                components=[Cue_2Back],
            )
            Cue2Back.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            Cue_2Back.reset()
            # Run 'Begin Routine' code from skip_loop_logic_2
            if initialRun == 2:
                TrialLoop_Run1.finished = True
                continueRoutine = False
            # store start times for Cue2Back
            Cue2Back.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Cue2Back.tStart = globalClock.getTime(format='float')
            Cue2Back.status = STARTED
            thisExp.addData('Cue2Back.started', Cue2Back.tStart)
            Cue2Back.maxDuration = 2.5
            # skip Routine Cue2Back if its 'Skip if' condition is True
            Cue2Back.skipped = continueRoutine and not (not (BlockType == '2-Back' and ID == 1))
            continueRoutine = Cue2Back.skipped
            # keep track of which components have finished
            Cue2BackComponents = Cue2Back.components
            for thisComponent in Cue2Back.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Cue2Back" ---
            # if trial has changed, end Routine now
            if isinstance(TrialLoop_Run2, data.TrialHandler2) and thisTrialLoop_Run2.thisN != TrialLoop_Run2.thisTrial.thisN:
                continueRoutine = False
            Cue2Back.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > Cue2Back.maxDuration-frameTolerance:
                    Cue2Back.maxDurationReached = True
                    continueRoutine = False
                
                # *Cue_2Back* updates
                
                # if Cue_2Back is starting this frame...
                if Cue_2Back.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Cue_2Back.frameNStart = frameN  # exact frame index
                    Cue_2Back.tStart = t  # local t and not account for scr refresh
                    Cue_2Back.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cue_2Back, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cue_2Back.started')
                    # update status
                    Cue_2Back.status = STARTED
                    Cue_2Back.setAutoDraw(True)
                
                # if Cue_2Back is active this frame...
                if Cue_2Back.status == STARTED:
                    # update params
                    pass
                
                # if Cue_2Back is stopping this frame...
                if Cue_2Back.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Cue_2Back.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Cue_2Back.tStop = t  # not accounting for scr refresh
                        Cue_2Back.tStopRefresh = tThisFlipGlobal  # on global time
                        Cue_2Back.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Cue_2Back.stopped')
                        # update status
                        Cue_2Back.status = FINISHED
                        Cue_2Back.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Cue2Back.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Cue2Back.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Cue2Back" ---
            for thisComponent in Cue2Back.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Cue2Back
            Cue2Back.tStop = globalClock.getTime(format='float')
            Cue2Back.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Cue2Back.stopped', Cue2Back.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Cue2Back.maxDurationReached:
                routineTimer.addTime(-Cue2Back.maxDuration)
            elif Cue2Back.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.500000)
            
            # --- Prepare to start Routine "Cue0Back" ---
            # create an object to store info about Routine Cue0Back
            Cue0Back = data.Routine(
                name='Cue0Back',
                components=[Cue_Target, Cue_TargetImage, Zero_back],
            )
            Cue0Back.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from targetImageLogic
            if BlockType == "0-Back":
                targetImage = TargetStimulus
            else:
                targetImage = 'blackbg.png'
            Cue_Target.reset()
            Cue_TargetImage.setImage(targetImage)
            # Run 'Begin Routine' code from skip_run_1_logic_9
            # Skip this routine if initial run is 2
            if initialRun == 2:
                continueRoutine = False
            Zero_back.reset()
            # store start times for Cue0Back
            Cue0Back.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Cue0Back.tStart = globalClock.getTime(format='float')
            Cue0Back.status = STARTED
            thisExp.addData('Cue0Back.started', Cue0Back.tStart)
            Cue0Back.maxDuration = 2.5
            # skip Routine Cue0Back if its 'Skip if' condition is True
            Cue0Back.skipped = continueRoutine and not (not (BlockType == '0-Back' and ID == 1))
            continueRoutine = Cue0Back.skipped
            # keep track of which components have finished
            Cue0BackComponents = Cue0Back.components
            for thisComponent in Cue0Back.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Cue0Back" ---
            # if trial has changed, end Routine now
            if isinstance(TrialLoop_Run2, data.TrialHandler2) and thisTrialLoop_Run2.thisN != TrialLoop_Run2.thisTrial.thisN:
                continueRoutine = False
            Cue0Back.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > Cue0Back.maxDuration-frameTolerance:
                    Cue0Back.maxDurationReached = True
                    continueRoutine = False
                
                # *Cue_Target* updates
                
                # if Cue_Target is starting this frame...
                if Cue_Target.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Cue_Target.frameNStart = frameN  # exact frame index
                    Cue_Target.tStart = t  # local t and not account for scr refresh
                    Cue_Target.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cue_Target, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cue_Target.started')
                    # update status
                    Cue_Target.status = STARTED
                    Cue_Target.setAutoDraw(True)
                
                # if Cue_Target is active this frame...
                if Cue_Target.status == STARTED:
                    # update params
                    pass
                
                # if Cue_Target is stopping this frame...
                if Cue_Target.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Cue_Target.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Cue_Target.tStop = t  # not accounting for scr refresh
                        Cue_Target.tStopRefresh = tThisFlipGlobal  # on global time
                        Cue_Target.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Cue_Target.stopped')
                        # update status
                        Cue_Target.status = FINISHED
                        Cue_Target.setAutoDraw(False)
                
                # *Cue_TargetImage* updates
                
                # if Cue_TargetImage is starting this frame...
                if Cue_TargetImage.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Cue_TargetImage.frameNStart = frameN  # exact frame index
                    Cue_TargetImage.tStart = t  # local t and not account for scr refresh
                    Cue_TargetImage.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cue_TargetImage, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Cue_TargetImage.started')
                    # update status
                    Cue_TargetImage.status = STARTED
                    Cue_TargetImage.setAutoDraw(True)
                
                # if Cue_TargetImage is active this frame...
                if Cue_TargetImage.status == STARTED:
                    # update params
                    pass
                
                # if Cue_TargetImage is stopping this frame...
                if Cue_TargetImage.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Cue_TargetImage.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Cue_TargetImage.tStop = t  # not accounting for scr refresh
                        Cue_TargetImage.tStopRefresh = tThisFlipGlobal  # on global time
                        Cue_TargetImage.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Cue_TargetImage.stopped')
                        # update status
                        Cue_TargetImage.status = FINISHED
                        Cue_TargetImage.setAutoDraw(False)
                
                # *Zero_back* updates
                
                # if Zero_back is starting this frame...
                if Zero_back.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    Zero_back.frameNStart = frameN  # exact frame index
                    Zero_back.tStart = t  # local t and not account for scr refresh
                    Zero_back.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Zero_back, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Zero_back.started')
                    # update status
                    Zero_back.status = STARTED
                    Zero_back.setAutoDraw(True)
                
                # if Zero_back is active this frame...
                if Zero_back.status == STARTED:
                    # update params
                    pass
                
                # if Zero_back is stopping this frame...
                if Zero_back.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Zero_back.tStartRefresh + 2.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Zero_back.tStop = t  # not accounting for scr refresh
                        Zero_back.tStopRefresh = tThisFlipGlobal  # on global time
                        Zero_back.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Zero_back.stopped')
                        # update status
                        Zero_back.status = FINISHED
                        Zero_back.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Cue0Back.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Cue0Back.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Cue0Back" ---
            for thisComponent in Cue0Back.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Cue0Back
            Cue0Back.tStop = globalClock.getTime(format='float')
            Cue0Back.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Cue0Back.stopped', Cue0Back.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Cue0Back.maxDurationReached:
                routineTimer.addTime(-Cue0Back.maxDuration)
            elif Cue0Back.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.500000)
            
            # --- Prepare to start Routine "Stim" ---
            # create an object to store info about Routine Stim
            Stim = data.Routine(
                name='Stim',
                components=[StimulusImage, LeftScreenResponse, RightScreenResponse, response],
            )
            Stim.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from targetLogic
            if CorrectResponse == 'Target':
                correctKey = matchKey
            else:
                correctKey = noMatchKey
            
            StimulusImage.setImage(Stimulus)
            LeftScreenResponse.reset()
            LeftScreenResponse.setText(leftSideOfScreen)
            RightScreenResponse.reset()
            RightScreenResponse.setText(rightSideOfScreen)
            # create starting attributes for response
            response.keys = []
            response.rt = []
            _response_allKeys = []
            # Run 'Begin Routine' code from skip_run_1_logic_10
            # Skip this routine if initial run is 2
            if initialRun == 2:
                continueRoutine = False
            # store start times for Stim
            Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Stim.tStart = globalClock.getTime(format='float')
            Stim.status = STARTED
            thisExp.addData('Stim.started', Stim.tStart)
            Stim.maxDuration = None
            # keep track of which components have finished
            StimComponents = Stim.components
            for thisComponent in Stim.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Stim" ---
            # if trial has changed, end Routine now
            if isinstance(TrialLoop_Run2, data.TrialHandler2) and thisTrialLoop_Run2.thisN != TrialLoop_Run2.thisTrial.thisN:
                continueRoutine = False
            Stim.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *StimulusImage* updates
                
                # if StimulusImage is starting this frame...
                if StimulusImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    StimulusImage.frameNStart = frameN  # exact frame index
                    StimulusImage.tStart = t  # local t and not account for scr refresh
                    StimulusImage.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(StimulusImage, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'StimulusImage.started')
                    # update status
                    StimulusImage.status = STARTED
                    StimulusImage.setAutoDraw(True)
                
                # if StimulusImage is active this frame...
                if StimulusImage.status == STARTED:
                    # update params
                    pass
                
                # if StimulusImage is stopping this frame...
                if StimulusImage.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > StimulusImage.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        StimulusImage.tStop = t  # not accounting for scr refresh
                        StimulusImage.tStopRefresh = tThisFlipGlobal  # on global time
                        StimulusImage.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'StimulusImage.stopped')
                        # update status
                        StimulusImage.status = FINISHED
                        StimulusImage.setAutoDraw(False)
                
                # *LeftScreenResponse* updates
                
                # if LeftScreenResponse is starting this frame...
                if LeftScreenResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    LeftScreenResponse.frameNStart = frameN  # exact frame index
                    LeftScreenResponse.tStart = t  # local t and not account for scr refresh
                    LeftScreenResponse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LeftScreenResponse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'LeftScreenResponse.started')
                    # update status
                    LeftScreenResponse.status = STARTED
                    LeftScreenResponse.setAutoDraw(True)
                
                # if LeftScreenResponse is active this frame...
                if LeftScreenResponse.status == STARTED:
                    # update params
                    pass
                
                # if LeftScreenResponse is stopping this frame...
                if LeftScreenResponse.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > LeftScreenResponse.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        LeftScreenResponse.tStop = t  # not accounting for scr refresh
                        LeftScreenResponse.tStopRefresh = tThisFlipGlobal  # on global time
                        LeftScreenResponse.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'LeftScreenResponse.stopped')
                        # update status
                        LeftScreenResponse.status = FINISHED
                        LeftScreenResponse.setAutoDraw(False)
                
                # *RightScreenResponse* updates
                
                # if RightScreenResponse is starting this frame...
                if RightScreenResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RightScreenResponse.frameNStart = frameN  # exact frame index
                    RightScreenResponse.tStart = t  # local t and not account for scr refresh
                    RightScreenResponse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RightScreenResponse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RightScreenResponse.started')
                    # update status
                    RightScreenResponse.status = STARTED
                    RightScreenResponse.setAutoDraw(True)
                
                # if RightScreenResponse is active this frame...
                if RightScreenResponse.status == STARTED:
                    # update params
                    pass
                
                # if RightScreenResponse is stopping this frame...
                if RightScreenResponse.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > RightScreenResponse.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        RightScreenResponse.tStop = t  # not accounting for scr refresh
                        RightScreenResponse.tStopRefresh = tThisFlipGlobal  # on global time
                        RightScreenResponse.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'RightScreenResponse.stopped')
                        # update status
                        RightScreenResponse.status = FINISHED
                        RightScreenResponse.setAutoDraw(False)
                
                # *response* updates
                waitOnFlip = False
                
                # if response is starting this frame...
                if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    response.frameNStart = frameN  # exact frame index
                    response.tStart = t  # local t and not account for scr refresh
                    response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response.started')
                    # update status
                    response.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if response is stopping this frame...
                if response.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        response.tStop = t  # not accounting for scr refresh
                        response.tStopRefresh = tThisFlipGlobal  # on global time
                        response.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response.stopped')
                        # update status
                        response.status = FINISHED
                        response.status = FINISHED
                if response.status == STARTED and not waitOnFlip:
                    theseKeys = response.getKeys(keyList=['2','3'], ignoreKeys=["escape"], waitRelease=False)
                    _response_allKeys.extend(theseKeys)
                    if len(_response_allKeys):
                        response.keys = _response_allKeys[0].name  # just the first key pressed
                        response.rt = _response_allKeys[0].rt
                        response.duration = _response_allKeys[0].duration
                        # was this correct?
                        if (response.keys == str(correctKey)) or (response.keys == correctKey):
                            response.corr = 1
                        else:
                            response.corr = 0
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Stim.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Stim.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Stim" ---
            for thisComponent in Stim.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Stim
            Stim.tStop = globalClock.getTime(format='float')
            Stim.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Stim.stopped', Stim.tStop)
            # check responses
            if response.keys in ['', [], None]:  # No response was made
                response.keys = None
                # was no response the correct answer?!
                if str(correctKey).lower() == 'none':
                   response.corr = 1;  # correct non-response
                else:
                   response.corr = 0;  # failed to respond (incorrectly)
            # store data for TrialLoop_Run2 (TrialHandler)
            TrialLoop_Run2.addData('response.keys',response.keys)
            TrialLoop_Run2.addData('response.corr', response.corr)
            if response.keys != None:  # we had a response
                TrialLoop_Run2.addData('response.rt', response.rt)
                TrialLoop_Run2.addData('response.duration', response.duration)
            # Run 'End Routine' code from recordDataLogic
            # -------------------------------
            # Collect trial data
            # -------------------------------
            
            from datetime import date
            from datetime import datetime
            # Get current date and time
            current_datetime = datetime.now()
            # Format the time as a string (e.g., "14:30:45")
            formatted_time = current_datetime.strftime("%H:%M:%S")
            
            response_key = response.keys if response.keys is not None else 'NA'
            response_rt  = response.rt if response.keys is not None else 'NA'
            accuracy     = response.corr if response.keys is not None else 'NA'
            
            if BlockType == "0-Back":
                target_stim_value = TargetStimulus
            elif BlockType == "2-Back":
                target_stim_value = 'NA'
            
            trial_data = [
                expInfo["Please select version:"],
                currentRun,
                currentBlock+1,
                ID,
                BlockType,
                StimType,
                Stimulus,
                target_stim_value,
                TargetType,
                response_key,
                response_rt,
                accuracy,
                expInfo["Enter subject\'s handedness:"],
                date.today(),
                formatted_time,
                globalClock.getTime()
            ]
            
            # -------------------------------
            # Append to CSV
            # -------------------------------
            
            with open(filename, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(trial_data)
            
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Stim.maxDurationReached:
                routineTimer.addTime(-Stim.maxDuration)
            elif Stim.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            
            # --- Prepare to start Routine "Fix" ---
            # create an object to store info about Routine Fix
            Fix = data.Routine(
                name='Fix',
                components=[End_Fix],
            )
            Fix.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            End_Fix.reset()
            # Run 'Begin Routine' code from skip_run_1_logic_11
            # Skip this routine if initial run is 2
            if initialRun == 2:
                continueRoutine = False
            # store start times for Fix
            Fix.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Fix.tStart = globalClock.getTime(format='float')
            Fix.status = STARTED
            thisExp.addData('Fix.started', Fix.tStart)
            Fix.maxDuration = None
            # keep track of which components have finished
            FixComponents = Fix.components
            for thisComponent in Fix.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Fix" ---
            # if trial has changed, end Routine now
            if isinstance(TrialLoop_Run2, data.TrialHandler2) and thisTrialLoop_Run2.thisN != TrialLoop_Run2.thisTrial.thisN:
                continueRoutine = False
            Fix.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *End_Fix* updates
                
                # if End_Fix is starting this frame...
                if End_Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    End_Fix.frameNStart = frameN  # exact frame index
                    End_Fix.tStart = t  # local t and not account for scr refresh
                    End_Fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(End_Fix, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'End_Fix.started')
                    # update status
                    End_Fix.status = STARTED
                    End_Fix.setAutoDraw(True)
                
                # if End_Fix is active this frame...
                if End_Fix.status == STARTED:
                    # update params
                    pass
                
                # if End_Fix is stopping this frame...
                if End_Fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > End_Fix.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        End_Fix.tStop = t  # not accounting for scr refresh
                        End_Fix.tStopRefresh = tThisFlipGlobal  # on global time
                        End_Fix.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'End_Fix.stopped')
                        # update status
                        End_Fix.status = FINISHED
                        End_Fix.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Fix.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Fix.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Fix" ---
            for thisComponent in Fix.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Fix
            Fix.tStop = globalClock.getTime(format='float')
            Fix.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Fix.stopped', Fix.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Fix.maxDurationReached:
                routineTimer.addTime(-Fix.maxDuration)
            elif Fix.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'TrialLoop_Run2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "EndBlock_Run2" ---
        # create an object to store info about Routine EndBlock_Run2
        EndBlock_Run2 = data.Routine(
            name='EndBlock_Run2',
            components=[],
        )
        EndBlock_Run2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for EndBlock_Run2
        EndBlock_Run2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        EndBlock_Run2.tStart = globalClock.getTime(format='float')
        EndBlock_Run2.status = STARTED
        thisExp.addData('EndBlock_Run2.started', EndBlock_Run2.tStart)
        EndBlock_Run2.maxDuration = None
        # keep track of which components have finished
        EndBlock_Run2Components = EndBlock_Run2.components
        for thisComponent in EndBlock_Run2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "EndBlock_Run2" ---
        # if trial has changed, end Routine now
        if isinstance(BlockLoop_Run2, data.TrialHandler2) and thisBlockLoop_Run2.thisN != BlockLoop_Run2.thisTrial.thisN:
            continueRoutine = False
        EndBlock_Run2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                EndBlock_Run2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EndBlock_Run2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "EndBlock_Run2" ---
        for thisComponent in EndBlock_Run2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for EndBlock_Run2
        EndBlock_Run2.tStop = globalClock.getTime(format='float')
        EndBlock_Run2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('EndBlock_Run2.stopped', EndBlock_Run2.tStop)
        # Run 'End Routine' code from blockLoopLogic_Run2
        blockIndex2 += 1
        if blockIndex2 >= len(blockFilesRun2):
            BlockLoop_Run2.finished = True
        else:
            # Load current block CSV dynamically
            blockFile2 = os.path.join(run2Folder, blockFilesRun2[blockIndex2])
            # Load data from a CSV file into a list of dictionaries
            csvData2 = data.importConditions(blockFile2)
            # Convert the list of dictionaries to a pandas DataFrame
            df2 = pd.DataFrame(csvData2)
        
        
        # the Routine "EndBlock_Run2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed num_blocks_run2 repeats of 'BlockLoop_Run2'
    
    
    # --- Prepare to start Routine "Goodbye" ---
    # create an object to store info about Routine Goodbye
    Goodbye = data.Routine(
        name='Goodbye',
        components=[Finish, All_Done],
    )
    Goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Finish
    Finish.keys = []
    Finish.rt = []
    _Finish_allKeys = []
    All_Done.reset()
    # store start times for Goodbye
    Goodbye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Goodbye.tStart = globalClock.getTime(format='float')
    Goodbye.status = STARTED
    thisExp.addData('Goodbye.started', Goodbye.tStart)
    Goodbye.maxDuration = None
    # keep track of which components have finished
    GoodbyeComponents = Goodbye.components
    for thisComponent in Goodbye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Goodbye" ---
    Goodbye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Finish* updates
        waitOnFlip = False
        
        # if Finish is starting this frame...
        if Finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Finish.frameNStart = frameN  # exact frame index
            Finish.tStart = t  # local t and not account for scr refresh
            Finish.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Finish, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Finish.started')
            # update status
            Finish.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Finish.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Finish.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Finish.status == STARTED and not waitOnFlip:
            theseKeys = Finish.getKeys(keyList=['2', '3', 'space'], ignoreKeys=["escape"], waitRelease=False)
            _Finish_allKeys.extend(theseKeys)
            if len(_Finish_allKeys):
                Finish.keys = _Finish_allKeys[-1].name  # just the last key pressed
                Finish.rt = _Finish_allKeys[-1].rt
                Finish.duration = _Finish_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *All_Done* updates
        
        # if All_Done is starting this frame...
        if All_Done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            All_Done.frameNStart = frameN  # exact frame index
            All_Done.tStart = t  # local t and not account for scr refresh
            All_Done.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(All_Done, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'All_Done.started')
            # update status
            All_Done.status = STARTED
            All_Done.setAutoDraw(True)
        
        # if All_Done is active this frame...
        if All_Done.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Goodbye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Goodbye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Goodbye" ---
    for thisComponent in Goodbye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Goodbye
    Goodbye.tStop = globalClock.getTime(format='float')
    Goodbye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Goodbye.stopped', Goodbye.tStop)
    # check responses
    if Finish.keys in ['', [], None]:  # No response was made
        Finish.keys = None
    thisExp.addData('Finish.keys',Finish.keys)
    if Finish.keys != None:  # we had a response
        thisExp.addData('Finish.rt', Finish.rt)
        thisExp.addData('Finish.duration', Finish.duration)
    thisExp.nextEntry()
    # the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
