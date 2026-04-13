#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Mon Apr 13 11:36:48 2026
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'EmoNback_Practice'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'Please enter the Subject ID:': 'AANNNAAA',
    'Please enter the Session Number:': ["1","2"],
    'Enter subject\'s handedness:': ["Right", "Left"],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
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
    filename = u'data/%s_%s' % (expInfo['Please enter the Subject ID:'], expInfo['Please enter the Session Number:'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/akashrathi/Documents/EDC_tasks/EmoNback/EmoNback_Practice/EmoNback_Practice_lastrun.py',
        savePickle=True, saveWideText=True,
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
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


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
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='stimpres', color=[0,0,0], colorSpace='rgb',
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
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
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
    if deviceManager.getDevice('NextPage') is None:
        # initialise NextPage
        NextPage = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage',
        )
    if deviceManager.getDevice('NextPage_2') is None:
        # initialise NextPage_2
        NextPage_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_2',
        )
    if deviceManager.getDevice('NextPage_5') is None:
        # initialise NextPage_5
        NextPage_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_5',
        )
    if deviceManager.getDevice('NextPage_6') is None:
        # initialise NextPage_6
        NextPage_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_6',
        )
    if deviceManager.getDevice('NextPage_27') is None:
        # initialise NextPage_27
        NextPage_27 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_27',
        )
    if deviceManager.getDevice('NextPage_30') is None:
        # initialise NextPage_30
        NextPage_30 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_30',
        )
    if deviceManager.getDevice('NextPage_7') is None:
        # initialise NextPage_7
        NextPage_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_7',
        )
    if deviceManager.getDevice('NextPage_31') is None:
        # initialise NextPage_31
        NextPage_31 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_31',
        )
    if deviceManager.getDevice('NextPage_8') is None:
        # initialise NextPage_8
        NextPage_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_8',
        )
    if deviceManager.getDevice('response') is None:
        # initialise response
        response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response',
        )
    if deviceManager.getDevice('NextPage_9') is None:
        # initialise NextPage_9
        NextPage_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_9',
        )
    if deviceManager.getDevice('NextPage_10') is None:
        # initialise NextPage_10
        NextPage_10 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_10',
        )
    if deviceManager.getDevice('NextPage_12') is None:
        # initialise NextPage_12
        NextPage_12 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_12',
        )
    if deviceManager.getDevice('NextPage_13') is None:
        # initialise NextPage_13
        NextPage_13 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_13',
        )
    if deviceManager.getDevice('NextPage_14') is None:
        # initialise NextPage_14
        NextPage_14 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_14',
        )
    if deviceManager.getDevice('NextPage_15') is None:
        # initialise NextPage_15
        NextPage_15 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_15',
        )
    if deviceManager.getDevice('NextPage_16') is None:
        # initialise NextPage_16
        NextPage_16 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_16',
        )
    if deviceManager.getDevice('NextPage_17') is None:
        # initialise NextPage_17
        NextPage_17 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_17',
        )
    if deviceManager.getDevice('NextPage_18') is None:
        # initialise NextPage_18
        NextPage_18 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_18',
        )
    if deviceManager.getDevice('NextPage_19') is None:
        # initialise NextPage_19
        NextPage_19 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_19',
        )
    if deviceManager.getDevice('NextPage_20') is None:
        # initialise NextPage_20
        NextPage_20 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_20',
        )
    if deviceManager.getDevice('NextPage_21') is None:
        # initialise NextPage_21
        NextPage_21 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_21',
        )
    if deviceManager.getDevice('NextPage_22') is None:
        # initialise NextPage_22
        NextPage_22 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_22',
        )
    if deviceManager.getDevice('NextPage_28') is None:
        # initialise NextPage_28
        NextPage_28 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_28',
        )
    if deviceManager.getDevice('NextPage_23') is None:
        # initialise NextPage_23
        NextPage_23 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_23',
        )
    if deviceManager.getDevice('NextPage_24') is None:
        # initialise NextPage_24
        NextPage_24 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_24',
        )
    if deviceManager.getDevice('NextPage_25') is None:
        # initialise NextPage_25
        NextPage_25 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_25',
        )
    if deviceManager.getDevice('NextPage_26') is None:
        # initialise NextPage_26
        NextPage_26 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_26',
        )
    if deviceManager.getDevice('NextPage_29') is None:
        # initialise NextPage_29
        NextPage_29 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='NextPage_29',
        )
    if deviceManager.getDevice('EndProgram') is None:
        # initialise EndProgram
        EndProgram = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='EndProgram',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
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
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
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
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
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
    
    # --- Initialize components for Routine "TitlePage" ---
    NextPage = keyboard.Keyboard(deviceName='NextPage')
    NbackTitle = visual.TextBox2(
         win, text='Welcome to the \nFaces & Places Game!', placeholder='Type here...', font='Arial',
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
    # Run 'Begin Experiment' code from handednessLogic
    # Define response mapping based on handedness
    if expInfo['Enter subject\'s handedness:'].lower() == 'right':
        matchKey = 'left'
        noMatchKey = 'right'
        leftScreenInstruction = "MATCH\nPOINTER"
        rightScreenInstruction = "NO MATCH\nMIDDLE"
    else:
        matchKey = 'right'
        noMatchKey = 'left'
        leftScreenInstruction = "NO MATCH\nMIDDLE"
        rightScreenInstruction = "MATCH\nPOINTER"
        
    # SAFETY: force to strings
    matchKey = str(matchKey)
    noMatchKey = str(noMatchKey)
    
    # --- Initialize components for Routine "Instructions1" ---
    NextPage_2 = keyboard.Keyboard(deviceName='NextPage_2')
    Instructions_1 = visual.TextBox2(
         win, text='In this game, you will see different pictures. \nThese pictures will be...', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.2), draggable=False,      letterHeight=0.04,
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
         name='Instructions_1',
         depth=-1, autoLog=True,
    )
    Label_faces = visual.TextBox2(
         win, text='Faces', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.3, -0.3), draggable=False,      letterHeight=0.04,
         size=(1, 1), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Label_faces',
         depth=-2, autoLog=True,
    )
    Places_label = visual.TextBox2(
         win, text='Places', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.3, -0.3), draggable=False,      letterHeight=0.04,
         size=(1, 1), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Places_label',
         depth=-3, autoLog=True,
    )
    Face_image = visual.ImageStim(
        win=win,
        name='Face_image', 
        image='VM Stimuli/PracticeNC1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, -0.10), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Place_Image = visual.ImageStim(
        win=win,
        name='Place_Image', 
        image='VM Stimuli/Place1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0.3, -0.10), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "Instructions5pt5" ---
    NextPage_5 = keyboard.Keyboard(deviceName='NextPage_5')
    Instructions_5pt5 = visual.TextBox2(
         win, text='There are two parts to the game:\n0-back and 2-back', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
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
         name='Instructions_5pt5',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions6" ---
    NextPage_6 = keyboard.Keyboard(deviceName='NextPage_6')
    Instructions_6 = visual.TextBox2(
         win, text='At the beginning of 0-back, \nyou will see a target picture:', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6',
         depth=-1, autoLog=True,
    )
    Instructions_6_Target = visual.TextBox2(
         win, text='Target          =', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.1, 0), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6_Target',
         depth=-2, autoLog=True,
    )
    TargetImage = visual.ImageStim(
        win=win,
        name='TargetImage', 
        image='VM Stimuli/PracticeNC1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0.2, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "Instructions6pt1" ---
    NextPage_27 = keyboard.Keyboard(deviceName='NextPage_27')
    Instructions_7 = visual.TextBox2(
         win, text='Then, pictures will appear one at a time. \nYou will decide if each picture matches the target. For example, if you see:', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_7',
         depth=-1, autoLog=True,
    )
    TargetImage_2 = visual.ImageStim(
        win=win,
        name='TargetImage_2', 
        image='VM Stimuli/PracticeNC1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Instructions_6_Match_2 = visual.TextBox2(
         win, text='Press with your POINTER finger for \na MATCH every time you see that picture.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6_Match_2',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "routine_1" ---
    NextPage_30 = keyboard.Keyboard(deviceName='NextPage_30')
    Instructions_13 = visual.TextBox2(
         win, text='Then, pictures will appear one at a time. \nYou will decide if each picture matches the target. For example, if you see:', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_13',
         depth=-1, autoLog=True,
    )
    TargetImage_4 = visual.ImageStim(
        win=win,
        name='TargetImage_4', 
        image='VM Stimuli/PracticeNC1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Instructions_6_Match_4 = visual.TextBox2(
         win, text='Press with your POINTER finger for \na MATCH every time you see that picture.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6_Match_4',
         depth=-3, autoLog=True,
    )
    Instructions_6_Match_6 = visual.TextBox2(
         win, text='Please press it now.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6_Match_6',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions14" ---
    NextPage_7 = keyboard.Keyboard(deviceName='NextPage_7')
    Instructions_10 = visual.TextBox2(
         win, text='But if the picture does not match the target:', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_10',
         depth=-1, autoLog=True,
    )
    Instructions_6_Match_3 = visual.TextBox2(
         win, text='Press with your \nMIDDLE finger for a NO MATCH. ', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6_Match_3',
         depth=-2, autoLog=True,
    )
    TargetImage_3 = visual.ImageStim(
        win=win,
        name='TargetImage_3', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "routine" ---
    NextPage_31 = keyboard.Keyboard(deviceName='NextPage_31')
    Instructions_14 = visual.TextBox2(
         win, text='But if the picture does not match the target:', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_14',
         depth=-1, autoLog=True,
    )
    Instructions_6_Match_5 = visual.TextBox2(
         win, text='Press with your \nMIDDLE finger for a NO MATCH.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.25), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6_Match_5',
         depth=-2, autoLog=True,
    )
    TargetImage_5 = visual.ImageStim(
        win=win,
        name='TargetImage_5', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    Instructions_6_Match_7 = visual.TextBox2(
         win, text='Please press it now.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6_Match_7',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions6pt2" ---
    NextPage_8 = keyboard.Keyboard(deviceName='NextPage_8')
    Instructions_6pt2 = visual.TextBox2(
         win, text="Let's practice now!", placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
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
         name='Instructions_6pt2',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial1_Cue" ---
    CueFix_1 = visual.TextBox2(
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
         name='CueFix_1',
         depth=0, autoLog=True,
    )
    CueTarget_1 = visual.TextBox2(
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
         name='CueTarget_1',
         depth=-1, autoLog=True,
    )
    CueTargetImage_1 = visual.ImageStim(
        win=win,
        name='CueTargetImage_1', 
        image='VM Stimuli/PracticeNC1.bmp', mask=None, anchor='center',
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
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Stim" ---
    response = keyboard.Keyboard(deviceName='response')
    Stim = visual.ImageStim(
        win=win,
        name='Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Stim_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Stim_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Feedback" ---
    Fix = visual.TextBox2(
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
         name='Fix',
         depth=0, autoLog=True,
    )
    Feedback = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Feedback',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "InstructionsSpaceToContinue" ---
    NextPage_9 = keyboard.Keyboard(deviceName='NextPage_9')
    Instructions_Space = visual.TextBox2(
         win, text='Press SPACE to continue', placeholder='Type here...', font='Arial',
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
         name='Instructions_Space',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial2_Cue" ---
    CueFix_2 = visual.TextBox2(
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
         name='CueFix_2',
         depth=0, autoLog=True,
    )
    CueTarget_2 = visual.TextBox2(
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
         name='CueTarget_2',
         depth=-1, autoLog=True,
    )
    CueTargetImage_2 = visual.ImageStim(
        win=win,
        name='CueTargetImage_2', 
        image='VM Stimuli/Place1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0.25, 0), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Zero_back_2 = visual.TextBox2(
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
         name='Zero_back_2',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Stim" ---
    response = keyboard.Keyboard(deviceName='response')
    Stim = visual.ImageStim(
        win=win,
        name='Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Stim_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Stim_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Feedback" ---
    Fix = visual.TextBox2(
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
         name='Fix',
         depth=0, autoLog=True,
    )
    Feedback = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Feedback',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "InstructionsSpaceToContinue" ---
    NextPage_9 = keyboard.Keyboard(deviceName='NextPage_9')
    Instructions_Space = visual.TextBox2(
         win, text='Press SPACE to continue', placeholder='Type here...', font='Arial',
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
         name='Instructions_Space',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions8" ---
    NextPage_10 = keyboard.Keyboard(deviceName='NextPage_10')
    Instructions_8 = visual.TextBox2(
         win, text='During the 2-Back, \nyou will see pictures appear one at a time.\n\nYou will decide if each \npicture is the same as the one you saw “2 back.”\n\nPress with your POINTER finger for MATCH.\n\nPress with your MIDDLE finger for NO MATCH.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
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
         name='Instructions_8',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions9" ---
    NextPage_12 = keyboard.Keyboard(deviceName='NextPage_12')
    Instructions_9 = visual.TextBox2(
         win, text='For example, if the first picture you see is:', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.2), draggable=False,      letterHeight=0.04,
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
         name='Instructions_9',
         depth=-1, autoLog=True,
    )
    Example_Stim = visual.ImageStim(
        win=win,
        name='Example_Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Example_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Example_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    Instructions_12 = visual.TextBox2(
         win, text='This is a NO MATCH \nbecause nothing was shown 2 back.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.3), draggable=False,      letterHeight=0.04,
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
         name='Instructions_12',
         depth=-5, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions21" ---
    NextPage_13 = keyboard.Keyboard(deviceName='NextPage_13')
    Instructions_21 = visual.TextBox2(
         win, text='This is also a NO MATCH, \nbecause nothing was shown 2 back.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.2), draggable=False,      letterHeight=0.04,
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
         name='Instructions_21',
         depth=-1, autoLog=True,
    )
    One_Back_Example_Stim = visual.ImageStim(
        win=win,
        name='One_Back_Example_Stim', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.30, 0), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Example_Stim_2 = visual.ImageStim(
        win=win,
        name='Example_Stim_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    Example_LeftScreenInstruction_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_2',
         depth=-4, autoLog=True,
    )
    Example_RightScreenInstruction_2 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_2',
         depth=-5, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions24" ---
    NextPage_14 = keyboard.Keyboard(deviceName='NextPage_14')
    Instructions_24 = visual.TextBox2(
         win, text='This is a MATCH because \nit is the same as the one shown 2 back.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.2), draggable=False,      letterHeight=0.04,
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
         name='Instructions_24',
         depth=-1, autoLog=True,
    )
    Green_Border = visual.Rect(
        win=win, name='Green_Border',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=(-0.50, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='limegreen', fillColor='limegreen',
        opacity=1.0, depth=-2.0, interpolate=True)
    Two_Back_Example_Stim = visual.ImageStim(
        win=win,
        name='Two_Back_Example_Stim', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.50, 0), draggable=False, size=(0.13, 0.13),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    One_Back_Example_Stim_2 = visual.ImageStim(
        win=win,
        name='One_Back_Example_Stim_2', 
        image='VM Stimuli/PracticeFO2.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.30, 0), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Example_Stim_3 = visual.ImageStim(
        win=win,
        name='Example_Stim_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    Example_LeftScreenInstruction_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_3',
         depth=-6, autoLog=True,
    )
    Example_RightScreenInstruction_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_3',
         depth=-7, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions25" ---
    NextPage_15 = keyboard.Keyboard(deviceName='NextPage_15')
    Instructions_25 = visual.TextBox2(
         win, text='This is a NO MATCH because it \nis a different picture than the one shown 2 back.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.2), draggable=False,      letterHeight=0.04,
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
         name='Instructions_25',
         depth=-1, autoLog=True,
    )
    Two_Back_Example_Stim_2 = visual.ImageStim(
        win=win,
        name='Two_Back_Example_Stim_2', 
        image='VM Stimuli/PracticeFO2.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.50, 0), draggable=False, size=(0.13, 0.13),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    One_Back_Example_Stim_3 = visual.ImageStim(
        win=win,
        name='One_Back_Example_Stim_3', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.30, 0), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    Example_Stim_4 = visual.ImageStim(
        win=win,
        name='Example_Stim_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Example_LeftScreenInstruction_4 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_4',
         depth=-5, autoLog=True,
    )
    Example_RightScreenInstruction_4 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_4',
         depth=-6, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions15" ---
    NextPage_16 = keyboard.Keyboard(deviceName='NextPage_16')
    Instructions_15 = visual.TextBox2(
         win, text="Let's try some together!", placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
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
         name='Instructions_15',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions32" ---
    NextPage_17 = keyboard.Keyboard(deviceName='NextPage_17')
    Instructions_32 = visual.TextBox2(
         win, text='MATCH or NO MATCH?', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.27), draggable=False,      letterHeight=0.04,
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
         name='Instructions_32',
         depth=-1, autoLog=True,
    )
    Example_Stim_5 = visual.ImageStim(
        win=win,
        name='Example_Stim_5', 
        image='VM Stimuli/PracticeFO2.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Example_LeftScreenInstruction_5 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_5',
         depth=-3, autoLog=True,
    )
    Example_RightScreenInstruction_5 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_5',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions27" ---
    NextPage_18 = keyboard.Keyboard(deviceName='NextPage_18')
    Instructions_27 = visual.TextBox2(
         win, text='This is a NO MATCH \nbecause nothing was shown 2 back.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.27), draggable=False,      letterHeight=0.04,
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
         name='Instructions_27',
         depth=-1, autoLog=True,
    )
    Example_Stim_6 = visual.ImageStim(
        win=win,
        name='Example_Stim_6', 
        image='VM Stimuli/PracticeFO2.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Example_LeftScreenInstruction_6 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_6',
         depth=-3, autoLog=True,
    )
    Example_RightScreenInstruction_6 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_6',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions33" ---
    NextPage_19 = keyboard.Keyboard(deviceName='NextPage_19')
    Instructions_33 = visual.TextBox2(
         win, text='MATCH or NO MATCH?', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.27), draggable=False,      letterHeight=0.04,
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
         name='Instructions_33',
         depth=-1, autoLog=True,
    )
    Example_Stim_7 = visual.ImageStim(
        win=win,
        name='Example_Stim_7', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Example_LeftScreenInstruction_7 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_7',
         depth=-3, autoLog=True,
    )
    Example_RightScreenInstruction_7 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_7',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions26" ---
    NextPage_20 = keyboard.Keyboard(deviceName='NextPage_20')
    Instructions_26 = visual.TextBox2(
         win, text='This is a NO MATCH \nbecause nothing was shown 2 back.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.27), draggable=False,      letterHeight=0.04,
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
         name='Instructions_26',
         depth=-1, autoLog=True,
    )
    One_Back_Example_Stim_4 = visual.ImageStim(
        win=win,
        name='One_Back_Example_Stim_4', 
        image='VM Stimuli/PracticeFO2.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.30, 0), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Example_Stim_8 = visual.ImageStim(
        win=win,
        name='Example_Stim_8', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    Example_LeftScreenInstruction_8 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_8',
         depth=-4, autoLog=True,
    )
    Example_RightScreenInstruction_8 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_8',
         depth=-5, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions34" ---
    NextPage_21 = keyboard.Keyboard(deviceName='NextPage_21')
    Instructions = visual.TextBox2(
         win, text='MATCH or NO MATCH?', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.27), draggable=False,      letterHeight=0.04,
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
         name='Instructions',
         depth=-1, autoLog=True,
    )
    Example_Stim_9 = visual.ImageStim(
        win=win,
        name='Example_Stim_9', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Example_LeftScreenInstruction_9 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_9',
         depth=-3, autoLog=True,
    )
    Example_RightScreenInstruction_9 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_9',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions28" ---
    NextPage_22 = keyboard.Keyboard(deviceName='NextPage_22')
    Instructions_28 = visual.TextBox2(
         win, text='This is a NO MATCH \nbecause this picture is different \nfrom the one that was shown 2 back.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.27), draggable=False,      letterHeight=0.04,
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
         name='Instructions_28',
         depth=-1, autoLog=True,
    )
    Two_Back_Example_Stim_3 = visual.ImageStim(
        win=win,
        name='Two_Back_Example_Stim_3', 
        image='VM Stimuli/PracticeFO2.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.50, 0), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    One_Back_Example_Stim_5 = visual.ImageStim(
        win=win,
        name='One_Back_Example_Stim_5', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.30, 0), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    Example_Stim_10 = visual.ImageStim(
        win=win,
        name='Example_Stim_10', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Example_LeftScreenInstruction_10 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_10',
         depth=-5, autoLog=True,
    )
    Example_RightScreenInstruction_10 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_10',
         depth=-6, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions_31" ---
    NextPage_28 = keyboard.Keyboard(deviceName='NextPage_28')
    Instructions_4 = visual.TextBox2(
         win, text='MATCH or NO MATCH?', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.27), draggable=False,      letterHeight=0.04,
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
         name='Instructions_4',
         depth=-1, autoLog=True,
    )
    Example_Stim_12 = visual.ImageStim(
        win=win,
        name='Example_Stim_12', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Example_LeftScreenInstruction_12 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_12',
         depth=-3, autoLog=True,
    )
    Example_RightScreenInstruction_12 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_12',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions29" ---
    NextPage_23 = keyboard.Keyboard(deviceName='NextPage_23')
    Instructions_29 = visual.TextBox2(
         win, text='This is a MATCH because it is \nthe same picture as the one shown 2 back.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.27), draggable=False,      letterHeight=0.04,
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
         name='Instructions_29',
         depth=-1, autoLog=True,
    )
    Green_Border_2 = visual.Rect(
        win=win, name='Green_Border_2',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=(-0.50, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='limegreen', fillColor='limegreen',
        opacity=1.0, depth=-2.0, interpolate=True)
    Two_Back_Example_Stim_4 = visual.ImageStim(
        win=win,
        name='Two_Back_Example_Stim_4', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.50, 0), draggable=False, size=(0.13, 0.13),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    One_Back_Example_Stim_6 = visual.ImageStim(
        win=win,
        name='One_Back_Example_Stim_6', 
        image='VM Stimuli/PracticeFO1.bmp', mask=None, anchor='center',
        ori=0.0, pos=(-0.30, 0), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    Example_Stim_11 = visual.ImageStim(
        win=win,
        name='Example_Stim_11', 
        image='VM Stimuli/PracticeFO3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.30, 0.30),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    Example_LeftScreenInstruction_11 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_LeftScreenInstruction_11',
         depth=-6, autoLog=True,
    )
    Example_RightScreenInstruction_11 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.23), draggable=False,      letterHeight=0.03,
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
         name='Example_RightScreenInstruction_11',
         depth=-7, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions22" ---
    NextPage_24 = keyboard.Keyboard(deviceName='NextPage_24')
    Instructions_22 = visual.TextBox2(
         win, text='Reminders: \n\nYou will see pictures one at a time.\n\nDuring the 0-back, look for the Target picture.\n\nDuring the 2-back, look \nfor what was shown 2 pictures back.\n\nPress with your POINTER finger for a MATCH, and press with your MIDDLE finger for a NO MATCH.\n\nAny questions?', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
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
         name='Instructions_22',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions30" ---
    NextPage_25 = keyboard.Keyboard(deviceName='NextPage_25')
    Instructions_30 = visual.TextBox2(
         win, text="Let's practice!", placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
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
         name='Instructions_30',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Stim" ---
    response = keyboard.Keyboard(deviceName='response')
    Stim = visual.ImageStim(
        win=win,
        name='Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Stim_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Stim_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Feedback" ---
    Fix = visual.TextBox2(
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
         name='Fix',
         depth=0, autoLog=True,
    )
    Feedback = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Feedback',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "InstructionsSpaceToContinue" ---
    NextPage_9 = keyboard.Keyboard(deviceName='NextPage_9')
    Instructions_Space = visual.TextBox2(
         win, text='Press SPACE to continue', placeholder='Type here...', font='Arial',
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
         name='Instructions_Space',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Stim" ---
    response = keyboard.Keyboard(deviceName='response')
    Stim = visual.ImageStim(
        win=win,
        name='Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Stim_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Stim_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Feedback" ---
    Fix = visual.TextBox2(
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
         name='Fix',
         depth=0, autoLog=True,
    )
    Feedback = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Feedback',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions36" ---
    NextPage_26 = keyboard.Keyboard(deviceName='NextPage_26')
    Instructions_36 = visual.TextBox2(
         win, text="Now let's practice switching between \nthe 0-back and 2-back parts of the games.  \n\nYou will see a plus sign \nbetween each picture, like this:", placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.2), draggable=False,      letterHeight=0.04,
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
         name='Instructions_36',
         depth=-1, autoLog=True,
    )
    magenta_fixcross = visual.TextBox2(
         win, text='+', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.2,
         size=(0.5, 0.5), borderWidth=2.0,
         color=[1.0000, -1.0000, 1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='magenta_fixcross',
         depth=-2, autoLog=True,
    )
    Instructions_37 = visual.TextBox2(
         win, text='The plus sign will turn purple \nwhen the game is switching between the 0-back \nand the 2-back, so make sure to pay attention!', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -0.2), draggable=False,      letterHeight=0.04,
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
         name='Instructions_37',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instructions_5" ---
    NextPage_29 = keyboard.Keyboard(deviceName='NextPage_29')
    Instructions_38 = visual.TextBox2(
         win, text='Any questions?\n\nGet ready to practice \nplaying the Faces & Places Game.\n\n\nPress the SPACEBAR to begin.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
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
         name='Instructions_38',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial5_Cue" ---
    CueFix_5 = visual.TextBox2(
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
         name='CueFix_5',
         depth=0, autoLog=True,
    )
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
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Stim" ---
    response = keyboard.Keyboard(deviceName='response')
    Stim = visual.ImageStim(
        win=win,
        name='Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Stim_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Stim_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Feedback" ---
    Fix = visual.TextBox2(
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
         name='Fix',
         depth=0, autoLog=True,
    )
    Feedback = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Feedback',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial6_Cue" ---
    CueFix_6 = visual.TextBox2(
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
         name='CueFix_6',
         depth=0, autoLog=True,
    )
    CueTarget_6 = visual.TextBox2(
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
         name='CueTarget_6',
         depth=-1, autoLog=True,
    )
    CueTargetImage_6 = visual.ImageStim(
        win=win,
        name='CueTargetImage_6', 
        image='VM Stimuli/Place3.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0.25, 0), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Zero_back_3 = visual.TextBox2(
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
         name='Zero_back_3',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Stim" ---
    response = keyboard.Keyboard(deviceName='response')
    Stim = visual.ImageStim(
        win=win,
        name='Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Stim_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Stim_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Feedback" ---
    Fix = visual.TextBox2(
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
         name='Fix',
         depth=0, autoLog=True,
    )
    Feedback = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Feedback',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial7_Cue" ---
    CueFix_7 = visual.TextBox2(
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
         name='CueFix_7',
         depth=0, autoLog=True,
    )
    Cue_2Back_2 = visual.TextBox2(
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
         name='Cue_2Back_2',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Stim" ---
    response = keyboard.Keyboard(deviceName='response')
    Stim = visual.ImageStim(
        win=win,
        name='Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Stim_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Stim_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Feedback" ---
    Fix = visual.TextBox2(
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
         name='Fix',
         depth=0, autoLog=True,
    )
    Feedback = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Feedback',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial8_Cue" ---
    CueFix_8 = visual.TextBox2(
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
         name='CueFix_8',
         depth=0, autoLog=True,
    )
    CueTarget_8 = visual.TextBox2(
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
         name='CueTarget_8',
         depth=-1, autoLog=True,
    )
    CueTargetImage_8 = visual.ImageStim(
        win=win,
        name='CueTargetImage_8', 
        image='VM Stimuli/PracticeNC2.bmp', mask=None, anchor='center',
        ori=0.0, pos=(0.25, 0), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Zero_back_4 = visual.TextBox2(
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
         name='Zero_back_4',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Stim" ---
    response = keyboard.Keyboard(deviceName='response')
    Stim = visual.ImageStim(
        win=win,
        name='Stim', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.1), draggable=False, size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    Stim_LeftScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(-0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_LeftScreenInstruction',
         depth=-3, autoLog=True,
    )
    Stim_RightScreenInstruction = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0.2, -0.2), draggable=False,      letterHeight=0.03,
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
         name='Stim_RightScreenInstruction',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "PracticeTrial_Feedback" ---
    Fix = visual.TextBox2(
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
         name='Fix',
         depth=0, autoLog=True,
    )
    Feedback = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.05), draggable=False,      letterHeight=0.05,
         size=(1, 1), borderWidth=0.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=True, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='Feedback',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Goodbye" ---
    EndProgram = keyboard.Keyboard(deviceName='EndProgram')
    AllDone = visual.TextBox2(
         win, text='All Done!\n\n\nPlease tell the experimenter \nyou are finished.\n\n\nPress the SPACEBAR to exit.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.04,
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
         name='AllDone',
         depth=-2, autoLog=True,
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
    
    # --- Prepare to start Routine "TitlePage" ---
    # create an object to store info about Routine TitlePage
    TitlePage = data.Routine(
        name='TitlePage',
        components=[NextPage, NbackTitle],
    )
    TitlePage.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage
    NextPage.keys = []
    NextPage.rt = []
    _NextPage_allKeys = []
    NbackTitle.reset()
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
        
        # *NextPage* updates
        waitOnFlip = False
        
        # if NextPage is starting this frame...
        if NextPage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage.frameNStart = frameN  # exact frame index
            NextPage.tStart = t  # local t and not account for scr refresh
            NextPage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage.started')
            # update status
            NextPage.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage.status == STARTED and not waitOnFlip:
            theseKeys = NextPage.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_allKeys.extend(theseKeys)
            if len(_NextPage_allKeys):
                NextPage.keys = _NextPage_allKeys[-1].name  # just the last key pressed
                NextPage.rt = _NextPage_allKeys[-1].rt
                NextPage.duration = _NextPage_allKeys[-1].duration
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
                timers=[routineTimer, globalClock], 
                currentRoutine=TitlePage,
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
    if NextPage.keys in ['', [], None]:  # No response was made
        NextPage.keys = None
    thisExp.addData('NextPage.keys',NextPage.keys)
    if NextPage.keys != None:  # we had a response
        thisExp.addData('NextPage.rt', NextPage.rt)
        thisExp.addData('NextPage.duration', NextPage.duration)
    thisExp.nextEntry()
    # the Routine "TitlePage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions1" ---
    # create an object to store info about Routine Instructions1
    Instructions1 = data.Routine(
        name='Instructions1',
        components=[NextPage_2, Instructions_1, Label_faces, Places_label, Face_image, Place_Image],
    )
    Instructions1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_2
    NextPage_2.keys = []
    NextPage_2.rt = []
    _NextPage_2_allKeys = []
    Instructions_1.reset()
    Label_faces.reset()
    Places_label.reset()
    # store start times for Instructions1
    Instructions1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions1.tStart = globalClock.getTime(format='float')
    Instructions1.status = STARTED
    thisExp.addData('Instructions1.started', Instructions1.tStart)
    Instructions1.maxDuration = None
    # keep track of which components have finished
    Instructions1Components = Instructions1.components
    for thisComponent in Instructions1.components:
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
    
    # --- Run Routine "Instructions1" ---
    Instructions1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_2* updates
        waitOnFlip = False
        
        # if NextPage_2 is starting this frame...
        if NextPage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_2.frameNStart = frameN  # exact frame index
            NextPage_2.tStart = t  # local t and not account for scr refresh
            NextPage_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_2.started')
            # update status
            NextPage_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_2.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_2_allKeys.extend(theseKeys)
            if len(_NextPage_2_allKeys):
                NextPage_2.keys = _NextPage_2_allKeys[-1].name  # just the last key pressed
                NextPage_2.rt = _NextPage_2_allKeys[-1].rt
                NextPage_2.duration = _NextPage_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_1* updates
        
        # if Instructions_1 is starting this frame...
        if Instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_1.frameNStart = frameN  # exact frame index
            Instructions_1.tStart = t  # local t and not account for scr refresh
            Instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_1.started')
            # update status
            Instructions_1.status = STARTED
            Instructions_1.setAutoDraw(True)
        
        # if Instructions_1 is active this frame...
        if Instructions_1.status == STARTED:
            # update params
            pass
        
        # *Label_faces* updates
        
        # if Label_faces is starting this frame...
        if Label_faces.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Label_faces.frameNStart = frameN  # exact frame index
            Label_faces.tStart = t  # local t and not account for scr refresh
            Label_faces.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Label_faces, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Label_faces.started')
            # update status
            Label_faces.status = STARTED
            Label_faces.setAutoDraw(True)
        
        # if Label_faces is active this frame...
        if Label_faces.status == STARTED:
            # update params
            pass
        
        # *Places_label* updates
        
        # if Places_label is starting this frame...
        if Places_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Places_label.frameNStart = frameN  # exact frame index
            Places_label.tStart = t  # local t and not account for scr refresh
            Places_label.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Places_label, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Places_label.started')
            # update status
            Places_label.status = STARTED
            Places_label.setAutoDraw(True)
        
        # if Places_label is active this frame...
        if Places_label.status == STARTED:
            # update params
            pass
        
        # *Face_image* updates
        
        # if Face_image is starting this frame...
        if Face_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Face_image.frameNStart = frameN  # exact frame index
            Face_image.tStart = t  # local t and not account for scr refresh
            Face_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Face_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Face_image.started')
            # update status
            Face_image.status = STARTED
            Face_image.setAutoDraw(True)
        
        # if Face_image is active this frame...
        if Face_image.status == STARTED:
            # update params
            pass
        
        # *Place_Image* updates
        
        # if Place_Image is starting this frame...
        if Place_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Place_Image.frameNStart = frameN  # exact frame index
            Place_Image.tStart = t  # local t and not account for scr refresh
            Place_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Place_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Place_Image.started')
            # update status
            Place_Image.status = STARTED
            Place_Image.setAutoDraw(True)
        
        # if Place_Image is active this frame...
        if Place_Image.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions1,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions1" ---
    for thisComponent in Instructions1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions1
    Instructions1.tStop = globalClock.getTime(format='float')
    Instructions1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions1.stopped', Instructions1.tStop)
    # check responses
    if NextPage_2.keys in ['', [], None]:  # No response was made
        NextPage_2.keys = None
    thisExp.addData('NextPage_2.keys',NextPage_2.keys)
    if NextPage_2.keys != None:  # we had a response
        thisExp.addData('NextPage_2.rt', NextPage_2.rt)
        thisExp.addData('NextPage_2.duration', NextPage_2.duration)
    thisExp.nextEntry()
    # the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions5pt5" ---
    # create an object to store info about Routine Instructions5pt5
    Instructions5pt5 = data.Routine(
        name='Instructions5pt5',
        components=[NextPage_5, Instructions_5pt5],
    )
    Instructions5pt5.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_5
    NextPage_5.keys = []
    NextPage_5.rt = []
    _NextPage_5_allKeys = []
    Instructions_5pt5.reset()
    # store start times for Instructions5pt5
    Instructions5pt5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions5pt5.tStart = globalClock.getTime(format='float')
    Instructions5pt5.status = STARTED
    thisExp.addData('Instructions5pt5.started', Instructions5pt5.tStart)
    Instructions5pt5.maxDuration = None
    # keep track of which components have finished
    Instructions5pt5Components = Instructions5pt5.components
    for thisComponent in Instructions5pt5.components:
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
    
    # --- Run Routine "Instructions5pt5" ---
    Instructions5pt5.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_5* updates
        waitOnFlip = False
        
        # if NextPage_5 is starting this frame...
        if NextPage_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_5.frameNStart = frameN  # exact frame index
            NextPage_5.tStart = t  # local t and not account for scr refresh
            NextPage_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_5.started')
            # update status
            NextPage_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_5.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_5_allKeys.extend(theseKeys)
            if len(_NextPage_5_allKeys):
                NextPage_5.keys = _NextPage_5_allKeys[-1].name  # just the last key pressed
                NextPage_5.rt = _NextPage_5_allKeys[-1].rt
                NextPage_5.duration = _NextPage_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_5pt5* updates
        
        # if Instructions_5pt5 is starting this frame...
        if Instructions_5pt5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_5pt5.frameNStart = frameN  # exact frame index
            Instructions_5pt5.tStart = t  # local t and not account for scr refresh
            Instructions_5pt5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_5pt5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_5pt5.started')
            # update status
            Instructions_5pt5.status = STARTED
            Instructions_5pt5.setAutoDraw(True)
        
        # if Instructions_5pt5 is active this frame...
        if Instructions_5pt5.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions5pt5,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions5pt5.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions5pt5.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions5pt5" ---
    for thisComponent in Instructions5pt5.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions5pt5
    Instructions5pt5.tStop = globalClock.getTime(format='float')
    Instructions5pt5.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions5pt5.stopped', Instructions5pt5.tStop)
    # check responses
    if NextPage_5.keys in ['', [], None]:  # No response was made
        NextPage_5.keys = None
    thisExp.addData('NextPage_5.keys',NextPage_5.keys)
    if NextPage_5.keys != None:  # we had a response
        thisExp.addData('NextPage_5.rt', NextPage_5.rt)
        thisExp.addData('NextPage_5.duration', NextPage_5.duration)
    thisExp.nextEntry()
    # the Routine "Instructions5pt5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions6" ---
    # create an object to store info about Routine Instructions6
    Instructions6 = data.Routine(
        name='Instructions6',
        components=[NextPage_6, Instructions_6, Instructions_6_Target, TargetImage],
    )
    Instructions6.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_6
    NextPage_6.keys = []
    NextPage_6.rt = []
    _NextPage_6_allKeys = []
    Instructions_6.reset()
    Instructions_6_Target.reset()
    # store start times for Instructions6
    Instructions6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions6.tStart = globalClock.getTime(format='float')
    Instructions6.status = STARTED
    thisExp.addData('Instructions6.started', Instructions6.tStart)
    Instructions6.maxDuration = None
    # keep track of which components have finished
    Instructions6Components = Instructions6.components
    for thisComponent in Instructions6.components:
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
    
    # --- Run Routine "Instructions6" ---
    Instructions6.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_6* updates
        waitOnFlip = False
        
        # if NextPage_6 is starting this frame...
        if NextPage_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_6.frameNStart = frameN  # exact frame index
            NextPage_6.tStart = t  # local t and not account for scr refresh
            NextPage_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_6.started')
            # update status
            NextPage_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_6.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_6_allKeys.extend(theseKeys)
            if len(_NextPage_6_allKeys):
                NextPage_6.keys = _NextPage_6_allKeys[0].name  # just the first key pressed
                NextPage_6.rt = _NextPage_6_allKeys[0].rt
                NextPage_6.duration = _NextPage_6_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_6* updates
        
        # if Instructions_6 is starting this frame...
        if Instructions_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6.frameNStart = frameN  # exact frame index
            Instructions_6.tStart = t  # local t and not account for scr refresh
            Instructions_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6.started')
            # update status
            Instructions_6.status = STARTED
            Instructions_6.setAutoDraw(True)
        
        # if Instructions_6 is active this frame...
        if Instructions_6.status == STARTED:
            # update params
            pass
        
        # *Instructions_6_Target* updates
        
        # if Instructions_6_Target is starting this frame...
        if Instructions_6_Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6_Target.frameNStart = frameN  # exact frame index
            Instructions_6_Target.tStart = t  # local t and not account for scr refresh
            Instructions_6_Target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6_Target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6_Target.started')
            # update status
            Instructions_6_Target.status = STARTED
            Instructions_6_Target.setAutoDraw(True)
        
        # if Instructions_6_Target is active this frame...
        if Instructions_6_Target.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions6,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions6.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions6.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions6" ---
    for thisComponent in Instructions6.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions6
    Instructions6.tStop = globalClock.getTime(format='float')
    Instructions6.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions6.stopped', Instructions6.tStop)
    # check responses
    if NextPage_6.keys in ['', [], None]:  # No response was made
        NextPage_6.keys = None
    thisExp.addData('NextPage_6.keys',NextPage_6.keys)
    if NextPage_6.keys != None:  # we had a response
        thisExp.addData('NextPage_6.rt', NextPage_6.rt)
        thisExp.addData('NextPage_6.duration', NextPage_6.duration)
    thisExp.nextEntry()
    # the Routine "Instructions6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions6pt1" ---
    # create an object to store info about Routine Instructions6pt1
    Instructions6pt1 = data.Routine(
        name='Instructions6pt1',
        components=[NextPage_27, Instructions_7, TargetImage_2, Instructions_6_Match_2],
    )
    Instructions6pt1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_27
    NextPage_27.keys = []
    NextPage_27.rt = []
    _NextPage_27_allKeys = []
    Instructions_7.reset()
    Instructions_6_Match_2.reset()
    # store start times for Instructions6pt1
    Instructions6pt1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions6pt1.tStart = globalClock.getTime(format='float')
    Instructions6pt1.status = STARTED
    thisExp.addData('Instructions6pt1.started', Instructions6pt1.tStart)
    Instructions6pt1.maxDuration = None
    # keep track of which components have finished
    Instructions6pt1Components = Instructions6pt1.components
    for thisComponent in Instructions6pt1.components:
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
    
    # --- Run Routine "Instructions6pt1" ---
    Instructions6pt1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_27* updates
        waitOnFlip = False
        
        # if NextPage_27 is starting this frame...
        if NextPage_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_27.frameNStart = frameN  # exact frame index
            NextPage_27.tStart = t  # local t and not account for scr refresh
            NextPage_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_27.started')
            # update status
            NextPage_27.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_27.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_27.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_27.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_27.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_27_allKeys.extend(theseKeys)
            if len(_NextPage_27_allKeys):
                NextPage_27.keys = _NextPage_27_allKeys[0].name  # just the first key pressed
                NextPage_27.rt = _NextPage_27_allKeys[0].rt
                NextPage_27.duration = _NextPage_27_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_7* updates
        
        # if Instructions_7 is starting this frame...
        if Instructions_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_7.frameNStart = frameN  # exact frame index
            Instructions_7.tStart = t  # local t and not account for scr refresh
            Instructions_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_7.started')
            # update status
            Instructions_7.status = STARTED
            Instructions_7.setAutoDraw(True)
        
        # if Instructions_7 is active this frame...
        if Instructions_7.status == STARTED:
            # update params
            pass
        
        # *TargetImage_2* updates
        
        # if TargetImage_2 is starting this frame...
        if TargetImage_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TargetImage_2.frameNStart = frameN  # exact frame index
            TargetImage_2.tStart = t  # local t and not account for scr refresh
            TargetImage_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargetImage_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TargetImage_2.started')
            # update status
            TargetImage_2.status = STARTED
            TargetImage_2.setAutoDraw(True)
        
        # if TargetImage_2 is active this frame...
        if TargetImage_2.status == STARTED:
            # update params
            pass
        
        # *Instructions_6_Match_2* updates
        
        # if Instructions_6_Match_2 is starting this frame...
        if Instructions_6_Match_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6_Match_2.frameNStart = frameN  # exact frame index
            Instructions_6_Match_2.tStart = t  # local t and not account for scr refresh
            Instructions_6_Match_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6_Match_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6_Match_2.started')
            # update status
            Instructions_6_Match_2.status = STARTED
            Instructions_6_Match_2.setAutoDraw(True)
        
        # if Instructions_6_Match_2 is active this frame...
        if Instructions_6_Match_2.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions6pt1,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions6pt1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions6pt1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions6pt1" ---
    for thisComponent in Instructions6pt1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions6pt1
    Instructions6pt1.tStop = globalClock.getTime(format='float')
    Instructions6pt1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions6pt1.stopped', Instructions6pt1.tStop)
    # check responses
    if NextPage_27.keys in ['', [], None]:  # No response was made
        NextPage_27.keys = None
    thisExp.addData('NextPage_27.keys',NextPage_27.keys)
    if NextPage_27.keys != None:  # we had a response
        thisExp.addData('NextPage_27.rt', NextPage_27.rt)
        thisExp.addData('NextPage_27.duration', NextPage_27.duration)
    thisExp.nextEntry()
    # the Routine "Instructions6pt1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "routine_1" ---
    # create an object to store info about Routine routine_1
    routine_1 = data.Routine(
        name='routine_1',
        components=[NextPage_30, Instructions_13, TargetImage_4, Instructions_6_Match_4, Instructions_6_Match_6],
    )
    routine_1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_30
    NextPage_30.keys = []
    NextPage_30.rt = []
    _NextPage_30_allKeys = []
    Instructions_13.reset()
    Instructions_6_Match_4.reset()
    Instructions_6_Match_6.reset()
    # store start times for routine_1
    routine_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_1.tStart = globalClock.getTime(format='float')
    routine_1.status = STARTED
    thisExp.addData('routine_1.started', routine_1.tStart)
    routine_1.maxDuration = None
    # keep track of which components have finished
    routine_1Components = routine_1.components
    for thisComponent in routine_1.components:
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
    
    # --- Run Routine "routine_1" ---
    routine_1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_30* updates
        waitOnFlip = False
        
        # if NextPage_30 is starting this frame...
        if NextPage_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_30.frameNStart = frameN  # exact frame index
            NextPage_30.tStart = t  # local t and not account for scr refresh
            NextPage_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_30.started')
            # update status
            NextPage_30.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_30.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_30.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_30.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_30.getKeys(keyList=[matchKey], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_30_allKeys.extend(theseKeys)
            if len(_NextPage_30_allKeys):
                NextPage_30.keys = _NextPage_30_allKeys[0].name  # just the first key pressed
                NextPage_30.rt = _NextPage_30_allKeys[0].rt
                NextPage_30.duration = _NextPage_30_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_13* updates
        
        # if Instructions_13 is starting this frame...
        if Instructions_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_13.frameNStart = frameN  # exact frame index
            Instructions_13.tStart = t  # local t and not account for scr refresh
            Instructions_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_13.started')
            # update status
            Instructions_13.status = STARTED
            Instructions_13.setAutoDraw(True)
        
        # if Instructions_13 is active this frame...
        if Instructions_13.status == STARTED:
            # update params
            pass
        
        # *TargetImage_4* updates
        
        # if TargetImage_4 is starting this frame...
        if TargetImage_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TargetImage_4.frameNStart = frameN  # exact frame index
            TargetImage_4.tStart = t  # local t and not account for scr refresh
            TargetImage_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargetImage_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TargetImage_4.started')
            # update status
            TargetImage_4.status = STARTED
            TargetImage_4.setAutoDraw(True)
        
        # if TargetImage_4 is active this frame...
        if TargetImage_4.status == STARTED:
            # update params
            pass
        
        # *Instructions_6_Match_4* updates
        
        # if Instructions_6_Match_4 is starting this frame...
        if Instructions_6_Match_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6_Match_4.frameNStart = frameN  # exact frame index
            Instructions_6_Match_4.tStart = t  # local t and not account for scr refresh
            Instructions_6_Match_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6_Match_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6_Match_4.started')
            # update status
            Instructions_6_Match_4.status = STARTED
            Instructions_6_Match_4.setAutoDraw(True)
        
        # if Instructions_6_Match_4 is active this frame...
        if Instructions_6_Match_4.status == STARTED:
            # update params
            pass
        
        # *Instructions_6_Match_6* updates
        
        # if Instructions_6_Match_6 is starting this frame...
        if Instructions_6_Match_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6_Match_6.frameNStart = frameN  # exact frame index
            Instructions_6_Match_6.tStart = t  # local t and not account for scr refresh
            Instructions_6_Match_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6_Match_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6_Match_6.started')
            # update status
            Instructions_6_Match_6.status = STARTED
            Instructions_6_Match_6.setAutoDraw(True)
        
        # if Instructions_6_Match_6 is active this frame...
        if Instructions_6_Match_6.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=routine_1,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routine_1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_1" ---
    for thisComponent in routine_1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_1
    routine_1.tStop = globalClock.getTime(format='float')
    routine_1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_1.stopped', routine_1.tStop)
    # check responses
    if NextPage_30.keys in ['', [], None]:  # No response was made
        NextPage_30.keys = None
    thisExp.addData('NextPage_30.keys',NextPage_30.keys)
    if NextPage_30.keys != None:  # we had a response
        thisExp.addData('NextPage_30.rt', NextPage_30.rt)
        thisExp.addData('NextPage_30.duration', NextPage_30.duration)
    thisExp.nextEntry()
    # the Routine "routine_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions14" ---
    # create an object to store info about Routine Instructions14
    Instructions14 = data.Routine(
        name='Instructions14',
        components=[NextPage_7, Instructions_10, Instructions_6_Match_3, TargetImage_3],
    )
    Instructions14.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_7
    NextPage_7.keys = []
    NextPage_7.rt = []
    _NextPage_7_allKeys = []
    Instructions_10.reset()
    Instructions_6_Match_3.reset()
    # store start times for Instructions14
    Instructions14.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions14.tStart = globalClock.getTime(format='float')
    Instructions14.status = STARTED
    thisExp.addData('Instructions14.started', Instructions14.tStart)
    Instructions14.maxDuration = None
    # keep track of which components have finished
    Instructions14Components = Instructions14.components
    for thisComponent in Instructions14.components:
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
    
    # --- Run Routine "Instructions14" ---
    Instructions14.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_7* updates
        waitOnFlip = False
        
        # if NextPage_7 is starting this frame...
        if NextPage_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_7.frameNStart = frameN  # exact frame index
            NextPage_7.tStart = t  # local t and not account for scr refresh
            NextPage_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_7.started')
            # update status
            NextPage_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_7.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_7_allKeys.extend(theseKeys)
            if len(_NextPage_7_allKeys):
                NextPage_7.keys = _NextPage_7_allKeys[-1].name  # just the last key pressed
                NextPage_7.rt = _NextPage_7_allKeys[-1].rt
                NextPage_7.duration = _NextPage_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_10* updates
        
        # if Instructions_10 is starting this frame...
        if Instructions_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_10.frameNStart = frameN  # exact frame index
            Instructions_10.tStart = t  # local t and not account for scr refresh
            Instructions_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_10.started')
            # update status
            Instructions_10.status = STARTED
            Instructions_10.setAutoDraw(True)
        
        # if Instructions_10 is active this frame...
        if Instructions_10.status == STARTED:
            # update params
            pass
        
        # *Instructions_6_Match_3* updates
        
        # if Instructions_6_Match_3 is starting this frame...
        if Instructions_6_Match_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6_Match_3.frameNStart = frameN  # exact frame index
            Instructions_6_Match_3.tStart = t  # local t and not account for scr refresh
            Instructions_6_Match_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6_Match_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6_Match_3.started')
            # update status
            Instructions_6_Match_3.status = STARTED
            Instructions_6_Match_3.setAutoDraw(True)
        
        # if Instructions_6_Match_3 is active this frame...
        if Instructions_6_Match_3.status == STARTED:
            # update params
            pass
        
        # *TargetImage_3* updates
        
        # if TargetImage_3 is starting this frame...
        if TargetImage_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TargetImage_3.frameNStart = frameN  # exact frame index
            TargetImage_3.tStart = t  # local t and not account for scr refresh
            TargetImage_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargetImage_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TargetImage_3.started')
            # update status
            TargetImage_3.status = STARTED
            TargetImage_3.setAutoDraw(True)
        
        # if TargetImage_3 is active this frame...
        if TargetImage_3.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions14,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions14.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions14.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions14" ---
    for thisComponent in Instructions14.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions14
    Instructions14.tStop = globalClock.getTime(format='float')
    Instructions14.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions14.stopped', Instructions14.tStop)
    # check responses
    if NextPage_7.keys in ['', [], None]:  # No response was made
        NextPage_7.keys = None
    thisExp.addData('NextPage_7.keys',NextPage_7.keys)
    if NextPage_7.keys != None:  # we had a response
        thisExp.addData('NextPage_7.rt', NextPage_7.rt)
        thisExp.addData('NextPage_7.duration', NextPage_7.duration)
    thisExp.nextEntry()
    # the Routine "Instructions14" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "routine" ---
    # create an object to store info about Routine routine
    routine = data.Routine(
        name='routine',
        components=[NextPage_31, Instructions_14, Instructions_6_Match_5, TargetImage_5, Instructions_6_Match_7],
    )
    routine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_31
    NextPage_31.keys = []
    NextPage_31.rt = []
    _NextPage_31_allKeys = []
    Instructions_14.reset()
    Instructions_6_Match_5.reset()
    Instructions_6_Match_7.reset()
    # store start times for routine
    routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine.tStart = globalClock.getTime(format='float')
    routine.status = STARTED
    thisExp.addData('routine.started', routine.tStart)
    routine.maxDuration = None
    # keep track of which components have finished
    routineComponents = routine.components
    for thisComponent in routine.components:
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
    
    # --- Run Routine "routine" ---
    routine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_31* updates
        waitOnFlip = False
        
        # if NextPage_31 is starting this frame...
        if NextPage_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_31.frameNStart = frameN  # exact frame index
            NextPage_31.tStart = t  # local t and not account for scr refresh
            NextPage_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_31, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_31.started')
            # update status
            NextPage_31.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_31.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_31.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_31.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_31.getKeys(keyList=[noMatchKey], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_31_allKeys.extend(theseKeys)
            if len(_NextPage_31_allKeys):
                NextPage_31.keys = _NextPage_31_allKeys[-1].name  # just the last key pressed
                NextPage_31.rt = _NextPage_31_allKeys[-1].rt
                NextPage_31.duration = _NextPage_31_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_14* updates
        
        # if Instructions_14 is starting this frame...
        if Instructions_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_14.frameNStart = frameN  # exact frame index
            Instructions_14.tStart = t  # local t and not account for scr refresh
            Instructions_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_14.started')
            # update status
            Instructions_14.status = STARTED
            Instructions_14.setAutoDraw(True)
        
        # if Instructions_14 is active this frame...
        if Instructions_14.status == STARTED:
            # update params
            pass
        
        # *Instructions_6_Match_5* updates
        
        # if Instructions_6_Match_5 is starting this frame...
        if Instructions_6_Match_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6_Match_5.frameNStart = frameN  # exact frame index
            Instructions_6_Match_5.tStart = t  # local t and not account for scr refresh
            Instructions_6_Match_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6_Match_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6_Match_5.started')
            # update status
            Instructions_6_Match_5.status = STARTED
            Instructions_6_Match_5.setAutoDraw(True)
        
        # if Instructions_6_Match_5 is active this frame...
        if Instructions_6_Match_5.status == STARTED:
            # update params
            pass
        
        # *TargetImage_5* updates
        
        # if TargetImage_5 is starting this frame...
        if TargetImage_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TargetImage_5.frameNStart = frameN  # exact frame index
            TargetImage_5.tStart = t  # local t and not account for scr refresh
            TargetImage_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargetImage_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'TargetImage_5.started')
            # update status
            TargetImage_5.status = STARTED
            TargetImage_5.setAutoDraw(True)
        
        # if TargetImage_5 is active this frame...
        if TargetImage_5.status == STARTED:
            # update params
            pass
        
        # *Instructions_6_Match_7* updates
        
        # if Instructions_6_Match_7 is starting this frame...
        if Instructions_6_Match_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6_Match_7.frameNStart = frameN  # exact frame index
            Instructions_6_Match_7.tStart = t  # local t and not account for scr refresh
            Instructions_6_Match_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6_Match_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6_Match_7.started')
            # update status
            Instructions_6_Match_7.status = STARTED
            Instructions_6_Match_7.setAutoDraw(True)
        
        # if Instructions_6_Match_7 is active this frame...
        if Instructions_6_Match_7.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=routine,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routine.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine" ---
    for thisComponent in routine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine
    routine.tStop = globalClock.getTime(format='float')
    routine.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine.stopped', routine.tStop)
    # check responses
    if NextPage_31.keys in ['', [], None]:  # No response was made
        NextPage_31.keys = None
    thisExp.addData('NextPage_31.keys',NextPage_31.keys)
    if NextPage_31.keys != None:  # we had a response
        thisExp.addData('NextPage_31.rt', NextPage_31.rt)
        thisExp.addData('NextPage_31.duration', NextPage_31.duration)
    thisExp.nextEntry()
    # the Routine "routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions6pt2" ---
    # create an object to store info about Routine Instructions6pt2
    Instructions6pt2 = data.Routine(
        name='Instructions6pt2',
        components=[NextPage_8, Instructions_6pt2],
    )
    Instructions6pt2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_8
    NextPage_8.keys = []
    NextPage_8.rt = []
    _NextPage_8_allKeys = []
    Instructions_6pt2.reset()
    # store start times for Instructions6pt2
    Instructions6pt2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions6pt2.tStart = globalClock.getTime(format='float')
    Instructions6pt2.status = STARTED
    thisExp.addData('Instructions6pt2.started', Instructions6pt2.tStart)
    Instructions6pt2.maxDuration = None
    # keep track of which components have finished
    Instructions6pt2Components = Instructions6pt2.components
    for thisComponent in Instructions6pt2.components:
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
    
    # --- Run Routine "Instructions6pt2" ---
    Instructions6pt2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_8* updates
        waitOnFlip = False
        
        # if NextPage_8 is starting this frame...
        if NextPage_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_8.frameNStart = frameN  # exact frame index
            NextPage_8.tStart = t  # local t and not account for scr refresh
            NextPage_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_8.started')
            # update status
            NextPage_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_8.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_8_allKeys.extend(theseKeys)
            if len(_NextPage_8_allKeys):
                NextPage_8.keys = _NextPage_8_allKeys[-1].name  # just the last key pressed
                NextPage_8.rt = _NextPage_8_allKeys[-1].rt
                NextPage_8.duration = _NextPage_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_6pt2* updates
        
        # if Instructions_6pt2 is starting this frame...
        if Instructions_6pt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_6pt2.frameNStart = frameN  # exact frame index
            Instructions_6pt2.tStart = t  # local t and not account for scr refresh
            Instructions_6pt2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_6pt2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_6pt2.started')
            # update status
            Instructions_6pt2.status = STARTED
            Instructions_6pt2.setAutoDraw(True)
        
        # if Instructions_6pt2 is active this frame...
        if Instructions_6pt2.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions6pt2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions6pt2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions6pt2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions6pt2" ---
    for thisComponent in Instructions6pt2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions6pt2
    Instructions6pt2.tStop = globalClock.getTime(format='float')
    Instructions6pt2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions6pt2.stopped', Instructions6pt2.tStop)
    # check responses
    if NextPage_8.keys in ['', [], None]:  # No response was made
        NextPage_8.keys = None
    thisExp.addData('NextPage_8.keys',NextPage_8.keys)
    if NextPage_8.keys != None:  # we had a response
        thisExp.addData('NextPage_8.rt', NextPage_8.rt)
        thisExp.addData('NextPage_8.duration', NextPage_8.duration)
    thisExp.nextEntry()
    # the Routine "Instructions6pt2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "PracticeTrial1_Cue" ---
    # create an object to store info about Routine PracticeTrial1_Cue
    PracticeTrial1_Cue = data.Routine(
        name='PracticeTrial1_Cue',
        components=[CueFix_1, CueTarget_1, CueTargetImage_1, Zero_back],
    )
    PracticeTrial1_Cue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    CueFix_1.reset()
    CueTarget_1.reset()
    Zero_back.reset()
    # store start times for PracticeTrial1_Cue
    PracticeTrial1_Cue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PracticeTrial1_Cue.tStart = globalClock.getTime(format='float')
    PracticeTrial1_Cue.status = STARTED
    thisExp.addData('PracticeTrial1_Cue.started', PracticeTrial1_Cue.tStart)
    PracticeTrial1_Cue.maxDuration = None
    # keep track of which components have finished
    PracticeTrial1_CueComponents = PracticeTrial1_Cue.components
    for thisComponent in PracticeTrial1_Cue.components:
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
    
    # --- Run Routine "PracticeTrial1_Cue" ---
    PracticeTrial1_Cue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CueFix_1* updates
        
        # if CueFix_1 is starting this frame...
        if CueFix_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CueFix_1.frameNStart = frameN  # exact frame index
            CueFix_1.tStart = t  # local t and not account for scr refresh
            CueFix_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueFix_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueFix_1.started')
            # update status
            CueFix_1.status = STARTED
            CueFix_1.setAutoDraw(True)
        
        # if CueFix_1 is active this frame...
        if CueFix_1.status == STARTED:
            # update params
            pass
        
        # if CueFix_1 is stopping this frame...
        if CueFix_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueFix_1.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                CueFix_1.tStop = t  # not accounting for scr refresh
                CueFix_1.tStopRefresh = tThisFlipGlobal  # on global time
                CueFix_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueFix_1.stopped')
                # update status
                CueFix_1.status = FINISHED
                CueFix_1.setAutoDraw(False)
        
        # *CueTarget_1* updates
        
        # if CueTarget_1 is starting this frame...
        if CueTarget_1.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            CueTarget_1.frameNStart = frameN  # exact frame index
            CueTarget_1.tStart = t  # local t and not account for scr refresh
            CueTarget_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueTarget_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueTarget_1.started')
            # update status
            CueTarget_1.status = STARTED
            CueTarget_1.setAutoDraw(True)
        
        # if CueTarget_1 is active this frame...
        if CueTarget_1.status == STARTED:
            # update params
            pass
        
        # if CueTarget_1 is stopping this frame...
        if CueTarget_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueTarget_1.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                CueTarget_1.tStop = t  # not accounting for scr refresh
                CueTarget_1.tStopRefresh = tThisFlipGlobal  # on global time
                CueTarget_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueTarget_1.stopped')
                # update status
                CueTarget_1.status = FINISHED
                CueTarget_1.setAutoDraw(False)
        
        # *CueTargetImage_1* updates
        
        # if CueTargetImage_1 is starting this frame...
        if CueTargetImage_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            CueTargetImage_1.frameNStart = frameN  # exact frame index
            CueTargetImage_1.tStart = t  # local t and not account for scr refresh
            CueTargetImage_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueTargetImage_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueTargetImage_1.started')
            # update status
            CueTargetImage_1.status = STARTED
            CueTargetImage_1.setAutoDraw(True)
        
        # if CueTargetImage_1 is active this frame...
        if CueTargetImage_1.status == STARTED:
            # update params
            pass
        
        # if CueTargetImage_1 is stopping this frame...
        if CueTargetImage_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueTargetImage_1.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                CueTargetImage_1.tStop = t  # not accounting for scr refresh
                CueTargetImage_1.tStopRefresh = tThisFlipGlobal  # on global time
                CueTargetImage_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueTargetImage_1.stopped')
                # update status
                CueTargetImage_1.status = FINISHED
                CueTargetImage_1.setAutoDraw(False)
        
        # *Zero_back* updates
        
        # if Zero_back is starting this frame...
        if Zero_back.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=PracticeTrial1_Cue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PracticeTrial1_Cue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrial1_Cue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PracticeTrial1_Cue" ---
    for thisComponent in PracticeTrial1_Cue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PracticeTrial1_Cue
    PracticeTrial1_Cue.tStop = globalClock.getTime(format='float')
    PracticeTrial1_Cue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PracticeTrial1_Cue.stopped', PracticeTrial1_Cue.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if PracticeTrial1_Cue.maxDurationReached:
        routineTimer.addTime(-PracticeTrial1_Cue.maxDuration)
    elif PracticeTrial1_Cue.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop = data.TrialHandler2(
        name='practiceLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('PracticeTrials/PracticeTrials1.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practiceLoop)  # add the loop to the experiment
    thisPracticeLoop = practiceLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            globals()[paramName] = thisPracticeLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeLoop in practiceLoop:
        practiceLoop.status = STARTED
        if hasattr(thisPracticeLoop, 'status'):
            thisPracticeLoop.status = STARTED
        currentLoop = practiceLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
        if thisPracticeLoop != None:
            for paramName in thisPracticeLoop:
                globals()[paramName] = thisPracticeLoop[paramName]
        
        # --- Prepare to start Routine "PracticeTrial_Stim" ---
        # create an object to store info about Routine PracticeTrial_Stim
        PracticeTrial_Stim = data.Routine(
            name='PracticeTrial_Stim',
            components=[response, Stim, Stim_LeftScreenInstruction, Stim_RightScreenInstruction],
        )
        PracticeTrial_Stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from targetLogic
        # Decide correct key for this trial
        if TargetType == 'target':
            correctKey = matchKey
        else:
            correctKey = noMatchKey
        
        # create starting attributes for response
        response.keys = []
        response.rt = []
        _response_allKeys = []
        Stim.setImage(Stimulus)
        Stim_LeftScreenInstruction.reset()
        Stim_LeftScreenInstruction.setText(leftScreenInstruction)
        Stim_RightScreenInstruction.reset()
        Stim_RightScreenInstruction.setText(rightScreenInstruction)
        # store start times for PracticeTrial_Stim
        PracticeTrial_Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Stim.tStart = globalClock.getTime(format='float')
        PracticeTrial_Stim.status = STARTED
        thisExp.addData('PracticeTrial_Stim.started', PracticeTrial_Stim.tStart)
        PracticeTrial_Stim.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_StimComponents = PracticeTrial_Stim.components
        for thisComponent in PracticeTrial_Stim.components:
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
        
        # --- Run Routine "PracticeTrial_Stim" ---
        PracticeTrial_Stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop, 'status') and thisPracticeLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = response.getKeys(keyList=[matchKey, noMatchKey], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # *Stim_LeftScreenInstruction* updates
            
            # if Stim_LeftScreenInstruction is starting this frame...
            if Stim_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_LeftScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.started')
                # update status
                Stim_LeftScreenInstruction.status = STARTED
                Stim_LeftScreenInstruction.setAutoDraw(True)
            
            # if Stim_LeftScreenInstruction is active this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_LeftScreenInstruction is stopping this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_LeftScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_LeftScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_LeftScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_LeftScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.stopped')
                    # update status
                    Stim_LeftScreenInstruction.status = FINISHED
                    Stim_LeftScreenInstruction.setAutoDraw(False)
            
            # *Stim_RightScreenInstruction* updates
            
            # if Stim_RightScreenInstruction is starting this frame...
            if Stim_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_RightScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.started')
                # update status
                Stim_RightScreenInstruction.status = STARTED
                Stim_RightScreenInstruction.setAutoDraw(True)
            
            # if Stim_RightScreenInstruction is active this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_RightScreenInstruction is stopping this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_RightScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_RightScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_RightScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_RightScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.stopped')
                    # update status
                    Stim_RightScreenInstruction.status = FINISHED
                    Stim_RightScreenInstruction.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Stim" ---
        for thisComponent in PracticeTrial_Stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Stim
        PracticeTrial_Stim.tStop = globalClock.getTime(format='float')
        PracticeTrial_Stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Stim.stopped', PracticeTrial_Stim.tStop)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceLoop (TrialHandler)
        practiceLoop.addData('response.keys',response.keys)
        practiceLoop.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceLoop.addData('response.rt', response.rt)
            practiceLoop.addData('response.duration', response.duration)
        # Run 'End Routine' code from feedbackLogic
        if response.keys is None:
            fbText = "No response."
            fbColor = 'yellow'
        elif response.corr:
            fbText = "Correct!"
            fbColor = 'limegreen'
        else:
            fbText = "Incorrect"
            fbColor = 'red'
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Stim.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Stim.maxDuration)
        elif PracticeTrial_Stim.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "PracticeTrial_Feedback" ---
        # create an object to store info about Routine PracticeTrial_Feedback
        PracticeTrial_Feedback = data.Routine(
            name='PracticeTrial_Feedback',
            components=[Fix, Feedback],
        )
        PracticeTrial_Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Fix.reset()
        Feedback.reset()
        Feedback.setColor(fbColor, colorSpace='rgb')
        Feedback.setText(fbText)
        # store start times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Feedback.tStart = globalClock.getTime(format='float')
        PracticeTrial_Feedback.status = STARTED
        thisExp.addData('PracticeTrial_Feedback.started', PracticeTrial_Feedback.tStart)
        PracticeTrial_Feedback.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_FeedbackComponents = PracticeTrial_Feedback.components
        for thisComponent in PracticeTrial_Feedback.components:
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
        
        # --- Run Routine "PracticeTrial_Feedback" ---
        PracticeTrial_Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop, 'status') and thisPracticeLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # *Feedback* updates
            
            # if Feedback is starting this frame...
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                # update status
                Feedback.status = STARTED
                Feedback.setAutoDraw(True)
            
            # if Feedback is active this frame...
            if Feedback.status == STARTED:
                # update params
                pass
            
            # if Feedback is stopping this frame...
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    # update status
                    Feedback.status = FINISHED
                    Feedback.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Feedback" ---
        for thisComponent in PracticeTrial_Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStop = globalClock.getTime(format='float')
        PracticeTrial_Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Feedback.stopped', PracticeTrial_Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Feedback.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Feedback.maxDuration)
        elif PracticeTrial_Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeLoop as finished
        if hasattr(thisPracticeLoop, 'status'):
            thisPracticeLoop.status = FINISHED
        # if awaiting a pause, pause now
        if practiceLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceLoop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practiceLoop'
    practiceLoop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "InstructionsSpaceToContinue" ---
    # create an object to store info about Routine InstructionsSpaceToContinue
    InstructionsSpaceToContinue = data.Routine(
        name='InstructionsSpaceToContinue',
        components=[NextPage_9, Instructions_Space],
    )
    InstructionsSpaceToContinue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_9
    NextPage_9.keys = []
    NextPage_9.rt = []
    _NextPage_9_allKeys = []
    Instructions_Space.reset()
    # store start times for InstructionsSpaceToContinue
    InstructionsSpaceToContinue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    InstructionsSpaceToContinue.tStart = globalClock.getTime(format='float')
    InstructionsSpaceToContinue.status = STARTED
    thisExp.addData('InstructionsSpaceToContinue.started', InstructionsSpaceToContinue.tStart)
    InstructionsSpaceToContinue.maxDuration = None
    # keep track of which components have finished
    InstructionsSpaceToContinueComponents = InstructionsSpaceToContinue.components
    for thisComponent in InstructionsSpaceToContinue.components:
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
    
    # --- Run Routine "InstructionsSpaceToContinue" ---
    InstructionsSpaceToContinue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_9* updates
        waitOnFlip = False
        
        # if NextPage_9 is starting this frame...
        if NextPage_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_9.frameNStart = frameN  # exact frame index
            NextPage_9.tStart = t  # local t and not account for scr refresh
            NextPage_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_9.started')
            # update status
            NextPage_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_9.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_9_allKeys.extend(theseKeys)
            if len(_NextPage_9_allKeys):
                NextPage_9.keys = _NextPage_9_allKeys[-1].name  # just the last key pressed
                NextPage_9.rt = _NextPage_9_allKeys[-1].rt
                NextPage_9.duration = _NextPage_9_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_Space* updates
        
        # if Instructions_Space is starting this frame...
        if Instructions_Space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Space.frameNStart = frameN  # exact frame index
            Instructions_Space.tStart = t  # local t and not account for scr refresh
            Instructions_Space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Space, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Space.started')
            # update status
            Instructions_Space.status = STARTED
            Instructions_Space.setAutoDraw(True)
        
        # if Instructions_Space is active this frame...
        if Instructions_Space.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=InstructionsSpaceToContinue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            InstructionsSpaceToContinue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsSpaceToContinue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionsSpaceToContinue" ---
    for thisComponent in InstructionsSpaceToContinue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for InstructionsSpaceToContinue
    InstructionsSpaceToContinue.tStop = globalClock.getTime(format='float')
    InstructionsSpaceToContinue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('InstructionsSpaceToContinue.stopped', InstructionsSpaceToContinue.tStop)
    # check responses
    if NextPage_9.keys in ['', [], None]:  # No response was made
        NextPage_9.keys = None
    thisExp.addData('NextPage_9.keys',NextPage_9.keys)
    if NextPage_9.keys != None:  # we had a response
        thisExp.addData('NextPage_9.rt', NextPage_9.rt)
        thisExp.addData('NextPage_9.duration', NextPage_9.duration)
    thisExp.nextEntry()
    # the Routine "InstructionsSpaceToContinue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "PracticeTrial2_Cue" ---
    # create an object to store info about Routine PracticeTrial2_Cue
    PracticeTrial2_Cue = data.Routine(
        name='PracticeTrial2_Cue',
        components=[CueFix_2, CueTarget_2, CueTargetImage_2, Zero_back_2],
    )
    PracticeTrial2_Cue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    CueFix_2.reset()
    CueTarget_2.reset()
    Zero_back_2.reset()
    # store start times for PracticeTrial2_Cue
    PracticeTrial2_Cue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PracticeTrial2_Cue.tStart = globalClock.getTime(format='float')
    PracticeTrial2_Cue.status = STARTED
    thisExp.addData('PracticeTrial2_Cue.started', PracticeTrial2_Cue.tStart)
    PracticeTrial2_Cue.maxDuration = None
    # keep track of which components have finished
    PracticeTrial2_CueComponents = PracticeTrial2_Cue.components
    for thisComponent in PracticeTrial2_Cue.components:
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
    
    # --- Run Routine "PracticeTrial2_Cue" ---
    PracticeTrial2_Cue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CueFix_2* updates
        
        # if CueFix_2 is starting this frame...
        if CueFix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CueFix_2.frameNStart = frameN  # exact frame index
            CueFix_2.tStart = t  # local t and not account for scr refresh
            CueFix_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueFix_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueFix_2.started')
            # update status
            CueFix_2.status = STARTED
            CueFix_2.setAutoDraw(True)
        
        # if CueFix_2 is active this frame...
        if CueFix_2.status == STARTED:
            # update params
            pass
        
        # if CueFix_2 is stopping this frame...
        if CueFix_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueFix_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                CueFix_2.tStop = t  # not accounting for scr refresh
                CueFix_2.tStopRefresh = tThisFlipGlobal  # on global time
                CueFix_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueFix_2.stopped')
                # update status
                CueFix_2.status = FINISHED
                CueFix_2.setAutoDraw(False)
        
        # *CueTarget_2* updates
        
        # if CueTarget_2 is starting this frame...
        if CueTarget_2.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            CueTarget_2.frameNStart = frameN  # exact frame index
            CueTarget_2.tStart = t  # local t and not account for scr refresh
            CueTarget_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueTarget_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueTarget_2.started')
            # update status
            CueTarget_2.status = STARTED
            CueTarget_2.setAutoDraw(True)
        
        # if CueTarget_2 is active this frame...
        if CueTarget_2.status == STARTED:
            # update params
            pass
        
        # if CueTarget_2 is stopping this frame...
        if CueTarget_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueTarget_2.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                CueTarget_2.tStop = t  # not accounting for scr refresh
                CueTarget_2.tStopRefresh = tThisFlipGlobal  # on global time
                CueTarget_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueTarget_2.stopped')
                # update status
                CueTarget_2.status = FINISHED
                CueTarget_2.setAutoDraw(False)
        
        # *CueTargetImage_2* updates
        
        # if CueTargetImage_2 is starting this frame...
        if CueTargetImage_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            CueTargetImage_2.frameNStart = frameN  # exact frame index
            CueTargetImage_2.tStart = t  # local t and not account for scr refresh
            CueTargetImage_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueTargetImage_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueTargetImage_2.started')
            # update status
            CueTargetImage_2.status = STARTED
            CueTargetImage_2.setAutoDraw(True)
        
        # if CueTargetImage_2 is active this frame...
        if CueTargetImage_2.status == STARTED:
            # update params
            pass
        
        # if CueTargetImage_2 is stopping this frame...
        if CueTargetImage_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueTargetImage_2.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                CueTargetImage_2.tStop = t  # not accounting for scr refresh
                CueTargetImage_2.tStopRefresh = tThisFlipGlobal  # on global time
                CueTargetImage_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueTargetImage_2.stopped')
                # update status
                CueTargetImage_2.status = FINISHED
                CueTargetImage_2.setAutoDraw(False)
        
        # *Zero_back_2* updates
        
        # if Zero_back_2 is starting this frame...
        if Zero_back_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Zero_back_2.frameNStart = frameN  # exact frame index
            Zero_back_2.tStart = t  # local t and not account for scr refresh
            Zero_back_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Zero_back_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Zero_back_2.started')
            # update status
            Zero_back_2.status = STARTED
            Zero_back_2.setAutoDraw(True)
        
        # if Zero_back_2 is active this frame...
        if Zero_back_2.status == STARTED:
            # update params
            pass
        
        # if Zero_back_2 is stopping this frame...
        if Zero_back_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Zero_back_2.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Zero_back_2.tStop = t  # not accounting for scr refresh
                Zero_back_2.tStopRefresh = tThisFlipGlobal  # on global time
                Zero_back_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Zero_back_2.stopped')
                # update status
                Zero_back_2.status = FINISHED
                Zero_back_2.setAutoDraw(False)
        
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
                timers=[routineTimer, globalClock], 
                currentRoutine=PracticeTrial2_Cue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PracticeTrial2_Cue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrial2_Cue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PracticeTrial2_Cue" ---
    for thisComponent in PracticeTrial2_Cue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PracticeTrial2_Cue
    PracticeTrial2_Cue.tStop = globalClock.getTime(format='float')
    PracticeTrial2_Cue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PracticeTrial2_Cue.stopped', PracticeTrial2_Cue.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if PracticeTrial2_Cue.maxDurationReached:
        routineTimer.addTime(-PracticeTrial2_Cue.maxDuration)
    elif PracticeTrial2_Cue.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop2 = data.TrialHandler2(
        name='practiceLoop2',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('PracticeTrials/PracticeTrials2.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practiceLoop2)  # add the loop to the experiment
    thisPracticeLoop2 = practiceLoop2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop2.rgb)
    if thisPracticeLoop2 != None:
        for paramName in thisPracticeLoop2:
            globals()[paramName] = thisPracticeLoop2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeLoop2 in practiceLoop2:
        practiceLoop2.status = STARTED
        if hasattr(thisPracticeLoop2, 'status'):
            thisPracticeLoop2.status = STARTED
        currentLoop = practiceLoop2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop2.rgb)
        if thisPracticeLoop2 != None:
            for paramName in thisPracticeLoop2:
                globals()[paramName] = thisPracticeLoop2[paramName]
        
        # --- Prepare to start Routine "PracticeTrial_Stim" ---
        # create an object to store info about Routine PracticeTrial_Stim
        PracticeTrial_Stim = data.Routine(
            name='PracticeTrial_Stim',
            components=[response, Stim, Stim_LeftScreenInstruction, Stim_RightScreenInstruction],
        )
        PracticeTrial_Stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from targetLogic
        # Decide correct key for this trial
        if TargetType == 'target':
            correctKey = matchKey
        else:
            correctKey = noMatchKey
        
        # create starting attributes for response
        response.keys = []
        response.rt = []
        _response_allKeys = []
        Stim.setImage(Stimulus)
        Stim_LeftScreenInstruction.reset()
        Stim_LeftScreenInstruction.setText(leftScreenInstruction)
        Stim_RightScreenInstruction.reset()
        Stim_RightScreenInstruction.setText(rightScreenInstruction)
        # store start times for PracticeTrial_Stim
        PracticeTrial_Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Stim.tStart = globalClock.getTime(format='float')
        PracticeTrial_Stim.status = STARTED
        thisExp.addData('PracticeTrial_Stim.started', PracticeTrial_Stim.tStart)
        PracticeTrial_Stim.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_StimComponents = PracticeTrial_Stim.components
        for thisComponent in PracticeTrial_Stim.components:
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
        
        # --- Run Routine "PracticeTrial_Stim" ---
        PracticeTrial_Stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop2, 'status') and thisPracticeLoop2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = response.getKeys(keyList=[matchKey, noMatchKey], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # *Stim_LeftScreenInstruction* updates
            
            # if Stim_LeftScreenInstruction is starting this frame...
            if Stim_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_LeftScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.started')
                # update status
                Stim_LeftScreenInstruction.status = STARTED
                Stim_LeftScreenInstruction.setAutoDraw(True)
            
            # if Stim_LeftScreenInstruction is active this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_LeftScreenInstruction is stopping this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_LeftScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_LeftScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_LeftScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_LeftScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.stopped')
                    # update status
                    Stim_LeftScreenInstruction.status = FINISHED
                    Stim_LeftScreenInstruction.setAutoDraw(False)
            
            # *Stim_RightScreenInstruction* updates
            
            # if Stim_RightScreenInstruction is starting this frame...
            if Stim_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_RightScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.started')
                # update status
                Stim_RightScreenInstruction.status = STARTED
                Stim_RightScreenInstruction.setAutoDraw(True)
            
            # if Stim_RightScreenInstruction is active this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_RightScreenInstruction is stopping this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_RightScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_RightScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_RightScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_RightScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.stopped')
                    # update status
                    Stim_RightScreenInstruction.status = FINISHED
                    Stim_RightScreenInstruction.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Stim" ---
        for thisComponent in PracticeTrial_Stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Stim
        PracticeTrial_Stim.tStop = globalClock.getTime(format='float')
        PracticeTrial_Stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Stim.stopped', PracticeTrial_Stim.tStop)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceLoop2 (TrialHandler)
        practiceLoop2.addData('response.keys',response.keys)
        practiceLoop2.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceLoop2.addData('response.rt', response.rt)
            practiceLoop2.addData('response.duration', response.duration)
        # Run 'End Routine' code from feedbackLogic
        if response.keys is None:
            fbText = "No response."
            fbColor = 'yellow'
        elif response.corr:
            fbText = "Correct!"
            fbColor = 'limegreen'
        else:
            fbText = "Incorrect"
            fbColor = 'red'
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Stim.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Stim.maxDuration)
        elif PracticeTrial_Stim.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "PracticeTrial_Feedback" ---
        # create an object to store info about Routine PracticeTrial_Feedback
        PracticeTrial_Feedback = data.Routine(
            name='PracticeTrial_Feedback',
            components=[Fix, Feedback],
        )
        PracticeTrial_Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Fix.reset()
        Feedback.reset()
        Feedback.setColor(fbColor, colorSpace='rgb')
        Feedback.setText(fbText)
        # store start times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Feedback.tStart = globalClock.getTime(format='float')
        PracticeTrial_Feedback.status = STARTED
        thisExp.addData('PracticeTrial_Feedback.started', PracticeTrial_Feedback.tStart)
        PracticeTrial_Feedback.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_FeedbackComponents = PracticeTrial_Feedback.components
        for thisComponent in PracticeTrial_Feedback.components:
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
        
        # --- Run Routine "PracticeTrial_Feedback" ---
        PracticeTrial_Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop2, 'status') and thisPracticeLoop2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # *Feedback* updates
            
            # if Feedback is starting this frame...
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                # update status
                Feedback.status = STARTED
                Feedback.setAutoDraw(True)
            
            # if Feedback is active this frame...
            if Feedback.status == STARTED:
                # update params
                pass
            
            # if Feedback is stopping this frame...
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    # update status
                    Feedback.status = FINISHED
                    Feedback.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Feedback" ---
        for thisComponent in PracticeTrial_Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStop = globalClock.getTime(format='float')
        PracticeTrial_Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Feedback.stopped', PracticeTrial_Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Feedback.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Feedback.maxDuration)
        elif PracticeTrial_Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeLoop2 as finished
        if hasattr(thisPracticeLoop2, 'status'):
            thisPracticeLoop2.status = FINISHED
        # if awaiting a pause, pause now
        if practiceLoop2.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceLoop2.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practiceLoop2'
    practiceLoop2.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "InstructionsSpaceToContinue" ---
    # create an object to store info about Routine InstructionsSpaceToContinue
    InstructionsSpaceToContinue = data.Routine(
        name='InstructionsSpaceToContinue',
        components=[NextPage_9, Instructions_Space],
    )
    InstructionsSpaceToContinue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_9
    NextPage_9.keys = []
    NextPage_9.rt = []
    _NextPage_9_allKeys = []
    Instructions_Space.reset()
    # store start times for InstructionsSpaceToContinue
    InstructionsSpaceToContinue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    InstructionsSpaceToContinue.tStart = globalClock.getTime(format='float')
    InstructionsSpaceToContinue.status = STARTED
    thisExp.addData('InstructionsSpaceToContinue.started', InstructionsSpaceToContinue.tStart)
    InstructionsSpaceToContinue.maxDuration = None
    # keep track of which components have finished
    InstructionsSpaceToContinueComponents = InstructionsSpaceToContinue.components
    for thisComponent in InstructionsSpaceToContinue.components:
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
    
    # --- Run Routine "InstructionsSpaceToContinue" ---
    InstructionsSpaceToContinue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_9* updates
        waitOnFlip = False
        
        # if NextPage_9 is starting this frame...
        if NextPage_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_9.frameNStart = frameN  # exact frame index
            NextPage_9.tStart = t  # local t and not account for scr refresh
            NextPage_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_9.started')
            # update status
            NextPage_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_9.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_9_allKeys.extend(theseKeys)
            if len(_NextPage_9_allKeys):
                NextPage_9.keys = _NextPage_9_allKeys[-1].name  # just the last key pressed
                NextPage_9.rt = _NextPage_9_allKeys[-1].rt
                NextPage_9.duration = _NextPage_9_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_Space* updates
        
        # if Instructions_Space is starting this frame...
        if Instructions_Space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Space.frameNStart = frameN  # exact frame index
            Instructions_Space.tStart = t  # local t and not account for scr refresh
            Instructions_Space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Space, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Space.started')
            # update status
            Instructions_Space.status = STARTED
            Instructions_Space.setAutoDraw(True)
        
        # if Instructions_Space is active this frame...
        if Instructions_Space.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=InstructionsSpaceToContinue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            InstructionsSpaceToContinue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsSpaceToContinue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionsSpaceToContinue" ---
    for thisComponent in InstructionsSpaceToContinue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for InstructionsSpaceToContinue
    InstructionsSpaceToContinue.tStop = globalClock.getTime(format='float')
    InstructionsSpaceToContinue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('InstructionsSpaceToContinue.stopped', InstructionsSpaceToContinue.tStop)
    # check responses
    if NextPage_9.keys in ['', [], None]:  # No response was made
        NextPage_9.keys = None
    thisExp.addData('NextPage_9.keys',NextPage_9.keys)
    if NextPage_9.keys != None:  # we had a response
        thisExp.addData('NextPage_9.rt', NextPage_9.rt)
        thisExp.addData('NextPage_9.duration', NextPage_9.duration)
    thisExp.nextEntry()
    # the Routine "InstructionsSpaceToContinue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions8" ---
    # create an object to store info about Routine Instructions8
    Instructions8 = data.Routine(
        name='Instructions8',
        components=[NextPage_10, Instructions_8],
    )
    Instructions8.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_10
    NextPage_10.keys = []
    NextPage_10.rt = []
    _NextPage_10_allKeys = []
    Instructions_8.reset()
    # store start times for Instructions8
    Instructions8.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions8.tStart = globalClock.getTime(format='float')
    Instructions8.status = STARTED
    thisExp.addData('Instructions8.started', Instructions8.tStart)
    Instructions8.maxDuration = None
    # keep track of which components have finished
    Instructions8Components = Instructions8.components
    for thisComponent in Instructions8.components:
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
    
    # --- Run Routine "Instructions8" ---
    Instructions8.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_10* updates
        waitOnFlip = False
        
        # if NextPage_10 is starting this frame...
        if NextPage_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_10.frameNStart = frameN  # exact frame index
            NextPage_10.tStart = t  # local t and not account for scr refresh
            NextPage_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_10.started')
            # update status
            NextPage_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_10.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_10.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_10_allKeys.extend(theseKeys)
            if len(_NextPage_10_allKeys):
                NextPage_10.keys = _NextPage_10_allKeys[-1].name  # just the last key pressed
                NextPage_10.rt = _NextPage_10_allKeys[-1].rt
                NextPage_10.duration = _NextPage_10_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_8* updates
        
        # if Instructions_8 is starting this frame...
        if Instructions_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_8.frameNStart = frameN  # exact frame index
            Instructions_8.tStart = t  # local t and not account for scr refresh
            Instructions_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_8.started')
            # update status
            Instructions_8.status = STARTED
            Instructions_8.setAutoDraw(True)
        
        # if Instructions_8 is active this frame...
        if Instructions_8.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions8,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions8.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions8.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions8" ---
    for thisComponent in Instructions8.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions8
    Instructions8.tStop = globalClock.getTime(format='float')
    Instructions8.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions8.stopped', Instructions8.tStop)
    # check responses
    if NextPage_10.keys in ['', [], None]:  # No response was made
        NextPage_10.keys = None
    thisExp.addData('NextPage_10.keys',NextPage_10.keys)
    if NextPage_10.keys != None:  # we had a response
        thisExp.addData('NextPage_10.rt', NextPage_10.rt)
        thisExp.addData('NextPage_10.duration', NextPage_10.duration)
    thisExp.nextEntry()
    # the Routine "Instructions8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions9" ---
    # create an object to store info about Routine Instructions9
    Instructions9 = data.Routine(
        name='Instructions9',
        components=[NextPage_12, Instructions_9, Example_Stim, Example_LeftScreenInstruction, Example_RightScreenInstruction, Instructions_12],
    )
    Instructions9.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_12
    NextPage_12.keys = []
    NextPage_12.rt = []
    _NextPage_12_allKeys = []
    Instructions_9.reset()
    Example_Stim.setImage('VM Stimuli/PracticeFO1.bmp')
    Example_LeftScreenInstruction.reset()
    Example_LeftScreenInstruction.setText(leftScreenInstruction)
    Example_RightScreenInstruction.reset()
    Example_RightScreenInstruction.setText(rightScreenInstruction)
    Instructions_12.reset()
    # store start times for Instructions9
    Instructions9.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions9.tStart = globalClock.getTime(format='float')
    Instructions9.status = STARTED
    thisExp.addData('Instructions9.started', Instructions9.tStart)
    Instructions9.maxDuration = None
    # keep track of which components have finished
    Instructions9Components = Instructions9.components
    for thisComponent in Instructions9.components:
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
    
    # --- Run Routine "Instructions9" ---
    Instructions9.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_12* updates
        waitOnFlip = False
        
        # if NextPage_12 is starting this frame...
        if NextPage_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_12.frameNStart = frameN  # exact frame index
            NextPage_12.tStart = t  # local t and not account for scr refresh
            NextPage_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_12.started')
            # update status
            NextPage_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_12.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_12.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_12_allKeys.extend(theseKeys)
            if len(_NextPage_12_allKeys):
                NextPage_12.keys = _NextPage_12_allKeys[-1].name  # just the last key pressed
                NextPage_12.rt = _NextPage_12_allKeys[-1].rt
                NextPage_12.duration = _NextPage_12_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_9* updates
        
        # if Instructions_9 is starting this frame...
        if Instructions_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_9.frameNStart = frameN  # exact frame index
            Instructions_9.tStart = t  # local t and not account for scr refresh
            Instructions_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_9.started')
            # update status
            Instructions_9.status = STARTED
            Instructions_9.setAutoDraw(True)
        
        # if Instructions_9 is active this frame...
        if Instructions_9.status == STARTED:
            # update params
            pass
        
        # *Example_Stim* updates
        
        # if Example_Stim is starting this frame...
        if Example_Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim.frameNStart = frameN  # exact frame index
            Example_Stim.tStart = t  # local t and not account for scr refresh
            Example_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim.started')
            # update status
            Example_Stim.status = STARTED
            Example_Stim.setAutoDraw(True)
        
        # if Example_Stim is active this frame...
        if Example_Stim.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction* updates
        
        # if Example_LeftScreenInstruction is starting this frame...
        if Example_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction.started')
            # update status
            Example_LeftScreenInstruction.status = STARTED
            Example_LeftScreenInstruction.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction is active this frame...
        if Example_LeftScreenInstruction.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction* updates
        
        # if Example_RightScreenInstruction is starting this frame...
        if Example_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction.started')
            # update status
            Example_RightScreenInstruction.status = STARTED
            Example_RightScreenInstruction.setAutoDraw(True)
        
        # if Example_RightScreenInstruction is active this frame...
        if Example_RightScreenInstruction.status == STARTED:
            # update params
            pass
        
        # *Instructions_12* updates
        
        # if Instructions_12 is starting this frame...
        if Instructions_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_12.frameNStart = frameN  # exact frame index
            Instructions_12.tStart = t  # local t and not account for scr refresh
            Instructions_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_12.started')
            # update status
            Instructions_12.status = STARTED
            Instructions_12.setAutoDraw(True)
        
        # if Instructions_12 is active this frame...
        if Instructions_12.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions9,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions9.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions9.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions9" ---
    for thisComponent in Instructions9.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions9
    Instructions9.tStop = globalClock.getTime(format='float')
    Instructions9.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions9.stopped', Instructions9.tStop)
    # check responses
    if NextPage_12.keys in ['', [], None]:  # No response was made
        NextPage_12.keys = None
    thisExp.addData('NextPage_12.keys',NextPage_12.keys)
    if NextPage_12.keys != None:  # we had a response
        thisExp.addData('NextPage_12.rt', NextPage_12.rt)
        thisExp.addData('NextPage_12.duration', NextPage_12.duration)
    thisExp.nextEntry()
    # the Routine "Instructions9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions21" ---
    # create an object to store info about Routine Instructions21
    Instructions21 = data.Routine(
        name='Instructions21',
        components=[NextPage_13, Instructions_21, One_Back_Example_Stim, Example_Stim_2, Example_LeftScreenInstruction_2, Example_RightScreenInstruction_2],
    )
    Instructions21.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_13
    NextPage_13.keys = []
    NextPage_13.rt = []
    _NextPage_13_allKeys = []
    Instructions_21.reset()
    Example_Stim_2.setImage('VM Stimuli/PracticeFO2.bmp')
    Example_LeftScreenInstruction_2.reset()
    Example_LeftScreenInstruction_2.setText(leftScreenInstruction)
    Example_RightScreenInstruction_2.reset()
    Example_RightScreenInstruction_2.setText(rightScreenInstruction)
    # store start times for Instructions21
    Instructions21.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions21.tStart = globalClock.getTime(format='float')
    Instructions21.status = STARTED
    thisExp.addData('Instructions21.started', Instructions21.tStart)
    Instructions21.maxDuration = None
    # keep track of which components have finished
    Instructions21Components = Instructions21.components
    for thisComponent in Instructions21.components:
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
    
    # --- Run Routine "Instructions21" ---
    Instructions21.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_13* updates
        waitOnFlip = False
        
        # if NextPage_13 is starting this frame...
        if NextPage_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_13.frameNStart = frameN  # exact frame index
            NextPage_13.tStart = t  # local t and not account for scr refresh
            NextPage_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_13.started')
            # update status
            NextPage_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_13.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_13.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_13_allKeys.extend(theseKeys)
            if len(_NextPage_13_allKeys):
                NextPage_13.keys = _NextPage_13_allKeys[-1].name  # just the last key pressed
                NextPage_13.rt = _NextPage_13_allKeys[-1].rt
                NextPage_13.duration = _NextPage_13_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_21* updates
        
        # if Instructions_21 is starting this frame...
        if Instructions_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_21.frameNStart = frameN  # exact frame index
            Instructions_21.tStart = t  # local t and not account for scr refresh
            Instructions_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_21.started')
            # update status
            Instructions_21.status = STARTED
            Instructions_21.setAutoDraw(True)
        
        # if Instructions_21 is active this frame...
        if Instructions_21.status == STARTED:
            # update params
            pass
        
        # *One_Back_Example_Stim* updates
        
        # if One_Back_Example_Stim is starting this frame...
        if One_Back_Example_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            One_Back_Example_Stim.frameNStart = frameN  # exact frame index
            One_Back_Example_Stim.tStart = t  # local t and not account for scr refresh
            One_Back_Example_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(One_Back_Example_Stim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'One_Back_Example_Stim.started')
            # update status
            One_Back_Example_Stim.status = STARTED
            One_Back_Example_Stim.setAutoDraw(True)
        
        # if One_Back_Example_Stim is active this frame...
        if One_Back_Example_Stim.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_2* updates
        
        # if Example_Stim_2 is starting this frame...
        if Example_Stim_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_2.frameNStart = frameN  # exact frame index
            Example_Stim_2.tStart = t  # local t and not account for scr refresh
            Example_Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_2.started')
            # update status
            Example_Stim_2.status = STARTED
            Example_Stim_2.setAutoDraw(True)
        
        # if Example_Stim_2 is active this frame...
        if Example_Stim_2.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_2* updates
        
        # if Example_LeftScreenInstruction_2 is starting this frame...
        if Example_LeftScreenInstruction_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_2.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_2.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_2.started')
            # update status
            Example_LeftScreenInstruction_2.status = STARTED
            Example_LeftScreenInstruction_2.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_2 is active this frame...
        if Example_LeftScreenInstruction_2.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_2* updates
        
        # if Example_RightScreenInstruction_2 is starting this frame...
        if Example_RightScreenInstruction_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_2.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_2.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_2.started')
            # update status
            Example_RightScreenInstruction_2.status = STARTED
            Example_RightScreenInstruction_2.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_2 is active this frame...
        if Example_RightScreenInstruction_2.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions21,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions21.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions21.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions21" ---
    for thisComponent in Instructions21.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions21
    Instructions21.tStop = globalClock.getTime(format='float')
    Instructions21.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions21.stopped', Instructions21.tStop)
    # check responses
    if NextPage_13.keys in ['', [], None]:  # No response was made
        NextPage_13.keys = None
    thisExp.addData('NextPage_13.keys',NextPage_13.keys)
    if NextPage_13.keys != None:  # we had a response
        thisExp.addData('NextPage_13.rt', NextPage_13.rt)
        thisExp.addData('NextPage_13.duration', NextPage_13.duration)
    thisExp.nextEntry()
    # the Routine "Instructions21" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions24" ---
    # create an object to store info about Routine Instructions24
    Instructions24 = data.Routine(
        name='Instructions24',
        components=[NextPage_14, Instructions_24, Green_Border, Two_Back_Example_Stim, One_Back_Example_Stim_2, Example_Stim_3, Example_LeftScreenInstruction_3, Example_RightScreenInstruction_3],
    )
    Instructions24.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_14
    NextPage_14.keys = []
    NextPage_14.rt = []
    _NextPage_14_allKeys = []
    Instructions_24.reset()
    Example_Stim_3.setImage('VM Stimuli/PracticeFO1.bmp')
    Example_LeftScreenInstruction_3.reset()
    Example_LeftScreenInstruction_3.setText(leftScreenInstruction)
    Example_RightScreenInstruction_3.reset()
    Example_RightScreenInstruction_3.setText(rightScreenInstruction)
    # store start times for Instructions24
    Instructions24.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions24.tStart = globalClock.getTime(format='float')
    Instructions24.status = STARTED
    thisExp.addData('Instructions24.started', Instructions24.tStart)
    Instructions24.maxDuration = None
    # keep track of which components have finished
    Instructions24Components = Instructions24.components
    for thisComponent in Instructions24.components:
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
    
    # --- Run Routine "Instructions24" ---
    Instructions24.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_14* updates
        waitOnFlip = False
        
        # if NextPage_14 is starting this frame...
        if NextPage_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_14.frameNStart = frameN  # exact frame index
            NextPage_14.tStart = t  # local t and not account for scr refresh
            NextPage_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_14.started')
            # update status
            NextPage_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_14.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_14.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_14_allKeys.extend(theseKeys)
            if len(_NextPage_14_allKeys):
                NextPage_14.keys = _NextPage_14_allKeys[-1].name  # just the last key pressed
                NextPage_14.rt = _NextPage_14_allKeys[-1].rt
                NextPage_14.duration = _NextPage_14_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_24* updates
        
        # if Instructions_24 is starting this frame...
        if Instructions_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_24.frameNStart = frameN  # exact frame index
            Instructions_24.tStart = t  # local t and not account for scr refresh
            Instructions_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_24.started')
            # update status
            Instructions_24.status = STARTED
            Instructions_24.setAutoDraw(True)
        
        # if Instructions_24 is active this frame...
        if Instructions_24.status == STARTED:
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
        
        # *Two_Back_Example_Stim* updates
        
        # if Two_Back_Example_Stim is starting this frame...
        if Two_Back_Example_Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Two_Back_Example_Stim.frameNStart = frameN  # exact frame index
            Two_Back_Example_Stim.tStart = t  # local t and not account for scr refresh
            Two_Back_Example_Stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Two_Back_Example_Stim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Two_Back_Example_Stim.started')
            # update status
            Two_Back_Example_Stim.status = STARTED
            Two_Back_Example_Stim.setAutoDraw(True)
        
        # if Two_Back_Example_Stim is active this frame...
        if Two_Back_Example_Stim.status == STARTED:
            # update params
            pass
        
        # *One_Back_Example_Stim_2* updates
        
        # if One_Back_Example_Stim_2 is starting this frame...
        if One_Back_Example_Stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            One_Back_Example_Stim_2.frameNStart = frameN  # exact frame index
            One_Back_Example_Stim_2.tStart = t  # local t and not account for scr refresh
            One_Back_Example_Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(One_Back_Example_Stim_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'One_Back_Example_Stim_2.started')
            # update status
            One_Back_Example_Stim_2.status = STARTED
            One_Back_Example_Stim_2.setAutoDraw(True)
        
        # if One_Back_Example_Stim_2 is active this frame...
        if One_Back_Example_Stim_2.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_3* updates
        
        # if Example_Stim_3 is starting this frame...
        if Example_Stim_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_3.frameNStart = frameN  # exact frame index
            Example_Stim_3.tStart = t  # local t and not account for scr refresh
            Example_Stim_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_3.started')
            # update status
            Example_Stim_3.status = STARTED
            Example_Stim_3.setAutoDraw(True)
        
        # if Example_Stim_3 is active this frame...
        if Example_Stim_3.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_3* updates
        
        # if Example_LeftScreenInstruction_3 is starting this frame...
        if Example_LeftScreenInstruction_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_3.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_3.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_3.started')
            # update status
            Example_LeftScreenInstruction_3.status = STARTED
            Example_LeftScreenInstruction_3.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_3 is active this frame...
        if Example_LeftScreenInstruction_3.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_3* updates
        
        # if Example_RightScreenInstruction_3 is starting this frame...
        if Example_RightScreenInstruction_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_3.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_3.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_3.started')
            # update status
            Example_RightScreenInstruction_3.status = STARTED
            Example_RightScreenInstruction_3.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_3 is active this frame...
        if Example_RightScreenInstruction_3.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions24,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions24.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions24.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions24" ---
    for thisComponent in Instructions24.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions24
    Instructions24.tStop = globalClock.getTime(format='float')
    Instructions24.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions24.stopped', Instructions24.tStop)
    # check responses
    if NextPage_14.keys in ['', [], None]:  # No response was made
        NextPage_14.keys = None
    thisExp.addData('NextPage_14.keys',NextPage_14.keys)
    if NextPage_14.keys != None:  # we had a response
        thisExp.addData('NextPage_14.rt', NextPage_14.rt)
        thisExp.addData('NextPage_14.duration', NextPage_14.duration)
    thisExp.nextEntry()
    # the Routine "Instructions24" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions25" ---
    # create an object to store info about Routine Instructions25
    Instructions25 = data.Routine(
        name='Instructions25',
        components=[NextPage_15, Instructions_25, Two_Back_Example_Stim_2, One_Back_Example_Stim_3, Example_Stim_4, Example_LeftScreenInstruction_4, Example_RightScreenInstruction_4],
    )
    Instructions25.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_15
    NextPage_15.keys = []
    NextPage_15.rt = []
    _NextPage_15_allKeys = []
    Instructions_25.reset()
    Example_Stim_4.setImage('VM Stimuli/PracticeFO3.bmp')
    Example_LeftScreenInstruction_4.reset()
    Example_LeftScreenInstruction_4.setText(leftScreenInstruction)
    Example_RightScreenInstruction_4.reset()
    Example_RightScreenInstruction_4.setText(rightScreenInstruction)
    # store start times for Instructions25
    Instructions25.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions25.tStart = globalClock.getTime(format='float')
    Instructions25.status = STARTED
    thisExp.addData('Instructions25.started', Instructions25.tStart)
    Instructions25.maxDuration = None
    # keep track of which components have finished
    Instructions25Components = Instructions25.components
    for thisComponent in Instructions25.components:
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
    
    # --- Run Routine "Instructions25" ---
    Instructions25.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_15* updates
        waitOnFlip = False
        
        # if NextPage_15 is starting this frame...
        if NextPage_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_15.frameNStart = frameN  # exact frame index
            NextPage_15.tStart = t  # local t and not account for scr refresh
            NextPage_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_15.started')
            # update status
            NextPage_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_15.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_15.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_15_allKeys.extend(theseKeys)
            if len(_NextPage_15_allKeys):
                NextPage_15.keys = _NextPage_15_allKeys[-1].name  # just the last key pressed
                NextPage_15.rt = _NextPage_15_allKeys[-1].rt
                NextPage_15.duration = _NextPage_15_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_25* updates
        
        # if Instructions_25 is starting this frame...
        if Instructions_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_25.frameNStart = frameN  # exact frame index
            Instructions_25.tStart = t  # local t and not account for scr refresh
            Instructions_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_25.started')
            # update status
            Instructions_25.status = STARTED
            Instructions_25.setAutoDraw(True)
        
        # if Instructions_25 is active this frame...
        if Instructions_25.status == STARTED:
            # update params
            pass
        
        # *Two_Back_Example_Stim_2* updates
        
        # if Two_Back_Example_Stim_2 is starting this frame...
        if Two_Back_Example_Stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Two_Back_Example_Stim_2.frameNStart = frameN  # exact frame index
            Two_Back_Example_Stim_2.tStart = t  # local t and not account for scr refresh
            Two_Back_Example_Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Two_Back_Example_Stim_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Two_Back_Example_Stim_2.started')
            # update status
            Two_Back_Example_Stim_2.status = STARTED
            Two_Back_Example_Stim_2.setAutoDraw(True)
        
        # if Two_Back_Example_Stim_2 is active this frame...
        if Two_Back_Example_Stim_2.status == STARTED:
            # update params
            pass
        
        # *One_Back_Example_Stim_3* updates
        
        # if One_Back_Example_Stim_3 is starting this frame...
        if One_Back_Example_Stim_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            One_Back_Example_Stim_3.frameNStart = frameN  # exact frame index
            One_Back_Example_Stim_3.tStart = t  # local t and not account for scr refresh
            One_Back_Example_Stim_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(One_Back_Example_Stim_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'One_Back_Example_Stim_3.started')
            # update status
            One_Back_Example_Stim_3.status = STARTED
            One_Back_Example_Stim_3.setAutoDraw(True)
        
        # if One_Back_Example_Stim_3 is active this frame...
        if One_Back_Example_Stim_3.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_4* updates
        
        # if Example_Stim_4 is starting this frame...
        if Example_Stim_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_4.frameNStart = frameN  # exact frame index
            Example_Stim_4.tStart = t  # local t and not account for scr refresh
            Example_Stim_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_4.started')
            # update status
            Example_Stim_4.status = STARTED
            Example_Stim_4.setAutoDraw(True)
        
        # if Example_Stim_4 is active this frame...
        if Example_Stim_4.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_4* updates
        
        # if Example_LeftScreenInstruction_4 is starting this frame...
        if Example_LeftScreenInstruction_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_4.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_4.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_4.started')
            # update status
            Example_LeftScreenInstruction_4.status = STARTED
            Example_LeftScreenInstruction_4.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_4 is active this frame...
        if Example_LeftScreenInstruction_4.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_4* updates
        
        # if Example_RightScreenInstruction_4 is starting this frame...
        if Example_RightScreenInstruction_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_4.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_4.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_4.started')
            # update status
            Example_RightScreenInstruction_4.status = STARTED
            Example_RightScreenInstruction_4.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_4 is active this frame...
        if Example_RightScreenInstruction_4.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions25,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions25.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions25.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions25" ---
    for thisComponent in Instructions25.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions25
    Instructions25.tStop = globalClock.getTime(format='float')
    Instructions25.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions25.stopped', Instructions25.tStop)
    # check responses
    if NextPage_15.keys in ['', [], None]:  # No response was made
        NextPage_15.keys = None
    thisExp.addData('NextPage_15.keys',NextPage_15.keys)
    if NextPage_15.keys != None:  # we had a response
        thisExp.addData('NextPage_15.rt', NextPage_15.rt)
        thisExp.addData('NextPage_15.duration', NextPage_15.duration)
    thisExp.nextEntry()
    # the Routine "Instructions25" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions15" ---
    # create an object to store info about Routine Instructions15
    Instructions15 = data.Routine(
        name='Instructions15',
        components=[NextPage_16, Instructions_15],
    )
    Instructions15.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_16
    NextPage_16.keys = []
    NextPage_16.rt = []
    _NextPage_16_allKeys = []
    Instructions_15.reset()
    # store start times for Instructions15
    Instructions15.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions15.tStart = globalClock.getTime(format='float')
    Instructions15.status = STARTED
    thisExp.addData('Instructions15.started', Instructions15.tStart)
    Instructions15.maxDuration = None
    # keep track of which components have finished
    Instructions15Components = Instructions15.components
    for thisComponent in Instructions15.components:
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
    
    # --- Run Routine "Instructions15" ---
    Instructions15.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_16* updates
        waitOnFlip = False
        
        # if NextPage_16 is starting this frame...
        if NextPage_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_16.frameNStart = frameN  # exact frame index
            NextPage_16.tStart = t  # local t and not account for scr refresh
            NextPage_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_16.started')
            # update status
            NextPage_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_16.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_16.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_16_allKeys.extend(theseKeys)
            if len(_NextPage_16_allKeys):
                NextPage_16.keys = _NextPage_16_allKeys[-1].name  # just the last key pressed
                NextPage_16.rt = _NextPage_16_allKeys[-1].rt
                NextPage_16.duration = _NextPage_16_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_15* updates
        
        # if Instructions_15 is starting this frame...
        if Instructions_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_15.frameNStart = frameN  # exact frame index
            Instructions_15.tStart = t  # local t and not account for scr refresh
            Instructions_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_15.started')
            # update status
            Instructions_15.status = STARTED
            Instructions_15.setAutoDraw(True)
        
        # if Instructions_15 is active this frame...
        if Instructions_15.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions15,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions15.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions15.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions15" ---
    for thisComponent in Instructions15.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions15
    Instructions15.tStop = globalClock.getTime(format='float')
    Instructions15.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions15.stopped', Instructions15.tStop)
    # check responses
    if NextPage_16.keys in ['', [], None]:  # No response was made
        NextPage_16.keys = None
    thisExp.addData('NextPage_16.keys',NextPage_16.keys)
    if NextPage_16.keys != None:  # we had a response
        thisExp.addData('NextPage_16.rt', NextPage_16.rt)
        thisExp.addData('NextPage_16.duration', NextPage_16.duration)
    thisExp.nextEntry()
    # the Routine "Instructions15" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions32" ---
    # create an object to store info about Routine Instructions32
    Instructions32 = data.Routine(
        name='Instructions32',
        components=[NextPage_17, Instructions_32, Example_Stim_5, Example_LeftScreenInstruction_5, Example_RightScreenInstruction_5],
    )
    Instructions32.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_17
    NextPage_17.keys = []
    NextPage_17.rt = []
    _NextPage_17_allKeys = []
    Instructions_32.reset()
    Example_LeftScreenInstruction_5.reset()
    Example_LeftScreenInstruction_5.setText(leftScreenInstruction)
    Example_RightScreenInstruction_5.reset()
    Example_RightScreenInstruction_5.setText(rightScreenInstruction)
    # store start times for Instructions32
    Instructions32.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions32.tStart = globalClock.getTime(format='float')
    Instructions32.status = STARTED
    thisExp.addData('Instructions32.started', Instructions32.tStart)
    Instructions32.maxDuration = None
    # keep track of which components have finished
    Instructions32Components = Instructions32.components
    for thisComponent in Instructions32.components:
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
    
    # --- Run Routine "Instructions32" ---
    Instructions32.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_17* updates
        waitOnFlip = False
        
        # if NextPage_17 is starting this frame...
        if NextPage_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_17.frameNStart = frameN  # exact frame index
            NextPage_17.tStart = t  # local t and not account for scr refresh
            NextPage_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_17.started')
            # update status
            NextPage_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_17.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_17.getKeys(keyList=['space','left','right'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_17_allKeys.extend(theseKeys)
            if len(_NextPage_17_allKeys):
                NextPage_17.keys = _NextPage_17_allKeys[-1].name  # just the last key pressed
                NextPage_17.rt = _NextPage_17_allKeys[-1].rt
                NextPage_17.duration = _NextPage_17_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_32* updates
        
        # if Instructions_32 is starting this frame...
        if Instructions_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_32.frameNStart = frameN  # exact frame index
            Instructions_32.tStart = t  # local t and not account for scr refresh
            Instructions_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_32, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_32.started')
            # update status
            Instructions_32.status = STARTED
            Instructions_32.setAutoDraw(True)
        
        # if Instructions_32 is active this frame...
        if Instructions_32.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_5* updates
        
        # if Example_Stim_5 is starting this frame...
        if Example_Stim_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_5.frameNStart = frameN  # exact frame index
            Example_Stim_5.tStart = t  # local t and not account for scr refresh
            Example_Stim_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_5.started')
            # update status
            Example_Stim_5.status = STARTED
            Example_Stim_5.setAutoDraw(True)
        
        # if Example_Stim_5 is active this frame...
        if Example_Stim_5.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_5* updates
        
        # if Example_LeftScreenInstruction_5 is starting this frame...
        if Example_LeftScreenInstruction_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_5.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_5.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_5.started')
            # update status
            Example_LeftScreenInstruction_5.status = STARTED
            Example_LeftScreenInstruction_5.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_5 is active this frame...
        if Example_LeftScreenInstruction_5.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_5* updates
        
        # if Example_RightScreenInstruction_5 is starting this frame...
        if Example_RightScreenInstruction_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_5.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_5.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_5.started')
            # update status
            Example_RightScreenInstruction_5.status = STARTED
            Example_RightScreenInstruction_5.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_5 is active this frame...
        if Example_RightScreenInstruction_5.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions32,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions32.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions32.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions32" ---
    for thisComponent in Instructions32.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions32
    Instructions32.tStop = globalClock.getTime(format='float')
    Instructions32.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions32.stopped', Instructions32.tStop)
    # check responses
    if NextPage_17.keys in ['', [], None]:  # No response was made
        NextPage_17.keys = None
    thisExp.addData('NextPage_17.keys',NextPage_17.keys)
    if NextPage_17.keys != None:  # we had a response
        thisExp.addData('NextPage_17.rt', NextPage_17.rt)
        thisExp.addData('NextPage_17.duration', NextPage_17.duration)
    thisExp.nextEntry()
    # the Routine "Instructions32" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions27" ---
    # create an object to store info about Routine Instructions27
    Instructions27 = data.Routine(
        name='Instructions27',
        components=[NextPage_18, Instructions_27, Example_Stim_6, Example_LeftScreenInstruction_6, Example_RightScreenInstruction_6],
    )
    Instructions27.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_18
    NextPage_18.keys = []
    NextPage_18.rt = []
    _NextPage_18_allKeys = []
    Instructions_27.reset()
    Example_LeftScreenInstruction_6.reset()
    Example_LeftScreenInstruction_6.setText(leftScreenInstruction)
    Example_RightScreenInstruction_6.reset()
    Example_RightScreenInstruction_6.setText(rightScreenInstruction)
    # store start times for Instructions27
    Instructions27.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions27.tStart = globalClock.getTime(format='float')
    Instructions27.status = STARTED
    thisExp.addData('Instructions27.started', Instructions27.tStart)
    Instructions27.maxDuration = None
    # keep track of which components have finished
    Instructions27Components = Instructions27.components
    for thisComponent in Instructions27.components:
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
    
    # --- Run Routine "Instructions27" ---
    Instructions27.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_18* updates
        waitOnFlip = False
        
        # if NextPage_18 is starting this frame...
        if NextPage_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_18.frameNStart = frameN  # exact frame index
            NextPage_18.tStart = t  # local t and not account for scr refresh
            NextPage_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_18.started')
            # update status
            NextPage_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_18.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_18.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_18.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_18_allKeys.extend(theseKeys)
            if len(_NextPage_18_allKeys):
                NextPage_18.keys = _NextPage_18_allKeys[-1].name  # just the last key pressed
                NextPage_18.rt = _NextPage_18_allKeys[-1].rt
                NextPage_18.duration = _NextPage_18_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_27* updates
        
        # if Instructions_27 is starting this frame...
        if Instructions_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_27.frameNStart = frameN  # exact frame index
            Instructions_27.tStart = t  # local t and not account for scr refresh
            Instructions_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_27.started')
            # update status
            Instructions_27.status = STARTED
            Instructions_27.setAutoDraw(True)
        
        # if Instructions_27 is active this frame...
        if Instructions_27.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_6* updates
        
        # if Example_Stim_6 is starting this frame...
        if Example_Stim_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_6.frameNStart = frameN  # exact frame index
            Example_Stim_6.tStart = t  # local t and not account for scr refresh
            Example_Stim_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_6.started')
            # update status
            Example_Stim_6.status = STARTED
            Example_Stim_6.setAutoDraw(True)
        
        # if Example_Stim_6 is active this frame...
        if Example_Stim_6.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_6* updates
        
        # if Example_LeftScreenInstruction_6 is starting this frame...
        if Example_LeftScreenInstruction_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_6.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_6.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_6.started')
            # update status
            Example_LeftScreenInstruction_6.status = STARTED
            Example_LeftScreenInstruction_6.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_6 is active this frame...
        if Example_LeftScreenInstruction_6.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_6* updates
        
        # if Example_RightScreenInstruction_6 is starting this frame...
        if Example_RightScreenInstruction_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_6.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_6.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_6.started')
            # update status
            Example_RightScreenInstruction_6.status = STARTED
            Example_RightScreenInstruction_6.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_6 is active this frame...
        if Example_RightScreenInstruction_6.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions27,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions27.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions27.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions27" ---
    for thisComponent in Instructions27.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions27
    Instructions27.tStop = globalClock.getTime(format='float')
    Instructions27.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions27.stopped', Instructions27.tStop)
    # check responses
    if NextPage_18.keys in ['', [], None]:  # No response was made
        NextPage_18.keys = None
    thisExp.addData('NextPage_18.keys',NextPage_18.keys)
    if NextPage_18.keys != None:  # we had a response
        thisExp.addData('NextPage_18.rt', NextPage_18.rt)
        thisExp.addData('NextPage_18.duration', NextPage_18.duration)
    thisExp.nextEntry()
    # the Routine "Instructions27" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions33" ---
    # create an object to store info about Routine Instructions33
    Instructions33 = data.Routine(
        name='Instructions33',
        components=[NextPage_19, Instructions_33, Example_Stim_7, Example_LeftScreenInstruction_7, Example_RightScreenInstruction_7],
    )
    Instructions33.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_19
    NextPage_19.keys = []
    NextPage_19.rt = []
    _NextPage_19_allKeys = []
    Instructions_33.reset()
    Example_LeftScreenInstruction_7.reset()
    Example_LeftScreenInstruction_7.setText(leftScreenInstruction)
    Example_RightScreenInstruction_7.reset()
    Example_RightScreenInstruction_7.setText(rightScreenInstruction)
    # store start times for Instructions33
    Instructions33.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions33.tStart = globalClock.getTime(format='float')
    Instructions33.status = STARTED
    thisExp.addData('Instructions33.started', Instructions33.tStart)
    Instructions33.maxDuration = None
    # keep track of which components have finished
    Instructions33Components = Instructions33.components
    for thisComponent in Instructions33.components:
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
    
    # --- Run Routine "Instructions33" ---
    Instructions33.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_19* updates
        waitOnFlip = False
        
        # if NextPage_19 is starting this frame...
        if NextPage_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_19.frameNStart = frameN  # exact frame index
            NextPage_19.tStart = t  # local t and not account for scr refresh
            NextPage_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_19.started')
            # update status
            NextPage_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_19.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_19.getKeys(keyList=['space','left','right'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_19_allKeys.extend(theseKeys)
            if len(_NextPage_19_allKeys):
                NextPage_19.keys = _NextPage_19_allKeys[-1].name  # just the last key pressed
                NextPage_19.rt = _NextPage_19_allKeys[-1].rt
                NextPage_19.duration = _NextPage_19_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_33* updates
        
        # if Instructions_33 is starting this frame...
        if Instructions_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_33.frameNStart = frameN  # exact frame index
            Instructions_33.tStart = t  # local t and not account for scr refresh
            Instructions_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_33.started')
            # update status
            Instructions_33.status = STARTED
            Instructions_33.setAutoDraw(True)
        
        # if Instructions_33 is active this frame...
        if Instructions_33.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_7* updates
        
        # if Example_Stim_7 is starting this frame...
        if Example_Stim_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_7.frameNStart = frameN  # exact frame index
            Example_Stim_7.tStart = t  # local t and not account for scr refresh
            Example_Stim_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_7.started')
            # update status
            Example_Stim_7.status = STARTED
            Example_Stim_7.setAutoDraw(True)
        
        # if Example_Stim_7 is active this frame...
        if Example_Stim_7.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_7* updates
        
        # if Example_LeftScreenInstruction_7 is starting this frame...
        if Example_LeftScreenInstruction_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_7.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_7.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_7.started')
            # update status
            Example_LeftScreenInstruction_7.status = STARTED
            Example_LeftScreenInstruction_7.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_7 is active this frame...
        if Example_LeftScreenInstruction_7.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_7* updates
        
        # if Example_RightScreenInstruction_7 is starting this frame...
        if Example_RightScreenInstruction_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_7.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_7.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_7.started')
            # update status
            Example_RightScreenInstruction_7.status = STARTED
            Example_RightScreenInstruction_7.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_7 is active this frame...
        if Example_RightScreenInstruction_7.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions33,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions33.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions33.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions33" ---
    for thisComponent in Instructions33.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions33
    Instructions33.tStop = globalClock.getTime(format='float')
    Instructions33.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions33.stopped', Instructions33.tStop)
    # check responses
    if NextPage_19.keys in ['', [], None]:  # No response was made
        NextPage_19.keys = None
    thisExp.addData('NextPage_19.keys',NextPage_19.keys)
    if NextPage_19.keys != None:  # we had a response
        thisExp.addData('NextPage_19.rt', NextPage_19.rt)
        thisExp.addData('NextPage_19.duration', NextPage_19.duration)
    thisExp.nextEntry()
    # the Routine "Instructions33" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions26" ---
    # create an object to store info about Routine Instructions26
    Instructions26 = data.Routine(
        name='Instructions26',
        components=[NextPage_20, Instructions_26, One_Back_Example_Stim_4, Example_Stim_8, Example_LeftScreenInstruction_8, Example_RightScreenInstruction_8],
    )
    Instructions26.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_20
    NextPage_20.keys = []
    NextPage_20.rt = []
    _NextPage_20_allKeys = []
    Instructions_26.reset()
    Example_LeftScreenInstruction_8.reset()
    Example_LeftScreenInstruction_8.setText(leftScreenInstruction)
    Example_RightScreenInstruction_8.reset()
    Example_RightScreenInstruction_8.setText(rightScreenInstruction)
    # store start times for Instructions26
    Instructions26.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions26.tStart = globalClock.getTime(format='float')
    Instructions26.status = STARTED
    thisExp.addData('Instructions26.started', Instructions26.tStart)
    Instructions26.maxDuration = None
    # keep track of which components have finished
    Instructions26Components = Instructions26.components
    for thisComponent in Instructions26.components:
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
    
    # --- Run Routine "Instructions26" ---
    Instructions26.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_20* updates
        waitOnFlip = False
        
        # if NextPage_20 is starting this frame...
        if NextPage_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_20.frameNStart = frameN  # exact frame index
            NextPage_20.tStart = t  # local t and not account for scr refresh
            NextPage_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_20.started')
            # update status
            NextPage_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_20.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_20.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_20.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_20_allKeys.extend(theseKeys)
            if len(_NextPage_20_allKeys):
                NextPage_20.keys = _NextPage_20_allKeys[-1].name  # just the last key pressed
                NextPage_20.rt = _NextPage_20_allKeys[-1].rt
                NextPage_20.duration = _NextPage_20_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_26* updates
        
        # if Instructions_26 is starting this frame...
        if Instructions_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_26.frameNStart = frameN  # exact frame index
            Instructions_26.tStart = t  # local t and not account for scr refresh
            Instructions_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_26.started')
            # update status
            Instructions_26.status = STARTED
            Instructions_26.setAutoDraw(True)
        
        # if Instructions_26 is active this frame...
        if Instructions_26.status == STARTED:
            # update params
            pass
        
        # *One_Back_Example_Stim_4* updates
        
        # if One_Back_Example_Stim_4 is starting this frame...
        if One_Back_Example_Stim_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            One_Back_Example_Stim_4.frameNStart = frameN  # exact frame index
            One_Back_Example_Stim_4.tStart = t  # local t and not account for scr refresh
            One_Back_Example_Stim_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(One_Back_Example_Stim_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'One_Back_Example_Stim_4.started')
            # update status
            One_Back_Example_Stim_4.status = STARTED
            One_Back_Example_Stim_4.setAutoDraw(True)
        
        # if One_Back_Example_Stim_4 is active this frame...
        if One_Back_Example_Stim_4.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_8* updates
        
        # if Example_Stim_8 is starting this frame...
        if Example_Stim_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_8.frameNStart = frameN  # exact frame index
            Example_Stim_8.tStart = t  # local t and not account for scr refresh
            Example_Stim_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_8.started')
            # update status
            Example_Stim_8.status = STARTED
            Example_Stim_8.setAutoDraw(True)
        
        # if Example_Stim_8 is active this frame...
        if Example_Stim_8.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_8* updates
        
        # if Example_LeftScreenInstruction_8 is starting this frame...
        if Example_LeftScreenInstruction_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_8.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_8.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_8.started')
            # update status
            Example_LeftScreenInstruction_8.status = STARTED
            Example_LeftScreenInstruction_8.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_8 is active this frame...
        if Example_LeftScreenInstruction_8.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_8* updates
        
        # if Example_RightScreenInstruction_8 is starting this frame...
        if Example_RightScreenInstruction_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_8.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_8.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_8.started')
            # update status
            Example_RightScreenInstruction_8.status = STARTED
            Example_RightScreenInstruction_8.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_8 is active this frame...
        if Example_RightScreenInstruction_8.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions26,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions26.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions26.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions26" ---
    for thisComponent in Instructions26.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions26
    Instructions26.tStop = globalClock.getTime(format='float')
    Instructions26.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions26.stopped', Instructions26.tStop)
    # check responses
    if NextPage_20.keys in ['', [], None]:  # No response was made
        NextPage_20.keys = None
    thisExp.addData('NextPage_20.keys',NextPage_20.keys)
    if NextPage_20.keys != None:  # we had a response
        thisExp.addData('NextPage_20.rt', NextPage_20.rt)
        thisExp.addData('NextPage_20.duration', NextPage_20.duration)
    thisExp.nextEntry()
    # the Routine "Instructions26" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions34" ---
    # create an object to store info about Routine Instructions34
    Instructions34 = data.Routine(
        name='Instructions34',
        components=[NextPage_21, Instructions, Example_Stim_9, Example_LeftScreenInstruction_9, Example_RightScreenInstruction_9],
    )
    Instructions34.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_21
    NextPage_21.keys = []
    NextPage_21.rt = []
    _NextPage_21_allKeys = []
    Instructions.reset()
    Example_LeftScreenInstruction_9.reset()
    Example_LeftScreenInstruction_9.setText(leftScreenInstruction)
    Example_RightScreenInstruction_9.reset()
    Example_RightScreenInstruction_9.setText(rightScreenInstruction)
    # store start times for Instructions34
    Instructions34.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions34.tStart = globalClock.getTime(format='float')
    Instructions34.status = STARTED
    thisExp.addData('Instructions34.started', Instructions34.tStart)
    Instructions34.maxDuration = None
    # keep track of which components have finished
    Instructions34Components = Instructions34.components
    for thisComponent in Instructions34.components:
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
    
    # --- Run Routine "Instructions34" ---
    Instructions34.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_21* updates
        waitOnFlip = False
        
        # if NextPage_21 is starting this frame...
        if NextPage_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_21.frameNStart = frameN  # exact frame index
            NextPage_21.tStart = t  # local t and not account for scr refresh
            NextPage_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_21.started')
            # update status
            NextPage_21.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_21.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_21.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_21.getKeys(keyList=['space','left','right'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_21_allKeys.extend(theseKeys)
            if len(_NextPage_21_allKeys):
                NextPage_21.keys = _NextPage_21_allKeys[-1].name  # just the last key pressed
                NextPage_21.rt = _NextPage_21_allKeys[-1].rt
                NextPage_21.duration = _NextPage_21_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions* updates
        
        # if Instructions is starting this frame...
        if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions.frameNStart = frameN  # exact frame index
            Instructions.tStart = t  # local t and not account for scr refresh
            Instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions.started')
            # update status
            Instructions.status = STARTED
            Instructions.setAutoDraw(True)
        
        # if Instructions is active this frame...
        if Instructions.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_9* updates
        
        # if Example_Stim_9 is starting this frame...
        if Example_Stim_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_9.frameNStart = frameN  # exact frame index
            Example_Stim_9.tStart = t  # local t and not account for scr refresh
            Example_Stim_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_9.started')
            # update status
            Example_Stim_9.status = STARTED
            Example_Stim_9.setAutoDraw(True)
        
        # if Example_Stim_9 is active this frame...
        if Example_Stim_9.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_9* updates
        
        # if Example_LeftScreenInstruction_9 is starting this frame...
        if Example_LeftScreenInstruction_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_9.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_9.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_9.started')
            # update status
            Example_LeftScreenInstruction_9.status = STARTED
            Example_LeftScreenInstruction_9.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_9 is active this frame...
        if Example_LeftScreenInstruction_9.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_9* updates
        
        # if Example_RightScreenInstruction_9 is starting this frame...
        if Example_RightScreenInstruction_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_9.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_9.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_9.started')
            # update status
            Example_RightScreenInstruction_9.status = STARTED
            Example_RightScreenInstruction_9.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_9 is active this frame...
        if Example_RightScreenInstruction_9.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions34,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions34.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions34.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions34" ---
    for thisComponent in Instructions34.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions34
    Instructions34.tStop = globalClock.getTime(format='float')
    Instructions34.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions34.stopped', Instructions34.tStop)
    # check responses
    if NextPage_21.keys in ['', [], None]:  # No response was made
        NextPage_21.keys = None
    thisExp.addData('NextPage_21.keys',NextPage_21.keys)
    if NextPage_21.keys != None:  # we had a response
        thisExp.addData('NextPage_21.rt', NextPage_21.rt)
        thisExp.addData('NextPage_21.duration', NextPage_21.duration)
    thisExp.nextEntry()
    # the Routine "Instructions34" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions28" ---
    # create an object to store info about Routine Instructions28
    Instructions28 = data.Routine(
        name='Instructions28',
        components=[NextPage_22, Instructions_28, Two_Back_Example_Stim_3, One_Back_Example_Stim_5, Example_Stim_10, Example_LeftScreenInstruction_10, Example_RightScreenInstruction_10],
    )
    Instructions28.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_22
    NextPage_22.keys = []
    NextPage_22.rt = []
    _NextPage_22_allKeys = []
    Instructions_28.reset()
    Example_LeftScreenInstruction_10.reset()
    Example_LeftScreenInstruction_10.setText(leftScreenInstruction)
    Example_RightScreenInstruction_10.reset()
    Example_RightScreenInstruction_10.setText(rightScreenInstruction)
    # store start times for Instructions28
    Instructions28.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions28.tStart = globalClock.getTime(format='float')
    Instructions28.status = STARTED
    thisExp.addData('Instructions28.started', Instructions28.tStart)
    Instructions28.maxDuration = None
    # keep track of which components have finished
    Instructions28Components = Instructions28.components
    for thisComponent in Instructions28.components:
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
    
    # --- Run Routine "Instructions28" ---
    Instructions28.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_22* updates
        waitOnFlip = False
        
        # if NextPage_22 is starting this frame...
        if NextPage_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_22.frameNStart = frameN  # exact frame index
            NextPage_22.tStart = t  # local t and not account for scr refresh
            NextPage_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_22.started')
            # update status
            NextPage_22.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_22.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_22.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_22.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_22_allKeys.extend(theseKeys)
            if len(_NextPage_22_allKeys):
                NextPage_22.keys = _NextPage_22_allKeys[-1].name  # just the last key pressed
                NextPage_22.rt = _NextPage_22_allKeys[-1].rt
                NextPage_22.duration = _NextPage_22_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_28* updates
        
        # if Instructions_28 is starting this frame...
        if Instructions_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_28.frameNStart = frameN  # exact frame index
            Instructions_28.tStart = t  # local t and not account for scr refresh
            Instructions_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_28.started')
            # update status
            Instructions_28.status = STARTED
            Instructions_28.setAutoDraw(True)
        
        # if Instructions_28 is active this frame...
        if Instructions_28.status == STARTED:
            # update params
            pass
        
        # *Two_Back_Example_Stim_3* updates
        
        # if Two_Back_Example_Stim_3 is starting this frame...
        if Two_Back_Example_Stim_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Two_Back_Example_Stim_3.frameNStart = frameN  # exact frame index
            Two_Back_Example_Stim_3.tStart = t  # local t and not account for scr refresh
            Two_Back_Example_Stim_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Two_Back_Example_Stim_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Two_Back_Example_Stim_3.started')
            # update status
            Two_Back_Example_Stim_3.status = STARTED
            Two_Back_Example_Stim_3.setAutoDraw(True)
        
        # if Two_Back_Example_Stim_3 is active this frame...
        if Two_Back_Example_Stim_3.status == STARTED:
            # update params
            pass
        
        # *One_Back_Example_Stim_5* updates
        
        # if One_Back_Example_Stim_5 is starting this frame...
        if One_Back_Example_Stim_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            One_Back_Example_Stim_5.frameNStart = frameN  # exact frame index
            One_Back_Example_Stim_5.tStart = t  # local t and not account for scr refresh
            One_Back_Example_Stim_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(One_Back_Example_Stim_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'One_Back_Example_Stim_5.started')
            # update status
            One_Back_Example_Stim_5.status = STARTED
            One_Back_Example_Stim_5.setAutoDraw(True)
        
        # if One_Back_Example_Stim_5 is active this frame...
        if One_Back_Example_Stim_5.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_10* updates
        
        # if Example_Stim_10 is starting this frame...
        if Example_Stim_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_10.frameNStart = frameN  # exact frame index
            Example_Stim_10.tStart = t  # local t and not account for scr refresh
            Example_Stim_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_10.started')
            # update status
            Example_Stim_10.status = STARTED
            Example_Stim_10.setAutoDraw(True)
        
        # if Example_Stim_10 is active this frame...
        if Example_Stim_10.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_10* updates
        
        # if Example_LeftScreenInstruction_10 is starting this frame...
        if Example_LeftScreenInstruction_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_10.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_10.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_10.started')
            # update status
            Example_LeftScreenInstruction_10.status = STARTED
            Example_LeftScreenInstruction_10.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_10 is active this frame...
        if Example_LeftScreenInstruction_10.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_10* updates
        
        # if Example_RightScreenInstruction_10 is starting this frame...
        if Example_RightScreenInstruction_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_10.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_10.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_10.started')
            # update status
            Example_RightScreenInstruction_10.status = STARTED
            Example_RightScreenInstruction_10.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_10 is active this frame...
        if Example_RightScreenInstruction_10.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions28,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions28.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions28.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions28" ---
    for thisComponent in Instructions28.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions28
    Instructions28.tStop = globalClock.getTime(format='float')
    Instructions28.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions28.stopped', Instructions28.tStop)
    # check responses
    if NextPage_22.keys in ['', [], None]:  # No response was made
        NextPage_22.keys = None
    thisExp.addData('NextPage_22.keys',NextPage_22.keys)
    if NextPage_22.keys != None:  # we had a response
        thisExp.addData('NextPage_22.rt', NextPage_22.rt)
        thisExp.addData('NextPage_22.duration', NextPage_22.duration)
    thisExp.nextEntry()
    # the Routine "Instructions28" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_31" ---
    # create an object to store info about Routine Instructions_31
    Instructions_31 = data.Routine(
        name='Instructions_31',
        components=[NextPage_28, Instructions_4, Example_Stim_12, Example_LeftScreenInstruction_12, Example_RightScreenInstruction_12],
    )
    Instructions_31.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_28
    NextPage_28.keys = []
    NextPage_28.rt = []
    _NextPage_28_allKeys = []
    Instructions_4.reset()
    Example_LeftScreenInstruction_12.reset()
    Example_LeftScreenInstruction_12.setText(leftScreenInstruction)
    Example_RightScreenInstruction_12.reset()
    Example_RightScreenInstruction_12.setText(rightScreenInstruction)
    # store start times for Instructions_31
    Instructions_31.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_31.tStart = globalClock.getTime(format='float')
    Instructions_31.status = STARTED
    thisExp.addData('Instructions_31.started', Instructions_31.tStart)
    Instructions_31.maxDuration = None
    # keep track of which components have finished
    Instructions_31Components = Instructions_31.components
    for thisComponent in Instructions_31.components:
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
    
    # --- Run Routine "Instructions_31" ---
    Instructions_31.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_28* updates
        waitOnFlip = False
        
        # if NextPage_28 is starting this frame...
        if NextPage_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_28.frameNStart = frameN  # exact frame index
            NextPage_28.tStart = t  # local t and not account for scr refresh
            NextPage_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_28.started')
            # update status
            NextPage_28.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_28.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_28.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_28.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_28.getKeys(keyList=['space','left','right'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_28_allKeys.extend(theseKeys)
            if len(_NextPage_28_allKeys):
                NextPage_28.keys = _NextPage_28_allKeys[-1].name  # just the last key pressed
                NextPage_28.rt = _NextPage_28_allKeys[-1].rt
                NextPage_28.duration = _NextPage_28_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_4* updates
        
        # if Instructions_4 is starting this frame...
        if Instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_4.frameNStart = frameN  # exact frame index
            Instructions_4.tStart = t  # local t and not account for scr refresh
            Instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_4.started')
            # update status
            Instructions_4.status = STARTED
            Instructions_4.setAutoDraw(True)
        
        # if Instructions_4 is active this frame...
        if Instructions_4.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_12* updates
        
        # if Example_Stim_12 is starting this frame...
        if Example_Stim_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_12.frameNStart = frameN  # exact frame index
            Example_Stim_12.tStart = t  # local t and not account for scr refresh
            Example_Stim_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_12.started')
            # update status
            Example_Stim_12.status = STARTED
            Example_Stim_12.setAutoDraw(True)
        
        # if Example_Stim_12 is active this frame...
        if Example_Stim_12.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_12* updates
        
        # if Example_LeftScreenInstruction_12 is starting this frame...
        if Example_LeftScreenInstruction_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_12.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_12.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_12.started')
            # update status
            Example_LeftScreenInstruction_12.status = STARTED
            Example_LeftScreenInstruction_12.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_12 is active this frame...
        if Example_LeftScreenInstruction_12.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_12* updates
        
        # if Example_RightScreenInstruction_12 is starting this frame...
        if Example_RightScreenInstruction_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_12.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_12.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_12.started')
            # update status
            Example_RightScreenInstruction_12.status = STARTED
            Example_RightScreenInstruction_12.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_12 is active this frame...
        if Example_RightScreenInstruction_12.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions_31,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_31.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_31.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_31" ---
    for thisComponent in Instructions_31.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_31
    Instructions_31.tStop = globalClock.getTime(format='float')
    Instructions_31.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_31.stopped', Instructions_31.tStop)
    # check responses
    if NextPage_28.keys in ['', [], None]:  # No response was made
        NextPage_28.keys = None
    thisExp.addData('NextPage_28.keys',NextPage_28.keys)
    if NextPage_28.keys != None:  # we had a response
        thisExp.addData('NextPage_28.rt', NextPage_28.rt)
        thisExp.addData('NextPage_28.duration', NextPage_28.duration)
    thisExp.nextEntry()
    # the Routine "Instructions_31" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions29" ---
    # create an object to store info about Routine Instructions29
    Instructions29 = data.Routine(
        name='Instructions29',
        components=[NextPage_23, Instructions_29, Green_Border_2, Two_Back_Example_Stim_4, One_Back_Example_Stim_6, Example_Stim_11, Example_LeftScreenInstruction_11, Example_RightScreenInstruction_11],
    )
    Instructions29.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_23
    NextPage_23.keys = []
    NextPage_23.rt = []
    _NextPage_23_allKeys = []
    Instructions_29.reset()
    Example_LeftScreenInstruction_11.reset()
    Example_LeftScreenInstruction_11.setText(leftScreenInstruction)
    Example_RightScreenInstruction_11.reset()
    Example_RightScreenInstruction_11.setText(rightScreenInstruction)
    # store start times for Instructions29
    Instructions29.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions29.tStart = globalClock.getTime(format='float')
    Instructions29.status = STARTED
    thisExp.addData('Instructions29.started', Instructions29.tStart)
    Instructions29.maxDuration = None
    # keep track of which components have finished
    Instructions29Components = Instructions29.components
    for thisComponent in Instructions29.components:
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
    
    # --- Run Routine "Instructions29" ---
    Instructions29.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_23* updates
        waitOnFlip = False
        
        # if NextPage_23 is starting this frame...
        if NextPage_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_23.frameNStart = frameN  # exact frame index
            NextPage_23.tStart = t  # local t and not account for scr refresh
            NextPage_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_23.started')
            # update status
            NextPage_23.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_23.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_23.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_23.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_23_allKeys.extend(theseKeys)
            if len(_NextPage_23_allKeys):
                NextPage_23.keys = _NextPage_23_allKeys[-1].name  # just the last key pressed
                NextPage_23.rt = _NextPage_23_allKeys[-1].rt
                NextPage_23.duration = _NextPage_23_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_29* updates
        
        # if Instructions_29 is starting this frame...
        if Instructions_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_29.frameNStart = frameN  # exact frame index
            Instructions_29.tStart = t  # local t and not account for scr refresh
            Instructions_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_29.started')
            # update status
            Instructions_29.status = STARTED
            Instructions_29.setAutoDraw(True)
        
        # if Instructions_29 is active this frame...
        if Instructions_29.status == STARTED:
            # update params
            pass
        
        # *Green_Border_2* updates
        
        # if Green_Border_2 is starting this frame...
        if Green_Border_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Green_Border_2.frameNStart = frameN  # exact frame index
            Green_Border_2.tStart = t  # local t and not account for scr refresh
            Green_Border_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Green_Border_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Green_Border_2.started')
            # update status
            Green_Border_2.status = STARTED
            Green_Border_2.setAutoDraw(True)
        
        # if Green_Border_2 is active this frame...
        if Green_Border_2.status == STARTED:
            # update params
            pass
        
        # *Two_Back_Example_Stim_4* updates
        
        # if Two_Back_Example_Stim_4 is starting this frame...
        if Two_Back_Example_Stim_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Two_Back_Example_Stim_4.frameNStart = frameN  # exact frame index
            Two_Back_Example_Stim_4.tStart = t  # local t and not account for scr refresh
            Two_Back_Example_Stim_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Two_Back_Example_Stim_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Two_Back_Example_Stim_4.started')
            # update status
            Two_Back_Example_Stim_4.status = STARTED
            Two_Back_Example_Stim_4.setAutoDraw(True)
        
        # if Two_Back_Example_Stim_4 is active this frame...
        if Two_Back_Example_Stim_4.status == STARTED:
            # update params
            pass
        
        # *One_Back_Example_Stim_6* updates
        
        # if One_Back_Example_Stim_6 is starting this frame...
        if One_Back_Example_Stim_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            One_Back_Example_Stim_6.frameNStart = frameN  # exact frame index
            One_Back_Example_Stim_6.tStart = t  # local t and not account for scr refresh
            One_Back_Example_Stim_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(One_Back_Example_Stim_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'One_Back_Example_Stim_6.started')
            # update status
            One_Back_Example_Stim_6.status = STARTED
            One_Back_Example_Stim_6.setAutoDraw(True)
        
        # if One_Back_Example_Stim_6 is active this frame...
        if One_Back_Example_Stim_6.status == STARTED:
            # update params
            pass
        
        # *Example_Stim_11* updates
        
        # if Example_Stim_11 is starting this frame...
        if Example_Stim_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_Stim_11.frameNStart = frameN  # exact frame index
            Example_Stim_11.tStart = t  # local t and not account for scr refresh
            Example_Stim_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_Stim_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_Stim_11.started')
            # update status
            Example_Stim_11.status = STARTED
            Example_Stim_11.setAutoDraw(True)
        
        # if Example_Stim_11 is active this frame...
        if Example_Stim_11.status == STARTED:
            # update params
            pass
        
        # *Example_LeftScreenInstruction_11* updates
        
        # if Example_LeftScreenInstruction_11 is starting this frame...
        if Example_LeftScreenInstruction_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_LeftScreenInstruction_11.frameNStart = frameN  # exact frame index
            Example_LeftScreenInstruction_11.tStart = t  # local t and not account for scr refresh
            Example_LeftScreenInstruction_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_LeftScreenInstruction_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_LeftScreenInstruction_11.started')
            # update status
            Example_LeftScreenInstruction_11.status = STARTED
            Example_LeftScreenInstruction_11.setAutoDraw(True)
        
        # if Example_LeftScreenInstruction_11 is active this frame...
        if Example_LeftScreenInstruction_11.status == STARTED:
            # update params
            pass
        
        # *Example_RightScreenInstruction_11* updates
        
        # if Example_RightScreenInstruction_11 is starting this frame...
        if Example_RightScreenInstruction_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Example_RightScreenInstruction_11.frameNStart = frameN  # exact frame index
            Example_RightScreenInstruction_11.tStart = t  # local t and not account for scr refresh
            Example_RightScreenInstruction_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Example_RightScreenInstruction_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Example_RightScreenInstruction_11.started')
            # update status
            Example_RightScreenInstruction_11.status = STARTED
            Example_RightScreenInstruction_11.setAutoDraw(True)
        
        # if Example_RightScreenInstruction_11 is active this frame...
        if Example_RightScreenInstruction_11.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions29,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions29.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions29.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions29" ---
    for thisComponent in Instructions29.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions29
    Instructions29.tStop = globalClock.getTime(format='float')
    Instructions29.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions29.stopped', Instructions29.tStop)
    # check responses
    if NextPage_23.keys in ['', [], None]:  # No response was made
        NextPage_23.keys = None
    thisExp.addData('NextPage_23.keys',NextPage_23.keys)
    if NextPage_23.keys != None:  # we had a response
        thisExp.addData('NextPage_23.rt', NextPage_23.rt)
        thisExp.addData('NextPage_23.duration', NextPage_23.duration)
    thisExp.nextEntry()
    # the Routine "Instructions29" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions22" ---
    # create an object to store info about Routine Instructions22
    Instructions22 = data.Routine(
        name='Instructions22',
        components=[NextPage_24, Instructions_22],
    )
    Instructions22.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_24
    NextPage_24.keys = []
    NextPage_24.rt = []
    _NextPage_24_allKeys = []
    Instructions_22.reset()
    # store start times for Instructions22
    Instructions22.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions22.tStart = globalClock.getTime(format='float')
    Instructions22.status = STARTED
    thisExp.addData('Instructions22.started', Instructions22.tStart)
    Instructions22.maxDuration = None
    # keep track of which components have finished
    Instructions22Components = Instructions22.components
    for thisComponent in Instructions22.components:
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
    
    # --- Run Routine "Instructions22" ---
    Instructions22.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_24* updates
        waitOnFlip = False
        
        # if NextPage_24 is starting this frame...
        if NextPage_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_24.frameNStart = frameN  # exact frame index
            NextPage_24.tStart = t  # local t and not account for scr refresh
            NextPage_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_24.started')
            # update status
            NextPage_24.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_24.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_24.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_24.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_24_allKeys.extend(theseKeys)
            if len(_NextPage_24_allKeys):
                NextPage_24.keys = _NextPage_24_allKeys[-1].name  # just the last key pressed
                NextPage_24.rt = _NextPage_24_allKeys[-1].rt
                NextPage_24.duration = _NextPage_24_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_22* updates
        
        # if Instructions_22 is starting this frame...
        if Instructions_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_22.frameNStart = frameN  # exact frame index
            Instructions_22.tStart = t  # local t and not account for scr refresh
            Instructions_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_22.started')
            # update status
            Instructions_22.status = STARTED
            Instructions_22.setAutoDraw(True)
        
        # if Instructions_22 is active this frame...
        if Instructions_22.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions22,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions22.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions22.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions22" ---
    for thisComponent in Instructions22.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions22
    Instructions22.tStop = globalClock.getTime(format='float')
    Instructions22.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions22.stopped', Instructions22.tStop)
    # check responses
    if NextPage_24.keys in ['', [], None]:  # No response was made
        NextPage_24.keys = None
    thisExp.addData('NextPage_24.keys',NextPage_24.keys)
    if NextPage_24.keys != None:  # we had a response
        thisExp.addData('NextPage_24.rt', NextPage_24.rt)
        thisExp.addData('NextPage_24.duration', NextPage_24.duration)
    thisExp.nextEntry()
    # the Routine "Instructions22" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions30" ---
    # create an object to store info about Routine Instructions30
    Instructions30 = data.Routine(
        name='Instructions30',
        components=[NextPage_25, Instructions_30],
    )
    Instructions30.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_25
    NextPage_25.keys = []
    NextPage_25.rt = []
    _NextPage_25_allKeys = []
    Instructions_30.reset()
    # store start times for Instructions30
    Instructions30.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions30.tStart = globalClock.getTime(format='float')
    Instructions30.status = STARTED
    thisExp.addData('Instructions30.started', Instructions30.tStart)
    Instructions30.maxDuration = None
    # keep track of which components have finished
    Instructions30Components = Instructions30.components
    for thisComponent in Instructions30.components:
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
    
    # --- Run Routine "Instructions30" ---
    Instructions30.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_25* updates
        waitOnFlip = False
        
        # if NextPage_25 is starting this frame...
        if NextPage_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_25.frameNStart = frameN  # exact frame index
            NextPage_25.tStart = t  # local t and not account for scr refresh
            NextPage_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_25.started')
            # update status
            NextPage_25.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_25.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_25.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_25.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_25_allKeys.extend(theseKeys)
            if len(_NextPage_25_allKeys):
                NextPage_25.keys = _NextPage_25_allKeys[-1].name  # just the last key pressed
                NextPage_25.rt = _NextPage_25_allKeys[-1].rt
                NextPage_25.duration = _NextPage_25_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_30* updates
        
        # if Instructions_30 is starting this frame...
        if Instructions_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_30.frameNStart = frameN  # exact frame index
            Instructions_30.tStart = t  # local t and not account for scr refresh
            Instructions_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_30.started')
            # update status
            Instructions_30.status = STARTED
            Instructions_30.setAutoDraw(True)
        
        # if Instructions_30 is active this frame...
        if Instructions_30.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions30,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions30.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions30.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions30" ---
    for thisComponent in Instructions30.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions30
    Instructions30.tStop = globalClock.getTime(format='float')
    Instructions30.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions30.stopped', Instructions30.tStop)
    # check responses
    if NextPage_25.keys in ['', [], None]:  # No response was made
        NextPage_25.keys = None
    thisExp.addData('NextPage_25.keys',NextPage_25.keys)
    if NextPage_25.keys != None:  # we had a response
        thisExp.addData('NextPage_25.rt', NextPage_25.rt)
        thisExp.addData('NextPage_25.duration', NextPage_25.duration)
    thisExp.nextEntry()
    # the Routine "Instructions30" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop3 = data.TrialHandler2(
        name='practiceLoop3',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('PracticeTrials/PracticeTrials3.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practiceLoop3)  # add the loop to the experiment
    thisPracticeLoop3 = practiceLoop3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop3.rgb)
    if thisPracticeLoop3 != None:
        for paramName in thisPracticeLoop3:
            globals()[paramName] = thisPracticeLoop3[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeLoop3 in practiceLoop3:
        practiceLoop3.status = STARTED
        if hasattr(thisPracticeLoop3, 'status'):
            thisPracticeLoop3.status = STARTED
        currentLoop = practiceLoop3
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop3.rgb)
        if thisPracticeLoop3 != None:
            for paramName in thisPracticeLoop3:
                globals()[paramName] = thisPracticeLoop3[paramName]
        
        # --- Prepare to start Routine "PracticeTrial_Stim" ---
        # create an object to store info about Routine PracticeTrial_Stim
        PracticeTrial_Stim = data.Routine(
            name='PracticeTrial_Stim',
            components=[response, Stim, Stim_LeftScreenInstruction, Stim_RightScreenInstruction],
        )
        PracticeTrial_Stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from targetLogic
        # Decide correct key for this trial
        if TargetType == 'target':
            correctKey = matchKey
        else:
            correctKey = noMatchKey
        
        # create starting attributes for response
        response.keys = []
        response.rt = []
        _response_allKeys = []
        Stim.setImage(Stimulus)
        Stim_LeftScreenInstruction.reset()
        Stim_LeftScreenInstruction.setText(leftScreenInstruction)
        Stim_RightScreenInstruction.reset()
        Stim_RightScreenInstruction.setText(rightScreenInstruction)
        # store start times for PracticeTrial_Stim
        PracticeTrial_Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Stim.tStart = globalClock.getTime(format='float')
        PracticeTrial_Stim.status = STARTED
        thisExp.addData('PracticeTrial_Stim.started', PracticeTrial_Stim.tStart)
        PracticeTrial_Stim.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_StimComponents = PracticeTrial_Stim.components
        for thisComponent in PracticeTrial_Stim.components:
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
        
        # --- Run Routine "PracticeTrial_Stim" ---
        PracticeTrial_Stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop3, 'status') and thisPracticeLoop3.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = response.getKeys(keyList=[matchKey, noMatchKey], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # *Stim_LeftScreenInstruction* updates
            
            # if Stim_LeftScreenInstruction is starting this frame...
            if Stim_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_LeftScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.started')
                # update status
                Stim_LeftScreenInstruction.status = STARTED
                Stim_LeftScreenInstruction.setAutoDraw(True)
            
            # if Stim_LeftScreenInstruction is active this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_LeftScreenInstruction is stopping this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_LeftScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_LeftScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_LeftScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_LeftScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.stopped')
                    # update status
                    Stim_LeftScreenInstruction.status = FINISHED
                    Stim_LeftScreenInstruction.setAutoDraw(False)
            
            # *Stim_RightScreenInstruction* updates
            
            # if Stim_RightScreenInstruction is starting this frame...
            if Stim_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_RightScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.started')
                # update status
                Stim_RightScreenInstruction.status = STARTED
                Stim_RightScreenInstruction.setAutoDraw(True)
            
            # if Stim_RightScreenInstruction is active this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_RightScreenInstruction is stopping this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_RightScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_RightScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_RightScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_RightScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.stopped')
                    # update status
                    Stim_RightScreenInstruction.status = FINISHED
                    Stim_RightScreenInstruction.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Stim" ---
        for thisComponent in PracticeTrial_Stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Stim
        PracticeTrial_Stim.tStop = globalClock.getTime(format='float')
        PracticeTrial_Stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Stim.stopped', PracticeTrial_Stim.tStop)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceLoop3 (TrialHandler)
        practiceLoop3.addData('response.keys',response.keys)
        practiceLoop3.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceLoop3.addData('response.rt', response.rt)
            practiceLoop3.addData('response.duration', response.duration)
        # Run 'End Routine' code from feedbackLogic
        if response.keys is None:
            fbText = "No response."
            fbColor = 'yellow'
        elif response.corr:
            fbText = "Correct!"
            fbColor = 'limegreen'
        else:
            fbText = "Incorrect"
            fbColor = 'red'
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Stim.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Stim.maxDuration)
        elif PracticeTrial_Stim.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "PracticeTrial_Feedback" ---
        # create an object to store info about Routine PracticeTrial_Feedback
        PracticeTrial_Feedback = data.Routine(
            name='PracticeTrial_Feedback',
            components=[Fix, Feedback],
        )
        PracticeTrial_Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Fix.reset()
        Feedback.reset()
        Feedback.setColor(fbColor, colorSpace='rgb')
        Feedback.setText(fbText)
        # store start times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Feedback.tStart = globalClock.getTime(format='float')
        PracticeTrial_Feedback.status = STARTED
        thisExp.addData('PracticeTrial_Feedback.started', PracticeTrial_Feedback.tStart)
        PracticeTrial_Feedback.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_FeedbackComponents = PracticeTrial_Feedback.components
        for thisComponent in PracticeTrial_Feedback.components:
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
        
        # --- Run Routine "PracticeTrial_Feedback" ---
        PracticeTrial_Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop3, 'status') and thisPracticeLoop3.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # *Feedback* updates
            
            # if Feedback is starting this frame...
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                # update status
                Feedback.status = STARTED
                Feedback.setAutoDraw(True)
            
            # if Feedback is active this frame...
            if Feedback.status == STARTED:
                # update params
                pass
            
            # if Feedback is stopping this frame...
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    # update status
                    Feedback.status = FINISHED
                    Feedback.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Feedback" ---
        for thisComponent in PracticeTrial_Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStop = globalClock.getTime(format='float')
        PracticeTrial_Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Feedback.stopped', PracticeTrial_Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Feedback.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Feedback.maxDuration)
        elif PracticeTrial_Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeLoop3 as finished
        if hasattr(thisPracticeLoop3, 'status'):
            thisPracticeLoop3.status = FINISHED
        # if awaiting a pause, pause now
        if practiceLoop3.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceLoop3.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practiceLoop3'
    practiceLoop3.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "InstructionsSpaceToContinue" ---
    # create an object to store info about Routine InstructionsSpaceToContinue
    InstructionsSpaceToContinue = data.Routine(
        name='InstructionsSpaceToContinue',
        components=[NextPage_9, Instructions_Space],
    )
    InstructionsSpaceToContinue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_9
    NextPage_9.keys = []
    NextPage_9.rt = []
    _NextPage_9_allKeys = []
    Instructions_Space.reset()
    # store start times for InstructionsSpaceToContinue
    InstructionsSpaceToContinue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    InstructionsSpaceToContinue.tStart = globalClock.getTime(format='float')
    InstructionsSpaceToContinue.status = STARTED
    thisExp.addData('InstructionsSpaceToContinue.started', InstructionsSpaceToContinue.tStart)
    InstructionsSpaceToContinue.maxDuration = None
    # keep track of which components have finished
    InstructionsSpaceToContinueComponents = InstructionsSpaceToContinue.components
    for thisComponent in InstructionsSpaceToContinue.components:
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
    
    # --- Run Routine "InstructionsSpaceToContinue" ---
    InstructionsSpaceToContinue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_9* updates
        waitOnFlip = False
        
        # if NextPage_9 is starting this frame...
        if NextPage_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_9.frameNStart = frameN  # exact frame index
            NextPage_9.tStart = t  # local t and not account for scr refresh
            NextPage_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_9.started')
            # update status
            NextPage_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_9.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_9_allKeys.extend(theseKeys)
            if len(_NextPage_9_allKeys):
                NextPage_9.keys = _NextPage_9_allKeys[-1].name  # just the last key pressed
                NextPage_9.rt = _NextPage_9_allKeys[-1].rt
                NextPage_9.duration = _NextPage_9_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_Space* updates
        
        # if Instructions_Space is starting this frame...
        if Instructions_Space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_Space.frameNStart = frameN  # exact frame index
            Instructions_Space.tStart = t  # local t and not account for scr refresh
            Instructions_Space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_Space, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_Space.started')
            # update status
            Instructions_Space.status = STARTED
            Instructions_Space.setAutoDraw(True)
        
        # if Instructions_Space is active this frame...
        if Instructions_Space.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=InstructionsSpaceToContinue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            InstructionsSpaceToContinue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsSpaceToContinue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionsSpaceToContinue" ---
    for thisComponent in InstructionsSpaceToContinue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for InstructionsSpaceToContinue
    InstructionsSpaceToContinue.tStop = globalClock.getTime(format='float')
    InstructionsSpaceToContinue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('InstructionsSpaceToContinue.stopped', InstructionsSpaceToContinue.tStop)
    # check responses
    if NextPage_9.keys in ['', [], None]:  # No response was made
        NextPage_9.keys = None
    thisExp.addData('NextPage_9.keys',NextPage_9.keys)
    if NextPage_9.keys != None:  # we had a response
        thisExp.addData('NextPage_9.rt', NextPage_9.rt)
        thisExp.addData('NextPage_9.duration', NextPage_9.duration)
    thisExp.nextEntry()
    # the Routine "InstructionsSpaceToContinue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop4 = data.TrialHandler2(
        name='practiceLoop4',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('PracticeTrials/PracticeTrials4.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practiceLoop4)  # add the loop to the experiment
    thisPracticeLoop4 = practiceLoop4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop4.rgb)
    if thisPracticeLoop4 != None:
        for paramName in thisPracticeLoop4:
            globals()[paramName] = thisPracticeLoop4[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeLoop4 in practiceLoop4:
        practiceLoop4.status = STARTED
        if hasattr(thisPracticeLoop4, 'status'):
            thisPracticeLoop4.status = STARTED
        currentLoop = practiceLoop4
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop4.rgb)
        if thisPracticeLoop4 != None:
            for paramName in thisPracticeLoop4:
                globals()[paramName] = thisPracticeLoop4[paramName]
        
        # --- Prepare to start Routine "PracticeTrial_Stim" ---
        # create an object to store info about Routine PracticeTrial_Stim
        PracticeTrial_Stim = data.Routine(
            name='PracticeTrial_Stim',
            components=[response, Stim, Stim_LeftScreenInstruction, Stim_RightScreenInstruction],
        )
        PracticeTrial_Stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from targetLogic
        # Decide correct key for this trial
        if TargetType == 'target':
            correctKey = matchKey
        else:
            correctKey = noMatchKey
        
        # create starting attributes for response
        response.keys = []
        response.rt = []
        _response_allKeys = []
        Stim.setImage(Stimulus)
        Stim_LeftScreenInstruction.reset()
        Stim_LeftScreenInstruction.setText(leftScreenInstruction)
        Stim_RightScreenInstruction.reset()
        Stim_RightScreenInstruction.setText(rightScreenInstruction)
        # store start times for PracticeTrial_Stim
        PracticeTrial_Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Stim.tStart = globalClock.getTime(format='float')
        PracticeTrial_Stim.status = STARTED
        thisExp.addData('PracticeTrial_Stim.started', PracticeTrial_Stim.tStart)
        PracticeTrial_Stim.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_StimComponents = PracticeTrial_Stim.components
        for thisComponent in PracticeTrial_Stim.components:
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
        
        # --- Run Routine "PracticeTrial_Stim" ---
        PracticeTrial_Stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop4, 'status') and thisPracticeLoop4.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = response.getKeys(keyList=[matchKey, noMatchKey], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # *Stim_LeftScreenInstruction* updates
            
            # if Stim_LeftScreenInstruction is starting this frame...
            if Stim_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_LeftScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.started')
                # update status
                Stim_LeftScreenInstruction.status = STARTED
                Stim_LeftScreenInstruction.setAutoDraw(True)
            
            # if Stim_LeftScreenInstruction is active this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_LeftScreenInstruction is stopping this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_LeftScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_LeftScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_LeftScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_LeftScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.stopped')
                    # update status
                    Stim_LeftScreenInstruction.status = FINISHED
                    Stim_LeftScreenInstruction.setAutoDraw(False)
            
            # *Stim_RightScreenInstruction* updates
            
            # if Stim_RightScreenInstruction is starting this frame...
            if Stim_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_RightScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.started')
                # update status
                Stim_RightScreenInstruction.status = STARTED
                Stim_RightScreenInstruction.setAutoDraw(True)
            
            # if Stim_RightScreenInstruction is active this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_RightScreenInstruction is stopping this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_RightScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_RightScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_RightScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_RightScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.stopped')
                    # update status
                    Stim_RightScreenInstruction.status = FINISHED
                    Stim_RightScreenInstruction.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Stim" ---
        for thisComponent in PracticeTrial_Stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Stim
        PracticeTrial_Stim.tStop = globalClock.getTime(format='float')
        PracticeTrial_Stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Stim.stopped', PracticeTrial_Stim.tStop)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceLoop4 (TrialHandler)
        practiceLoop4.addData('response.keys',response.keys)
        practiceLoop4.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceLoop4.addData('response.rt', response.rt)
            practiceLoop4.addData('response.duration', response.duration)
        # Run 'End Routine' code from feedbackLogic
        if response.keys is None:
            fbText = "No response."
            fbColor = 'yellow'
        elif response.corr:
            fbText = "Correct!"
            fbColor = 'limegreen'
        else:
            fbText = "Incorrect"
            fbColor = 'red'
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Stim.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Stim.maxDuration)
        elif PracticeTrial_Stim.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "PracticeTrial_Feedback" ---
        # create an object to store info about Routine PracticeTrial_Feedback
        PracticeTrial_Feedback = data.Routine(
            name='PracticeTrial_Feedback',
            components=[Fix, Feedback],
        )
        PracticeTrial_Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Fix.reset()
        Feedback.reset()
        Feedback.setColor(fbColor, colorSpace='rgb')
        Feedback.setText(fbText)
        # store start times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Feedback.tStart = globalClock.getTime(format='float')
        PracticeTrial_Feedback.status = STARTED
        thisExp.addData('PracticeTrial_Feedback.started', PracticeTrial_Feedback.tStart)
        PracticeTrial_Feedback.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_FeedbackComponents = PracticeTrial_Feedback.components
        for thisComponent in PracticeTrial_Feedback.components:
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
        
        # --- Run Routine "PracticeTrial_Feedback" ---
        PracticeTrial_Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop4, 'status') and thisPracticeLoop4.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # *Feedback* updates
            
            # if Feedback is starting this frame...
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                # update status
                Feedback.status = STARTED
                Feedback.setAutoDraw(True)
            
            # if Feedback is active this frame...
            if Feedback.status == STARTED:
                # update params
                pass
            
            # if Feedback is stopping this frame...
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    # update status
                    Feedback.status = FINISHED
                    Feedback.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Feedback" ---
        for thisComponent in PracticeTrial_Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStop = globalClock.getTime(format='float')
        PracticeTrial_Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Feedback.stopped', PracticeTrial_Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Feedback.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Feedback.maxDuration)
        elif PracticeTrial_Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeLoop4 as finished
        if hasattr(thisPracticeLoop4, 'status'):
            thisPracticeLoop4.status = FINISHED
        # if awaiting a pause, pause now
        if practiceLoop4.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceLoop4.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practiceLoop4'
    practiceLoop4.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Instructions36" ---
    # create an object to store info about Routine Instructions36
    Instructions36 = data.Routine(
        name='Instructions36',
        components=[NextPage_26, Instructions_36, magenta_fixcross, Instructions_37],
    )
    Instructions36.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_26
    NextPage_26.keys = []
    NextPage_26.rt = []
    _NextPage_26_allKeys = []
    Instructions_36.reset()
    magenta_fixcross.reset()
    Instructions_37.reset()
    # store start times for Instructions36
    Instructions36.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions36.tStart = globalClock.getTime(format='float')
    Instructions36.status = STARTED
    thisExp.addData('Instructions36.started', Instructions36.tStart)
    Instructions36.maxDuration = None
    # keep track of which components have finished
    Instructions36Components = Instructions36.components
    for thisComponent in Instructions36.components:
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
    
    # --- Run Routine "Instructions36" ---
    Instructions36.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NextPage_26* updates
        waitOnFlip = False
        
        # if NextPage_26 is starting this frame...
        if NextPage_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_26.frameNStart = frameN  # exact frame index
            NextPage_26.tStart = t  # local t and not account for scr refresh
            NextPage_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_26.started')
            # update status
            NextPage_26.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_26.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_26.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_26.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_26_allKeys.extend(theseKeys)
            if len(_NextPage_26_allKeys):
                NextPage_26.keys = _NextPage_26_allKeys[-1].name  # just the last key pressed
                NextPage_26.rt = _NextPage_26_allKeys[-1].rt
                NextPage_26.duration = _NextPage_26_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_36* updates
        
        # if Instructions_36 is starting this frame...
        if Instructions_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_36.frameNStart = frameN  # exact frame index
            Instructions_36.tStart = t  # local t and not account for scr refresh
            Instructions_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_36, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_36.started')
            # update status
            Instructions_36.status = STARTED
            Instructions_36.setAutoDraw(True)
        
        # if Instructions_36 is active this frame...
        if Instructions_36.status == STARTED:
            # update params
            pass
        
        # *magenta_fixcross* updates
        
        # if magenta_fixcross is starting this frame...
        if magenta_fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            magenta_fixcross.frameNStart = frameN  # exact frame index
            magenta_fixcross.tStart = t  # local t and not account for scr refresh
            magenta_fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(magenta_fixcross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'magenta_fixcross.started')
            # update status
            magenta_fixcross.status = STARTED
            magenta_fixcross.setAutoDraw(True)
        
        # if magenta_fixcross is active this frame...
        if magenta_fixcross.status == STARTED:
            # update params
            pass
        
        # *Instructions_37* updates
        
        # if Instructions_37 is starting this frame...
        if Instructions_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_37.frameNStart = frameN  # exact frame index
            Instructions_37.tStart = t  # local t and not account for scr refresh
            Instructions_37.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_37, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_37.started')
            # update status
            Instructions_37.status = STARTED
            Instructions_37.setAutoDraw(True)
        
        # if Instructions_37 is active this frame...
        if Instructions_37.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions36,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions36.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions36.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions36" ---
    for thisComponent in Instructions36.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions36
    Instructions36.tStop = globalClock.getTime(format='float')
    Instructions36.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions36.stopped', Instructions36.tStop)
    # check responses
    if NextPage_26.keys in ['', [], None]:  # No response was made
        NextPage_26.keys = None
    thisExp.addData('NextPage_26.keys',NextPage_26.keys)
    if NextPage_26.keys != None:  # we had a response
        thisExp.addData('NextPage_26.rt', NextPage_26.rt)
        thisExp.addData('NextPage_26.duration', NextPage_26.duration)
    thisExp.nextEntry()
    # the Routine "Instructions36" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_5" ---
    # create an object to store info about Routine Instructions_5
    Instructions_5 = data.Routine(
        name='Instructions_5',
        components=[NextPage_29, Instructions_38],
    )
    Instructions_5.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for NextPage_29
    NextPage_29.keys = []
    NextPage_29.rt = []
    _NextPage_29_allKeys = []
    Instructions_38.reset()
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
        
        # *NextPage_29* updates
        waitOnFlip = False
        
        # if NextPage_29 is starting this frame...
        if NextPage_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NextPage_29.frameNStart = frameN  # exact frame index
            NextPage_29.tStart = t  # local t and not account for scr refresh
            NextPage_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NextPage_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NextPage_29.started')
            # update status
            NextPage_29.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(NextPage_29.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(NextPage_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if NextPage_29.status == STARTED and not waitOnFlip:
            theseKeys = NextPage_29.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _NextPage_29_allKeys.extend(theseKeys)
            if len(_NextPage_29_allKeys):
                NextPage_29.keys = _NextPage_29_allKeys[-1].name  # just the last key pressed
                NextPage_29.rt = _NextPage_29_allKeys[-1].rt
                NextPage_29.duration = _NextPage_29_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Instructions_38* updates
        
        # if Instructions_38 is starting this frame...
        if Instructions_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_38.frameNStart = frameN  # exact frame index
            Instructions_38.tStart = t  # local t and not account for scr refresh
            Instructions_38.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_38, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_38.started')
            # update status
            Instructions_38.status = STARTED
            Instructions_38.setAutoDraw(True)
        
        # if Instructions_38 is active this frame...
        if Instructions_38.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Instructions_5,
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
    if NextPage_29.keys in ['', [], None]:  # No response was made
        NextPage_29.keys = None
    thisExp.addData('NextPage_29.keys',NextPage_29.keys)
    if NextPage_29.keys != None:  # we had a response
        thisExp.addData('NextPage_29.rt', NextPage_29.rt)
        thisExp.addData('NextPage_29.duration', NextPage_29.duration)
    thisExp.nextEntry()
    # the Routine "Instructions_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "PracticeTrial5_Cue" ---
    # create an object to store info about Routine PracticeTrial5_Cue
    PracticeTrial5_Cue = data.Routine(
        name='PracticeTrial5_Cue',
        components=[CueFix_5, Cue_2Back],
    )
    PracticeTrial5_Cue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    CueFix_5.reset()
    Cue_2Back.reset()
    # store start times for PracticeTrial5_Cue
    PracticeTrial5_Cue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PracticeTrial5_Cue.tStart = globalClock.getTime(format='float')
    PracticeTrial5_Cue.status = STARTED
    thisExp.addData('PracticeTrial5_Cue.started', PracticeTrial5_Cue.tStart)
    PracticeTrial5_Cue.maxDuration = None
    # keep track of which components have finished
    PracticeTrial5_CueComponents = PracticeTrial5_Cue.components
    for thisComponent in PracticeTrial5_Cue.components:
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
    
    # --- Run Routine "PracticeTrial5_Cue" ---
    PracticeTrial5_Cue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CueFix_5* updates
        
        # if CueFix_5 is starting this frame...
        if CueFix_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CueFix_5.frameNStart = frameN  # exact frame index
            CueFix_5.tStart = t  # local t and not account for scr refresh
            CueFix_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueFix_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueFix_5.started')
            # update status
            CueFix_5.status = STARTED
            CueFix_5.setAutoDraw(True)
        
        # if CueFix_5 is active this frame...
        if CueFix_5.status == STARTED:
            # update params
            pass
        
        # if CueFix_5 is stopping this frame...
        if CueFix_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueFix_5.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                CueFix_5.tStop = t  # not accounting for scr refresh
                CueFix_5.tStopRefresh = tThisFlipGlobal  # on global time
                CueFix_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueFix_5.stopped')
                # update status
                CueFix_5.status = FINISHED
                CueFix_5.setAutoDraw(False)
        
        # *Cue_2Back* updates
        
        # if Cue_2Back is starting this frame...
        if Cue_2Back.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
            if tThisFlipGlobal > Cue_2Back.tStartRefresh + 2-frameTolerance:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=PracticeTrial5_Cue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PracticeTrial5_Cue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrial5_Cue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PracticeTrial5_Cue" ---
    for thisComponent in PracticeTrial5_Cue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PracticeTrial5_Cue
    PracticeTrial5_Cue.tStop = globalClock.getTime(format='float')
    PracticeTrial5_Cue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PracticeTrial5_Cue.stopped', PracticeTrial5_Cue.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if PracticeTrial5_Cue.maxDurationReached:
        routineTimer.addTime(-PracticeTrial5_Cue.maxDuration)
    elif PracticeTrial5_Cue.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop5 = data.TrialHandler2(
        name='practiceLoop5',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('PracticeTrials/PracticeTrials5.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practiceLoop5)  # add the loop to the experiment
    thisPracticeLoop5 = practiceLoop5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop5.rgb)
    if thisPracticeLoop5 != None:
        for paramName in thisPracticeLoop5:
            globals()[paramName] = thisPracticeLoop5[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeLoop5 in practiceLoop5:
        practiceLoop5.status = STARTED
        if hasattr(thisPracticeLoop5, 'status'):
            thisPracticeLoop5.status = STARTED
        currentLoop = practiceLoop5
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop5.rgb)
        if thisPracticeLoop5 != None:
            for paramName in thisPracticeLoop5:
                globals()[paramName] = thisPracticeLoop5[paramName]
        
        # --- Prepare to start Routine "PracticeTrial_Stim" ---
        # create an object to store info about Routine PracticeTrial_Stim
        PracticeTrial_Stim = data.Routine(
            name='PracticeTrial_Stim',
            components=[response, Stim, Stim_LeftScreenInstruction, Stim_RightScreenInstruction],
        )
        PracticeTrial_Stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from targetLogic
        # Decide correct key for this trial
        if TargetType == 'target':
            correctKey = matchKey
        else:
            correctKey = noMatchKey
        
        # create starting attributes for response
        response.keys = []
        response.rt = []
        _response_allKeys = []
        Stim.setImage(Stimulus)
        Stim_LeftScreenInstruction.reset()
        Stim_LeftScreenInstruction.setText(leftScreenInstruction)
        Stim_RightScreenInstruction.reset()
        Stim_RightScreenInstruction.setText(rightScreenInstruction)
        # store start times for PracticeTrial_Stim
        PracticeTrial_Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Stim.tStart = globalClock.getTime(format='float')
        PracticeTrial_Stim.status = STARTED
        thisExp.addData('PracticeTrial_Stim.started', PracticeTrial_Stim.tStart)
        PracticeTrial_Stim.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_StimComponents = PracticeTrial_Stim.components
        for thisComponent in PracticeTrial_Stim.components:
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
        
        # --- Run Routine "PracticeTrial_Stim" ---
        PracticeTrial_Stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop5, 'status') and thisPracticeLoop5.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = response.getKeys(keyList=[matchKey, noMatchKey], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # *Stim_LeftScreenInstruction* updates
            
            # if Stim_LeftScreenInstruction is starting this frame...
            if Stim_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_LeftScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.started')
                # update status
                Stim_LeftScreenInstruction.status = STARTED
                Stim_LeftScreenInstruction.setAutoDraw(True)
            
            # if Stim_LeftScreenInstruction is active this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_LeftScreenInstruction is stopping this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_LeftScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_LeftScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_LeftScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_LeftScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.stopped')
                    # update status
                    Stim_LeftScreenInstruction.status = FINISHED
                    Stim_LeftScreenInstruction.setAutoDraw(False)
            
            # *Stim_RightScreenInstruction* updates
            
            # if Stim_RightScreenInstruction is starting this frame...
            if Stim_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_RightScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.started')
                # update status
                Stim_RightScreenInstruction.status = STARTED
                Stim_RightScreenInstruction.setAutoDraw(True)
            
            # if Stim_RightScreenInstruction is active this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_RightScreenInstruction is stopping this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_RightScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_RightScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_RightScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_RightScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.stopped')
                    # update status
                    Stim_RightScreenInstruction.status = FINISHED
                    Stim_RightScreenInstruction.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Stim" ---
        for thisComponent in PracticeTrial_Stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Stim
        PracticeTrial_Stim.tStop = globalClock.getTime(format='float')
        PracticeTrial_Stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Stim.stopped', PracticeTrial_Stim.tStop)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceLoop5 (TrialHandler)
        practiceLoop5.addData('response.keys',response.keys)
        practiceLoop5.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceLoop5.addData('response.rt', response.rt)
            practiceLoop5.addData('response.duration', response.duration)
        # Run 'End Routine' code from feedbackLogic
        if response.keys is None:
            fbText = "No response."
            fbColor = 'yellow'
        elif response.corr:
            fbText = "Correct!"
            fbColor = 'limegreen'
        else:
            fbText = "Incorrect"
            fbColor = 'red'
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Stim.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Stim.maxDuration)
        elif PracticeTrial_Stim.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "PracticeTrial_Feedback" ---
        # create an object to store info about Routine PracticeTrial_Feedback
        PracticeTrial_Feedback = data.Routine(
            name='PracticeTrial_Feedback',
            components=[Fix, Feedback],
        )
        PracticeTrial_Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Fix.reset()
        Feedback.reset()
        Feedback.setColor(fbColor, colorSpace='rgb')
        Feedback.setText(fbText)
        # store start times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Feedback.tStart = globalClock.getTime(format='float')
        PracticeTrial_Feedback.status = STARTED
        thisExp.addData('PracticeTrial_Feedback.started', PracticeTrial_Feedback.tStart)
        PracticeTrial_Feedback.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_FeedbackComponents = PracticeTrial_Feedback.components
        for thisComponent in PracticeTrial_Feedback.components:
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
        
        # --- Run Routine "PracticeTrial_Feedback" ---
        PracticeTrial_Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop5, 'status') and thisPracticeLoop5.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # *Feedback* updates
            
            # if Feedback is starting this frame...
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                # update status
                Feedback.status = STARTED
                Feedback.setAutoDraw(True)
            
            # if Feedback is active this frame...
            if Feedback.status == STARTED:
                # update params
                pass
            
            # if Feedback is stopping this frame...
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    # update status
                    Feedback.status = FINISHED
                    Feedback.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Feedback" ---
        for thisComponent in PracticeTrial_Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStop = globalClock.getTime(format='float')
        PracticeTrial_Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Feedback.stopped', PracticeTrial_Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Feedback.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Feedback.maxDuration)
        elif PracticeTrial_Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeLoop5 as finished
        if hasattr(thisPracticeLoop5, 'status'):
            thisPracticeLoop5.status = FINISHED
        # if awaiting a pause, pause now
        if practiceLoop5.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceLoop5.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practiceLoop5'
    practiceLoop5.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "PracticeTrial6_Cue" ---
    # create an object to store info about Routine PracticeTrial6_Cue
    PracticeTrial6_Cue = data.Routine(
        name='PracticeTrial6_Cue',
        components=[CueFix_6, CueTarget_6, CueTargetImage_6, Zero_back_3],
    )
    PracticeTrial6_Cue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    CueFix_6.reset()
    CueTarget_6.reset()
    Zero_back_3.reset()
    # store start times for PracticeTrial6_Cue
    PracticeTrial6_Cue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PracticeTrial6_Cue.tStart = globalClock.getTime(format='float')
    PracticeTrial6_Cue.status = STARTED
    thisExp.addData('PracticeTrial6_Cue.started', PracticeTrial6_Cue.tStart)
    PracticeTrial6_Cue.maxDuration = None
    # keep track of which components have finished
    PracticeTrial6_CueComponents = PracticeTrial6_Cue.components
    for thisComponent in PracticeTrial6_Cue.components:
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
    
    # --- Run Routine "PracticeTrial6_Cue" ---
    PracticeTrial6_Cue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CueFix_6* updates
        
        # if CueFix_6 is starting this frame...
        if CueFix_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CueFix_6.frameNStart = frameN  # exact frame index
            CueFix_6.tStart = t  # local t and not account for scr refresh
            CueFix_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueFix_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueFix_6.started')
            # update status
            CueFix_6.status = STARTED
            CueFix_6.setAutoDraw(True)
        
        # if CueFix_6 is active this frame...
        if CueFix_6.status == STARTED:
            # update params
            pass
        
        # if CueFix_6 is stopping this frame...
        if CueFix_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueFix_6.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                CueFix_6.tStop = t  # not accounting for scr refresh
                CueFix_6.tStopRefresh = tThisFlipGlobal  # on global time
                CueFix_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueFix_6.stopped')
                # update status
                CueFix_6.status = FINISHED
                CueFix_6.setAutoDraw(False)
        
        # *CueTarget_6* updates
        
        # if CueTarget_6 is starting this frame...
        if CueTarget_6.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            CueTarget_6.frameNStart = frameN  # exact frame index
            CueTarget_6.tStart = t  # local t and not account for scr refresh
            CueTarget_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueTarget_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueTarget_6.started')
            # update status
            CueTarget_6.status = STARTED
            CueTarget_6.setAutoDraw(True)
        
        # if CueTarget_6 is active this frame...
        if CueTarget_6.status == STARTED:
            # update params
            pass
        
        # if CueTarget_6 is stopping this frame...
        if CueTarget_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueTarget_6.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                CueTarget_6.tStop = t  # not accounting for scr refresh
                CueTarget_6.tStopRefresh = tThisFlipGlobal  # on global time
                CueTarget_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueTarget_6.stopped')
                # update status
                CueTarget_6.status = FINISHED
                CueTarget_6.setAutoDraw(False)
        
        # *CueTargetImage_6* updates
        
        # if CueTargetImage_6 is starting this frame...
        if CueTargetImage_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            CueTargetImage_6.frameNStart = frameN  # exact frame index
            CueTargetImage_6.tStart = t  # local t and not account for scr refresh
            CueTargetImage_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueTargetImage_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueTargetImage_6.started')
            # update status
            CueTargetImage_6.status = STARTED
            CueTargetImage_6.setAutoDraw(True)
        
        # if CueTargetImage_6 is active this frame...
        if CueTargetImage_6.status == STARTED:
            # update params
            pass
        
        # if CueTargetImage_6 is stopping this frame...
        if CueTargetImage_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueTargetImage_6.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                CueTargetImage_6.tStop = t  # not accounting for scr refresh
                CueTargetImage_6.tStopRefresh = tThisFlipGlobal  # on global time
                CueTargetImage_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueTargetImage_6.stopped')
                # update status
                CueTargetImage_6.status = FINISHED
                CueTargetImage_6.setAutoDraw(False)
        
        # *Zero_back_3* updates
        
        # if Zero_back_3 is starting this frame...
        if Zero_back_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Zero_back_3.frameNStart = frameN  # exact frame index
            Zero_back_3.tStart = t  # local t and not account for scr refresh
            Zero_back_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Zero_back_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Zero_back_3.started')
            # update status
            Zero_back_3.status = STARTED
            Zero_back_3.setAutoDraw(True)
        
        # if Zero_back_3 is active this frame...
        if Zero_back_3.status == STARTED:
            # update params
            pass
        
        # if Zero_back_3 is stopping this frame...
        if Zero_back_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Zero_back_3.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Zero_back_3.tStop = t  # not accounting for scr refresh
                Zero_back_3.tStopRefresh = tThisFlipGlobal  # on global time
                Zero_back_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Zero_back_3.stopped')
                # update status
                Zero_back_3.status = FINISHED
                Zero_back_3.setAutoDraw(False)
        
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
                timers=[routineTimer, globalClock], 
                currentRoutine=PracticeTrial6_Cue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PracticeTrial6_Cue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrial6_Cue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PracticeTrial6_Cue" ---
    for thisComponent in PracticeTrial6_Cue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PracticeTrial6_Cue
    PracticeTrial6_Cue.tStop = globalClock.getTime(format='float')
    PracticeTrial6_Cue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PracticeTrial6_Cue.stopped', PracticeTrial6_Cue.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if PracticeTrial6_Cue.maxDurationReached:
        routineTimer.addTime(-PracticeTrial6_Cue.maxDuration)
    elif PracticeTrial6_Cue.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop6 = data.TrialHandler2(
        name='practiceLoop6',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('PracticeTrials/PracticeTrials6.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practiceLoop6)  # add the loop to the experiment
    thisPracticeLoop6 = practiceLoop6.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop6.rgb)
    if thisPracticeLoop6 != None:
        for paramName in thisPracticeLoop6:
            globals()[paramName] = thisPracticeLoop6[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeLoop6 in practiceLoop6:
        practiceLoop6.status = STARTED
        if hasattr(thisPracticeLoop6, 'status'):
            thisPracticeLoop6.status = STARTED
        currentLoop = practiceLoop6
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop6.rgb)
        if thisPracticeLoop6 != None:
            for paramName in thisPracticeLoop6:
                globals()[paramName] = thisPracticeLoop6[paramName]
        
        # --- Prepare to start Routine "PracticeTrial_Stim" ---
        # create an object to store info about Routine PracticeTrial_Stim
        PracticeTrial_Stim = data.Routine(
            name='PracticeTrial_Stim',
            components=[response, Stim, Stim_LeftScreenInstruction, Stim_RightScreenInstruction],
        )
        PracticeTrial_Stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from targetLogic
        # Decide correct key for this trial
        if TargetType == 'target':
            correctKey = matchKey
        else:
            correctKey = noMatchKey
        
        # create starting attributes for response
        response.keys = []
        response.rt = []
        _response_allKeys = []
        Stim.setImage(Stimulus)
        Stim_LeftScreenInstruction.reset()
        Stim_LeftScreenInstruction.setText(leftScreenInstruction)
        Stim_RightScreenInstruction.reset()
        Stim_RightScreenInstruction.setText(rightScreenInstruction)
        # store start times for PracticeTrial_Stim
        PracticeTrial_Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Stim.tStart = globalClock.getTime(format='float')
        PracticeTrial_Stim.status = STARTED
        thisExp.addData('PracticeTrial_Stim.started', PracticeTrial_Stim.tStart)
        PracticeTrial_Stim.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_StimComponents = PracticeTrial_Stim.components
        for thisComponent in PracticeTrial_Stim.components:
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
        
        # --- Run Routine "PracticeTrial_Stim" ---
        PracticeTrial_Stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop6, 'status') and thisPracticeLoop6.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = response.getKeys(keyList=[matchKey, noMatchKey], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # *Stim_LeftScreenInstruction* updates
            
            # if Stim_LeftScreenInstruction is starting this frame...
            if Stim_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_LeftScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.started')
                # update status
                Stim_LeftScreenInstruction.status = STARTED
                Stim_LeftScreenInstruction.setAutoDraw(True)
            
            # if Stim_LeftScreenInstruction is active this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_LeftScreenInstruction is stopping this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_LeftScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_LeftScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_LeftScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_LeftScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.stopped')
                    # update status
                    Stim_LeftScreenInstruction.status = FINISHED
                    Stim_LeftScreenInstruction.setAutoDraw(False)
            
            # *Stim_RightScreenInstruction* updates
            
            # if Stim_RightScreenInstruction is starting this frame...
            if Stim_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_RightScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.started')
                # update status
                Stim_RightScreenInstruction.status = STARTED
                Stim_RightScreenInstruction.setAutoDraw(True)
            
            # if Stim_RightScreenInstruction is active this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_RightScreenInstruction is stopping this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_RightScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_RightScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_RightScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_RightScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.stopped')
                    # update status
                    Stim_RightScreenInstruction.status = FINISHED
                    Stim_RightScreenInstruction.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Stim" ---
        for thisComponent in PracticeTrial_Stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Stim
        PracticeTrial_Stim.tStop = globalClock.getTime(format='float')
        PracticeTrial_Stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Stim.stopped', PracticeTrial_Stim.tStop)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceLoop6 (TrialHandler)
        practiceLoop6.addData('response.keys',response.keys)
        practiceLoop6.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceLoop6.addData('response.rt', response.rt)
            practiceLoop6.addData('response.duration', response.duration)
        # Run 'End Routine' code from feedbackLogic
        if response.keys is None:
            fbText = "No response."
            fbColor = 'yellow'
        elif response.corr:
            fbText = "Correct!"
            fbColor = 'limegreen'
        else:
            fbText = "Incorrect"
            fbColor = 'red'
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Stim.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Stim.maxDuration)
        elif PracticeTrial_Stim.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "PracticeTrial_Feedback" ---
        # create an object to store info about Routine PracticeTrial_Feedback
        PracticeTrial_Feedback = data.Routine(
            name='PracticeTrial_Feedback',
            components=[Fix, Feedback],
        )
        PracticeTrial_Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Fix.reset()
        Feedback.reset()
        Feedback.setColor(fbColor, colorSpace='rgb')
        Feedback.setText(fbText)
        # store start times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Feedback.tStart = globalClock.getTime(format='float')
        PracticeTrial_Feedback.status = STARTED
        thisExp.addData('PracticeTrial_Feedback.started', PracticeTrial_Feedback.tStart)
        PracticeTrial_Feedback.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_FeedbackComponents = PracticeTrial_Feedback.components
        for thisComponent in PracticeTrial_Feedback.components:
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
        
        # --- Run Routine "PracticeTrial_Feedback" ---
        PracticeTrial_Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop6, 'status') and thisPracticeLoop6.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # *Feedback* updates
            
            # if Feedback is starting this frame...
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                # update status
                Feedback.status = STARTED
                Feedback.setAutoDraw(True)
            
            # if Feedback is active this frame...
            if Feedback.status == STARTED:
                # update params
                pass
            
            # if Feedback is stopping this frame...
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    # update status
                    Feedback.status = FINISHED
                    Feedback.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Feedback" ---
        for thisComponent in PracticeTrial_Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStop = globalClock.getTime(format='float')
        PracticeTrial_Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Feedback.stopped', PracticeTrial_Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Feedback.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Feedback.maxDuration)
        elif PracticeTrial_Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeLoop6 as finished
        if hasattr(thisPracticeLoop6, 'status'):
            thisPracticeLoop6.status = FINISHED
        # if awaiting a pause, pause now
        if practiceLoop6.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceLoop6.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practiceLoop6'
    practiceLoop6.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "PracticeTrial7_Cue" ---
    # create an object to store info about Routine PracticeTrial7_Cue
    PracticeTrial7_Cue = data.Routine(
        name='PracticeTrial7_Cue',
        components=[CueFix_7, Cue_2Back_2],
    )
    PracticeTrial7_Cue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    CueFix_7.reset()
    Cue_2Back_2.reset()
    # store start times for PracticeTrial7_Cue
    PracticeTrial7_Cue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PracticeTrial7_Cue.tStart = globalClock.getTime(format='float')
    PracticeTrial7_Cue.status = STARTED
    thisExp.addData('PracticeTrial7_Cue.started', PracticeTrial7_Cue.tStart)
    PracticeTrial7_Cue.maxDuration = None
    # keep track of which components have finished
    PracticeTrial7_CueComponents = PracticeTrial7_Cue.components
    for thisComponent in PracticeTrial7_Cue.components:
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
    
    # --- Run Routine "PracticeTrial7_Cue" ---
    PracticeTrial7_Cue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CueFix_7* updates
        
        # if CueFix_7 is starting this frame...
        if CueFix_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CueFix_7.frameNStart = frameN  # exact frame index
            CueFix_7.tStart = t  # local t and not account for scr refresh
            CueFix_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueFix_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueFix_7.started')
            # update status
            CueFix_7.status = STARTED
            CueFix_7.setAutoDraw(True)
        
        # if CueFix_7 is active this frame...
        if CueFix_7.status == STARTED:
            # update params
            pass
        
        # if CueFix_7 is stopping this frame...
        if CueFix_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueFix_7.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                CueFix_7.tStop = t  # not accounting for scr refresh
                CueFix_7.tStopRefresh = tThisFlipGlobal  # on global time
                CueFix_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueFix_7.stopped')
                # update status
                CueFix_7.status = FINISHED
                CueFix_7.setAutoDraw(False)
        
        # *Cue_2Back_2* updates
        
        # if Cue_2Back_2 is starting this frame...
        if Cue_2Back_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Cue_2Back_2.frameNStart = frameN  # exact frame index
            Cue_2Back_2.tStart = t  # local t and not account for scr refresh
            Cue_2Back_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cue_2Back_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Cue_2Back_2.started')
            # update status
            Cue_2Back_2.status = STARTED
            Cue_2Back_2.setAutoDraw(True)
        
        # if Cue_2Back_2 is active this frame...
        if Cue_2Back_2.status == STARTED:
            # update params
            pass
        
        # if Cue_2Back_2 is stopping this frame...
        if Cue_2Back_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cue_2Back_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Cue_2Back_2.tStop = t  # not accounting for scr refresh
                Cue_2Back_2.tStopRefresh = tThisFlipGlobal  # on global time
                Cue_2Back_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cue_2Back_2.stopped')
                # update status
                Cue_2Back_2.status = FINISHED
                Cue_2Back_2.setAutoDraw(False)
        
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
                timers=[routineTimer, globalClock], 
                currentRoutine=PracticeTrial7_Cue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PracticeTrial7_Cue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrial7_Cue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PracticeTrial7_Cue" ---
    for thisComponent in PracticeTrial7_Cue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PracticeTrial7_Cue
    PracticeTrial7_Cue.tStop = globalClock.getTime(format='float')
    PracticeTrial7_Cue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PracticeTrial7_Cue.stopped', PracticeTrial7_Cue.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if PracticeTrial7_Cue.maxDurationReached:
        routineTimer.addTime(-PracticeTrial7_Cue.maxDuration)
    elif PracticeTrial7_Cue.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop7 = data.TrialHandler2(
        name='practiceLoop7',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('PracticeTrials/PracticeTrials7.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practiceLoop7)  # add the loop to the experiment
    thisPracticeLoop7 = practiceLoop7.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop7.rgb)
    if thisPracticeLoop7 != None:
        for paramName in thisPracticeLoop7:
            globals()[paramName] = thisPracticeLoop7[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeLoop7 in practiceLoop7:
        practiceLoop7.status = STARTED
        if hasattr(thisPracticeLoop7, 'status'):
            thisPracticeLoop7.status = STARTED
        currentLoop = practiceLoop7
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop7.rgb)
        if thisPracticeLoop7 != None:
            for paramName in thisPracticeLoop7:
                globals()[paramName] = thisPracticeLoop7[paramName]
        
        # --- Prepare to start Routine "PracticeTrial_Stim" ---
        # create an object to store info about Routine PracticeTrial_Stim
        PracticeTrial_Stim = data.Routine(
            name='PracticeTrial_Stim',
            components=[response, Stim, Stim_LeftScreenInstruction, Stim_RightScreenInstruction],
        )
        PracticeTrial_Stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from targetLogic
        # Decide correct key for this trial
        if TargetType == 'target':
            correctKey = matchKey
        else:
            correctKey = noMatchKey
        
        # create starting attributes for response
        response.keys = []
        response.rt = []
        _response_allKeys = []
        Stim.setImage(Stimulus)
        Stim_LeftScreenInstruction.reset()
        Stim_LeftScreenInstruction.setText(leftScreenInstruction)
        Stim_RightScreenInstruction.reset()
        Stim_RightScreenInstruction.setText(rightScreenInstruction)
        # store start times for PracticeTrial_Stim
        PracticeTrial_Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Stim.tStart = globalClock.getTime(format='float')
        PracticeTrial_Stim.status = STARTED
        thisExp.addData('PracticeTrial_Stim.started', PracticeTrial_Stim.tStart)
        PracticeTrial_Stim.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_StimComponents = PracticeTrial_Stim.components
        for thisComponent in PracticeTrial_Stim.components:
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
        
        # --- Run Routine "PracticeTrial_Stim" ---
        PracticeTrial_Stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop7, 'status') and thisPracticeLoop7.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = response.getKeys(keyList=[matchKey, noMatchKey], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # *Stim_LeftScreenInstruction* updates
            
            # if Stim_LeftScreenInstruction is starting this frame...
            if Stim_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_LeftScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.started')
                # update status
                Stim_LeftScreenInstruction.status = STARTED
                Stim_LeftScreenInstruction.setAutoDraw(True)
            
            # if Stim_LeftScreenInstruction is active this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_LeftScreenInstruction is stopping this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_LeftScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_LeftScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_LeftScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_LeftScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.stopped')
                    # update status
                    Stim_LeftScreenInstruction.status = FINISHED
                    Stim_LeftScreenInstruction.setAutoDraw(False)
            
            # *Stim_RightScreenInstruction* updates
            
            # if Stim_RightScreenInstruction is starting this frame...
            if Stim_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_RightScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.started')
                # update status
                Stim_RightScreenInstruction.status = STARTED
                Stim_RightScreenInstruction.setAutoDraw(True)
            
            # if Stim_RightScreenInstruction is active this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_RightScreenInstruction is stopping this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_RightScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_RightScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_RightScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_RightScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.stopped')
                    # update status
                    Stim_RightScreenInstruction.status = FINISHED
                    Stim_RightScreenInstruction.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Stim" ---
        for thisComponent in PracticeTrial_Stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Stim
        PracticeTrial_Stim.tStop = globalClock.getTime(format='float')
        PracticeTrial_Stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Stim.stopped', PracticeTrial_Stim.tStop)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceLoop7 (TrialHandler)
        practiceLoop7.addData('response.keys',response.keys)
        practiceLoop7.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceLoop7.addData('response.rt', response.rt)
            practiceLoop7.addData('response.duration', response.duration)
        # Run 'End Routine' code from feedbackLogic
        if response.keys is None:
            fbText = "No response."
            fbColor = 'yellow'
        elif response.corr:
            fbText = "Correct!"
            fbColor = 'limegreen'
        else:
            fbText = "Incorrect"
            fbColor = 'red'
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Stim.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Stim.maxDuration)
        elif PracticeTrial_Stim.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "PracticeTrial_Feedback" ---
        # create an object to store info about Routine PracticeTrial_Feedback
        PracticeTrial_Feedback = data.Routine(
            name='PracticeTrial_Feedback',
            components=[Fix, Feedback],
        )
        PracticeTrial_Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Fix.reset()
        Feedback.reset()
        Feedback.setColor(fbColor, colorSpace='rgb')
        Feedback.setText(fbText)
        # store start times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Feedback.tStart = globalClock.getTime(format='float')
        PracticeTrial_Feedback.status = STARTED
        thisExp.addData('PracticeTrial_Feedback.started', PracticeTrial_Feedback.tStart)
        PracticeTrial_Feedback.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_FeedbackComponents = PracticeTrial_Feedback.components
        for thisComponent in PracticeTrial_Feedback.components:
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
        
        # --- Run Routine "PracticeTrial_Feedback" ---
        PracticeTrial_Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop7, 'status') and thisPracticeLoop7.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # *Feedback* updates
            
            # if Feedback is starting this frame...
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                # update status
                Feedback.status = STARTED
                Feedback.setAutoDraw(True)
            
            # if Feedback is active this frame...
            if Feedback.status == STARTED:
                # update params
                pass
            
            # if Feedback is stopping this frame...
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    # update status
                    Feedback.status = FINISHED
                    Feedback.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Feedback" ---
        for thisComponent in PracticeTrial_Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStop = globalClock.getTime(format='float')
        PracticeTrial_Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Feedback.stopped', PracticeTrial_Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Feedback.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Feedback.maxDuration)
        elif PracticeTrial_Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeLoop7 as finished
        if hasattr(thisPracticeLoop7, 'status'):
            thisPracticeLoop7.status = FINISHED
        # if awaiting a pause, pause now
        if practiceLoop7.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceLoop7.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practiceLoop7'
    practiceLoop7.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "PracticeTrial8_Cue" ---
    # create an object to store info about Routine PracticeTrial8_Cue
    PracticeTrial8_Cue = data.Routine(
        name='PracticeTrial8_Cue',
        components=[CueFix_8, CueTarget_8, CueTargetImage_8, Zero_back_4],
    )
    PracticeTrial8_Cue.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    CueFix_8.reset()
    CueTarget_8.reset()
    Zero_back_4.reset()
    # store start times for PracticeTrial8_Cue
    PracticeTrial8_Cue.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PracticeTrial8_Cue.tStart = globalClock.getTime(format='float')
    PracticeTrial8_Cue.status = STARTED
    thisExp.addData('PracticeTrial8_Cue.started', PracticeTrial8_Cue.tStart)
    PracticeTrial8_Cue.maxDuration = None
    # keep track of which components have finished
    PracticeTrial8_CueComponents = PracticeTrial8_Cue.components
    for thisComponent in PracticeTrial8_Cue.components:
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
    
    # --- Run Routine "PracticeTrial8_Cue" ---
    PracticeTrial8_Cue.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CueFix_8* updates
        
        # if CueFix_8 is starting this frame...
        if CueFix_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CueFix_8.frameNStart = frameN  # exact frame index
            CueFix_8.tStart = t  # local t and not account for scr refresh
            CueFix_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueFix_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueFix_8.started')
            # update status
            CueFix_8.status = STARTED
            CueFix_8.setAutoDraw(True)
        
        # if CueFix_8 is active this frame...
        if CueFix_8.status == STARTED:
            # update params
            pass
        
        # if CueFix_8 is stopping this frame...
        if CueFix_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueFix_8.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                CueFix_8.tStop = t  # not accounting for scr refresh
                CueFix_8.tStopRefresh = tThisFlipGlobal  # on global time
                CueFix_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueFix_8.stopped')
                # update status
                CueFix_8.status = FINISHED
                CueFix_8.setAutoDraw(False)
        
        # *CueTarget_8* updates
        
        # if CueTarget_8 is starting this frame...
        if CueTarget_8.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            CueTarget_8.frameNStart = frameN  # exact frame index
            CueTarget_8.tStart = t  # local t and not account for scr refresh
            CueTarget_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueTarget_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueTarget_8.started')
            # update status
            CueTarget_8.status = STARTED
            CueTarget_8.setAutoDraw(True)
        
        # if CueTarget_8 is active this frame...
        if CueTarget_8.status == STARTED:
            # update params
            pass
        
        # if CueTarget_8 is stopping this frame...
        if CueTarget_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueTarget_8.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                CueTarget_8.tStop = t  # not accounting for scr refresh
                CueTarget_8.tStopRefresh = tThisFlipGlobal  # on global time
                CueTarget_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueTarget_8.stopped')
                # update status
                CueTarget_8.status = FINISHED
                CueTarget_8.setAutoDraw(False)
        
        # *CueTargetImage_8* updates
        
        # if CueTargetImage_8 is starting this frame...
        if CueTargetImage_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            CueTargetImage_8.frameNStart = frameN  # exact frame index
            CueTargetImage_8.tStart = t  # local t and not account for scr refresh
            CueTargetImage_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CueTargetImage_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'CueTargetImage_8.started')
            # update status
            CueTargetImage_8.status = STARTED
            CueTargetImage_8.setAutoDraw(True)
        
        # if CueTargetImage_8 is active this frame...
        if CueTargetImage_8.status == STARTED:
            # update params
            pass
        
        # if CueTargetImage_8 is stopping this frame...
        if CueTargetImage_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CueTargetImage_8.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                CueTargetImage_8.tStop = t  # not accounting for scr refresh
                CueTargetImage_8.tStopRefresh = tThisFlipGlobal  # on global time
                CueTargetImage_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'CueTargetImage_8.stopped')
                # update status
                CueTargetImage_8.status = FINISHED
                CueTargetImage_8.setAutoDraw(False)
        
        # *Zero_back_4* updates
        
        # if Zero_back_4 is starting this frame...
        if Zero_back_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Zero_back_4.frameNStart = frameN  # exact frame index
            Zero_back_4.tStart = t  # local t and not account for scr refresh
            Zero_back_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Zero_back_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Zero_back_4.started')
            # update status
            Zero_back_4.status = STARTED
            Zero_back_4.setAutoDraw(True)
        
        # if Zero_back_4 is active this frame...
        if Zero_back_4.status == STARTED:
            # update params
            pass
        
        # if Zero_back_4 is stopping this frame...
        if Zero_back_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Zero_back_4.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Zero_back_4.tStop = t  # not accounting for scr refresh
                Zero_back_4.tStopRefresh = tThisFlipGlobal  # on global time
                Zero_back_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Zero_back_4.stopped')
                # update status
                Zero_back_4.status = FINISHED
                Zero_back_4.setAutoDraw(False)
        
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
                timers=[routineTimer, globalClock], 
                currentRoutine=PracticeTrial8_Cue,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PracticeTrial8_Cue.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrial8_Cue.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PracticeTrial8_Cue" ---
    for thisComponent in PracticeTrial8_Cue.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PracticeTrial8_Cue
    PracticeTrial8_Cue.tStop = globalClock.getTime(format='float')
    PracticeTrial8_Cue.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PracticeTrial8_Cue.stopped', PracticeTrial8_Cue.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if PracticeTrial8_Cue.maxDurationReached:
        routineTimer.addTime(-PracticeTrial8_Cue.maxDuration)
    elif PracticeTrial8_Cue.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop8 = data.TrialHandler2(
        name='practiceLoop8',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('PracticeTrials/PracticeTrials8.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practiceLoop8)  # add the loop to the experiment
    thisPracticeLoop8 = practiceLoop8.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop8.rgb)
    if thisPracticeLoop8 != None:
        for paramName in thisPracticeLoop8:
            globals()[paramName] = thisPracticeLoop8[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeLoop8 in practiceLoop8:
        practiceLoop8.status = STARTED
        if hasattr(thisPracticeLoop8, 'status'):
            thisPracticeLoop8.status = STARTED
        currentLoop = practiceLoop8
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop8.rgb)
        if thisPracticeLoop8 != None:
            for paramName in thisPracticeLoop8:
                globals()[paramName] = thisPracticeLoop8[paramName]
        
        # --- Prepare to start Routine "PracticeTrial_Stim" ---
        # create an object to store info about Routine PracticeTrial_Stim
        PracticeTrial_Stim = data.Routine(
            name='PracticeTrial_Stim',
            components=[response, Stim, Stim_LeftScreenInstruction, Stim_RightScreenInstruction],
        )
        PracticeTrial_Stim.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from targetLogic
        # Decide correct key for this trial
        if TargetType == 'target':
            correctKey = matchKey
        else:
            correctKey = noMatchKey
        
        # create starting attributes for response
        response.keys = []
        response.rt = []
        _response_allKeys = []
        Stim.setImage(Stimulus)
        Stim_LeftScreenInstruction.reset()
        Stim_LeftScreenInstruction.setText(leftScreenInstruction)
        Stim_RightScreenInstruction.reset()
        Stim_RightScreenInstruction.setText(rightScreenInstruction)
        # store start times for PracticeTrial_Stim
        PracticeTrial_Stim.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Stim.tStart = globalClock.getTime(format='float')
        PracticeTrial_Stim.status = STARTED
        thisExp.addData('PracticeTrial_Stim.started', PracticeTrial_Stim.tStart)
        PracticeTrial_Stim.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_StimComponents = PracticeTrial_Stim.components
        for thisComponent in PracticeTrial_Stim.components:
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
        
        # --- Run Routine "PracticeTrial_Stim" ---
        PracticeTrial_Stim.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop8, 'status') and thisPracticeLoop8.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                theseKeys = response.getKeys(keyList=[matchKey, noMatchKey], ignoreKeys=["escape"], waitRelease=False)
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
            
            # *Stim* updates
            
            # if Stim is starting this frame...
            if Stim.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim.started')
                # update status
                Stim.status = STARTED
                Stim.setAutoDraw(True)
            
            # if Stim is active this frame...
            if Stim.status == STARTED:
                # update params
                pass
            
            # if Stim is stopping this frame...
            if Stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim.tStop = t  # not accounting for scr refresh
                    Stim.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim.stopped')
                    # update status
                    Stim.status = FINISHED
                    Stim.setAutoDraw(False)
            
            # *Stim_LeftScreenInstruction* updates
            
            # if Stim_LeftScreenInstruction is starting this frame...
            if Stim_LeftScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_LeftScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_LeftScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_LeftScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_LeftScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.started')
                # update status
                Stim_LeftScreenInstruction.status = STARTED
                Stim_LeftScreenInstruction.setAutoDraw(True)
            
            # if Stim_LeftScreenInstruction is active this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_LeftScreenInstruction is stopping this frame...
            if Stim_LeftScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_LeftScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_LeftScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_LeftScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_LeftScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_LeftScreenInstruction.stopped')
                    # update status
                    Stim_LeftScreenInstruction.status = FINISHED
                    Stim_LeftScreenInstruction.setAutoDraw(False)
            
            # *Stim_RightScreenInstruction* updates
            
            # if Stim_RightScreenInstruction is starting this frame...
            if Stim_RightScreenInstruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Stim_RightScreenInstruction.frameNStart = frameN  # exact frame index
                Stim_RightScreenInstruction.tStart = t  # local t and not account for scr refresh
                Stim_RightScreenInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_RightScreenInstruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.started')
                # update status
                Stim_RightScreenInstruction.status = STARTED
                Stim_RightScreenInstruction.setAutoDraw(True)
            
            # if Stim_RightScreenInstruction is active this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # update params
                pass
            
            # if Stim_RightScreenInstruction is stopping this frame...
            if Stim_RightScreenInstruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Stim_RightScreenInstruction.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Stim_RightScreenInstruction.tStop = t  # not accounting for scr refresh
                    Stim_RightScreenInstruction.tStopRefresh = tThisFlipGlobal  # on global time
                    Stim_RightScreenInstruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Stim_RightScreenInstruction.stopped')
                    # update status
                    Stim_RightScreenInstruction.status = FINISHED
                    Stim_RightScreenInstruction.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Stim,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Stim.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Stim.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Stim" ---
        for thisComponent in PracticeTrial_Stim.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Stim
        PracticeTrial_Stim.tStop = globalClock.getTime(format='float')
        PracticeTrial_Stim.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Stim.stopped', PracticeTrial_Stim.tStop)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correctKey).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceLoop8 (TrialHandler)
        practiceLoop8.addData('response.keys',response.keys)
        practiceLoop8.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceLoop8.addData('response.rt', response.rt)
            practiceLoop8.addData('response.duration', response.duration)
        # Run 'End Routine' code from feedbackLogic
        if response.keys is None:
            fbText = "No response."
            fbColor = 'yellow'
        elif response.corr:
            fbText = "Correct!"
            fbColor = 'limegreen'
        else:
            fbText = "Incorrect"
            fbColor = 'red'
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Stim.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Stim.maxDuration)
        elif PracticeTrial_Stim.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "PracticeTrial_Feedback" ---
        # create an object to store info about Routine PracticeTrial_Feedback
        PracticeTrial_Feedback = data.Routine(
            name='PracticeTrial_Feedback',
            components=[Fix, Feedback],
        )
        PracticeTrial_Feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Fix.reset()
        Feedback.reset()
        Feedback.setColor(fbColor, colorSpace='rgb')
        Feedback.setText(fbText)
        # store start times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PracticeTrial_Feedback.tStart = globalClock.getTime(format='float')
        PracticeTrial_Feedback.status = STARTED
        thisExp.addData('PracticeTrial_Feedback.started', PracticeTrial_Feedback.tStart)
        PracticeTrial_Feedback.maxDuration = None
        # keep track of which components have finished
        PracticeTrial_FeedbackComponents = PracticeTrial_Feedback.components
        for thisComponent in PracticeTrial_Feedback.components:
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
        
        # --- Run Routine "PracticeTrial_Feedback" ---
        PracticeTrial_Feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeLoop8, 'status') and thisPracticeLoop8.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fix* updates
            
            # if Fix is starting this frame...
            if Fix.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Fix.frameNStart = frameN  # exact frame index
                Fix.tStart = t  # local t and not account for scr refresh
                Fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fix.started')
                # update status
                Fix.status = STARTED
                Fix.setAutoDraw(True)
            
            # if Fix is active this frame...
            if Fix.status == STARTED:
                # update params
                pass
            
            # if Fix is stopping this frame...
            if Fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fix.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fix.tStop = t  # not accounting for scr refresh
                    Fix.tStopRefresh = tThisFlipGlobal  # on global time
                    Fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fix.stopped')
                    # update status
                    Fix.status = FINISHED
                    Fix.setAutoDraw(False)
            
            # *Feedback* updates
            
            # if Feedback is starting this frame...
            if Feedback.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Feedback.frameNStart = frameN  # exact frame index
                Feedback.tStart = t  # local t and not account for scr refresh
                Feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Feedback.started')
                # update status
                Feedback.status = STARTED
                Feedback.setAutoDraw(True)
            
            # if Feedback is active this frame...
            if Feedback.status == STARTED:
                # update params
                pass
            
            # if Feedback is stopping this frame...
            if Feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Feedback.tStop = t  # not accounting for scr refresh
                    Feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Feedback.stopped')
                    # update status
                    Feedback.status = FINISHED
                    Feedback.setAutoDraw(False)
            
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
                    timers=[routineTimer, globalClock], 
                    currentRoutine=PracticeTrial_Feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PracticeTrial_Feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrial_Feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PracticeTrial_Feedback" ---
        for thisComponent in PracticeTrial_Feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PracticeTrial_Feedback
        PracticeTrial_Feedback.tStop = globalClock.getTime(format='float')
        PracticeTrial_Feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PracticeTrial_Feedback.stopped', PracticeTrial_Feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if PracticeTrial_Feedback.maxDurationReached:
            routineTimer.addTime(-PracticeTrial_Feedback.maxDuration)
        elif PracticeTrial_Feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeLoop8 as finished
        if hasattr(thisPracticeLoop8, 'status'):
            thisPracticeLoop8.status = FINISHED
        # if awaiting a pause, pause now
        if practiceLoop8.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceLoop8.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practiceLoop8'
    practiceLoop8.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Goodbye" ---
    # create an object to store info about Routine Goodbye
    Goodbye = data.Routine(
        name='Goodbye',
        components=[EndProgram, AllDone],
    )
    Goodbye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for EndProgram
    EndProgram.keys = []
    EndProgram.rt = []
    _EndProgram_allKeys = []
    AllDone.reset()
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
        
        # *EndProgram* updates
        waitOnFlip = False
        
        # if EndProgram is starting this frame...
        if EndProgram.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndProgram.frameNStart = frameN  # exact frame index
            EndProgram.tStart = t  # local t and not account for scr refresh
            EndProgram.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndProgram, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndProgram.started')
            # update status
            EndProgram.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(EndProgram.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(EndProgram.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if EndProgram.status == STARTED and not waitOnFlip:
            theseKeys = EndProgram.getKeys(keyList=['space', 'escape'], ignoreKeys=["escape"], waitRelease=False)
            _EndProgram_allKeys.extend(theseKeys)
            if len(_EndProgram_allKeys):
                EndProgram.keys = _EndProgram_allKeys[-1].name  # just the last key pressed
                EndProgram.rt = _EndProgram_allKeys[-1].rt
                EndProgram.duration = _EndProgram_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code
        if 'space' in EndProgram.keys:
            core.quit()
        
        
        # *AllDone* updates
        
        # if AllDone is starting this frame...
        if AllDone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AllDone.frameNStart = frameN  # exact frame index
            AllDone.tStart = t  # local t and not account for scr refresh
            AllDone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AllDone, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AllDone.started')
            # update status
            AllDone.status = STARTED
            AllDone.setAutoDraw(True)
        
        # if AllDone is active this frame...
        if AllDone.status == STARTED:
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
                timers=[routineTimer, globalClock], 
                currentRoutine=Goodbye,
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
    if EndProgram.keys in ['', [], None]:  # No response was made
        EndProgram.keys = None
    thisExp.addData('EndProgram.keys',EndProgram.keys)
    if EndProgram.keys != None:  # we had a response
        thisExp.addData('EndProgram.rt', EndProgram.rt)
        thisExp.addData('EndProgram.duration', EndProgram.duration)
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
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


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
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


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
    logging.flush()
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
