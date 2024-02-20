#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.2),
    on December 01, 2023, at 17:22
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.2'
expName = 'AB_pic_singleT2'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
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
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='R:\\MSS\\Johnson_Lab\\dtf8829\\GitHub\\AB_pic\\AB_pic_singleT2_lastrun.py',
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
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
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
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=(1024, 768), fullscr=True, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
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
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
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
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
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
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
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
    
    # --- Initialize components for Routine "instructions" ---
    # Run 'Begin Experiment' code from code_7
    import random
    #from sklearn.linear_model import LogisticRegression
     
    
    folder = '.\\resources\\'
    picFiles = os.listdir(folder)
    
    #picFiles = np.random.choice(picFiles, 30, False)
    
    
    
    key_resp_4 = keyboard.Keyboard()
    textbox = visual.TextBox2(
         win, text='ในขั้นตอนนี้ ขอให้ท่านตั้งใจมองภาพบนหน้าจอ โดยแต่ละครั้งจะแสดงภาพวัตถุเพียง 1 ชนิด ในเวลา 3 วินาที ขอให้ท่านคิดว่าเป็นภาพวัตถุชนิดใด เมื่อปรากฎเครื่องหมาย + บนหน้าจอ ให้จ้องเครื่องหมาย + ท่านจะเห็นภาพหลายภาพปรากฎขึ้นอย่างรวดเร็ว และจะวนกลับไปที่ภาพแรกเมื่อสิ้นสุดการนำเสนอ ให้กดลูกศรชี้ไปทางขวา ‘ถ้าท่านเห็นภาพที่คิดไว้’ และกดลูกศรไปทางซ้าย ‘ถ้าท่านไม่เห็นภาพที่คิดไว้’  \nนอกจากนี้ ท่านควรมองหารูปเครื่องปั่น โดยเมื่อสิ้นสุดการทดลองผู้วิจัยจะสอบถามเกี่ยวกับรูปเครื่องปั่นอีกครั้ง ทั้งนี้ท่านจะได้รับการฝึกซ้อมก่อนการทดลองจริง และในการทดลองนี้ท่านจะได้รับคำแนะนำเกี่ยวกับผลการทดลองว่าถูกหรือผิด กด Spacebar เพื่อเริ่มการฝึกใช้งาน ', placeholder='Type here...', font='Browallia New',
         pos=(0, 0),     letterHeight=0.05,
         size=None, borderWidth=1.0,
         color='white', colorSpace='rgb',
         opacity=1,
         bold=False, italic=False,
         lineSpacing=0.75, speechPoint=None,
         padding=None, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "options" ---
    option1 = visual.ImageStim(
        win=win,
        name='option1', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, .3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    text_2 = visual.TextStim(win=win, name='text_2',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "trial" ---
    # Set experiment start values for variable component curOpacity3
    curOpacity3 = ''
    curOpacity3Container = []
    # Set experiment start values for variable component maskCol
    maskCol = ''
    maskColContainer = []
    # Set experiment start values for variable component curOpacity2
    curOpacity2 = ''
    curOpacity2Container = []
    # Set experiment start values for variable component curOpacity
    curOpacity = ''
    curOpacityContainer = []
    # Set experiment start values for variable component curImage
    curImage = ''
    curImageContainer = []
    displayPicture = visual.ImageStim(
        win=win,
        name='displayPicture', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-6.0)
    polygon_2 = visual.Rect(
        win=win, name='polygon_2',
        width=(0.25, 0.25)[0], height=(0.25, 0.25)[1],
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='white',
        opacity=1.0, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "response1" ---
    polygon_4 = visual.ShapeStim(
        win=win, name='polygon_4',
        size=(0.8, 0.8), vertices='triangle',
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,0,0],
        opacity=1, depth=0.0, interpolate=True)
    option1_t1 = visual.ImageStim(
        win=win,
        name='option1_t1', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "response2" ---
    polygon_5 = visual.ShapeStim(
        win=win, name='polygon_5', vertices='star7',
        size=(0.7, 0.7),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,1],
        opacity=1, depth=0.0, interpolate=True)
    key_resp_2 = keyboard.Keyboard()
    textbox_2 = visual.TextBox2(
         win, text='                            ท่านเห็นเครื่องปั่นหรือไม่ ', placeholder='Type here...', font='Browallia New',
         pos=(0, 0),     letterHeight=0.05,
         size=None, borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=1,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=None, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_2',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "feedback" ---
    textbox_3 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Browallia New',
         pos=(0, 0),     letterHeight=0.05,
         size=None, borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=1,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=None, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_3',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "break_2" ---
    # Set experiment start values for variable component breakText
    breakText = ""
    breakTextContainer = []
    # Set experiment start values for variable component breakTime
    breakTime = .1
    breakTimeContainer = []
    key_resp_3 = keyboard.Keyboard()
    textbox_6 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Browallia New',
         pos=(0, 0),     letterHeight=0.05,
         size=None, borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=1,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=None, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_6',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "mainInstructions" ---
    key_resp_7 = keyboard.Keyboard()
    textbox_4 = visual.TextBox2(
         win, text='ยอดเยี่ยม ! ท่านผ่านการฝึกใช้การแล้ว ต่อไปท่านจะเข้าสู่การทดลอง ซึ่งมีลักษณะเช่นเดียวกับที่ท่านได้ฝึกมาก่อนหน้านี้ ยกเว้นว่าในการทดลองนี้ท่านจะได้รับคำตอบว่าท่านตอบถูกหรือผิด ทั้งนี้การแสดงภาพในการหน้าจะจอจะเพิ่มความรวดเร็วขึ้น ซึ่งจะทำให้ท่านรู้สึกยากขึ้น ขอให้ท่านไม่ต้องกังวลใจ และทำการทดลองอย่างเต็มความสามารถ และเป็นความจริงที่สุด \n\nกด Spacebar', placeholder='Type here...', font='Browallia New',
         pos=(0, 0),     letterHeight=0.05,
         size=None, borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=1,
         bold=False, italic=False,
         lineSpacing=0.75, speechPoint=None,
         padding=None, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_4',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "optionsMain_2" ---
    option1_3 = visual.ImageStim(
        win=win,
        name='option1_3', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, .3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    text_7 = visual.TextStim(win=win, name='text_7',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "trial_2" ---
    # Set experiment start values for variable component curOpacity3_3
    curOpacity3_3 = ''
    curOpacity3_3Container = []
    # Set experiment start values for variable component maskCol_3
    maskCol_3 = ''
    maskCol_3Container = []
    # Set experiment start values for variable component curOpacity2_3
    curOpacity2_3 = ''
    curOpacity2_3Container = []
    # Set experiment start values for variable component curOpacity_3
    curOpacity_3 = ''
    curOpacity_3Container = []
    # Set experiment start values for variable component curImage_3
    curImage_3 = ''
    curImage_3Container = []
    displayPicture_4 = visual.ImageStim(
        win=win,
        name='displayPicture_4', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-6.0)
    polygon_16 = visual.Rect(
        win=win, name='polygon_16',
        width=(0.25, 0.25)[0], height=(0.25, 0.25)[1],
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='white',
        opacity=1.0, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "response1Main" ---
    polygon_7 = visual.ShapeStim(
        win=win, name='polygon_7',
        size=(0.8, 0.8), vertices='triangle',
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,0,0],
        opacity=1, depth=0.0, interpolate=True)
    option1_t1_2 = visual.ImageStim(
        win=win,
        name='option1_t1_2', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    key_resp_6 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "response2_2" ---
    polygon_17 = visual.ShapeStim(
        win=win, name='polygon_17', vertices='star7',
        size=(0.7, 0.7),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,1],
        opacity=1, depth=0.0, interpolate=True)
    key_resp_8 = keyboard.Keyboard()
    textbox_5 = visual.TextBox2(
         win, text='                            ท่านเห็นเครื่องปั่นหรือไม่ ', placeholder='Type here...', font='Browallia New',
         pos=(0, 0),     letterHeight=0.05,
         size=None, borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=1,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=None, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_5',
         depth=-3, autoLog=True,
    )
    
    # --- Initialize components for Routine "break_2" ---
    # Set experiment start values for variable component breakText
    breakText = ""
    breakTextContainer = []
    # Set experiment start values for variable component breakTime
    breakTime = .1
    breakTimeContainer = []
    key_resp_3 = keyboard.Keyboard()
    textbox_6 = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Browallia New',
         pos=(0, 0),     letterHeight=0.05,
         size=None, borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=1,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=None, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_6',
         depth=-4, autoLog=True,
    )
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions.started', globalClock.getTime())
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    textbox.reset()
    # keep track of which components have finished
    instructionsComponents = [key_resp_4, textbox]
    for thisComponent in instructionsComponents:
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
    
    # --- Run Routine "instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *textbox* updates
        
        # if textbox is starting this frame...
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            # update status
            textbox.status = STARTED
            textbox.setAutoDraw(True)
        
        # if textbox is active this frame...
        if textbox.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions.stopped', globalClock.getTime())
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionAB.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "options" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('options.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_5
        
        curSet = np.random.choice(picFiles,17, False)
        shuffle(curSet)
        for kk in range(0,17):
            trials.addData('img'+str(kk), curSet[kk])
        
        ii = 0
        curImage = folder + curSet[ii]
        checkForOff = True
        checkForOn = False
        
        options = [folder + curSet[T1_loc-1],  folder + curSet[T2_loc-1]]
        #shuffle(options)
        opt1 = options[0]
        opt2 = options[1]
        #opt3 = options[2]
        #opt4 = options[3]
        option1.setImage(opt1)
        # keep track of which components have finished
        optionsComponents = [option1, text_2]
        for thisComponent in optionsComponents:
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
        
        # --- Run Routine "options" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *option1* updates
            
            # if option1 is starting this frame...
            if option1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                option1.frameNStart = frameN  # exact frame index
                option1.tStart = t  # local t and not account for scr refresh
                option1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(option1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'option1.started')
                # update status
                option1.status = STARTED
                option1.setAutoDraw(True)
            
            # if option1 is active this frame...
            if option1.status == STARTED:
                # update params
                pass
            
            # if option1 is stopping this frame...
            if option1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > option1.tStartRefresh + 2.75-frameTolerance:
                    # keep track of stop time/frame for later
                    option1.tStop = t  # not accounting for scr refresh
                    option1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'option1.stopped')
                    # update status
                    option1.status = FINISHED
                    option1.setAutoDraw(False)
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in optionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "options" ---
        for thisComponent in optionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('options.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from code
        curImage = folder + curSet[0]
        curOpacity = 0
        curOpacity2 = 0
        curOpacity3 = .2
        # keep track of which components have finished
        trialComponents = [displayPicture, polygon_2]
        for thisComponent in trialComponents:
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
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            t = trialClock.getTime()
            onSets = np.linspace(stimLen+isi, (stimLen+isi)*15, 15)
            offSets = np.linspace(stimLen, (stimLen+isi)*15 - isi, 15)
            if checkForOff: #there's an image on screen and we need to know to take it off
                if t>offSets[ii]:
                    print(str(t) + "offset!")
                    curOpacity2 = 1
                    maskCol = [random.random(), random.random(), random.random()]
                    checkForOff = False
                    checkForOn = True
            else: #the mask is up right now, check for new image
                if t>onSets[ii]:
                    print(str(t) + "onSet!")
                    curOpacity2 = 0
                    checkForOff = True
                    checkForOn = False
                    ii = ii + 1
                    if ii==15:
                        continueRoutine = False
                        trials.addData('lastPresent', ii-1)
                    elif ii==T2_loc+3:
                        trials.addData('lastPresent', ii-1)
                        continueRoutine = False
                    else:
                        curImage = folder + curSet[ii]
                        if T1_loc-1==ii:
                            if random.random()<skipProb: #skip target 1
                                curImage = folder + curSet[15]       
                                trials.addData('skip1', 1)
                                skip1 = True
                            else:
                                trials.addData('skip1', 0)
                                skip1 = False
                            curOpacity = 1
                        elif T2_loc-1==ii:
                            curImage = "blender.jpg"
                            if random.random()<skipProb: #skip target 2
                                curImage = folder + curSet[16]      
                                trials.addData('skip2', 1)
                                skip2 = True
                            else:
                                trials.addData('skip2', 0)
                                skip2 = False
                            
                            curOpacity3 = 1
                        else:
                            curOpacity = 0
                            curOpacity3 = 0
                        
            
            
            
            
            # *displayPicture* updates
            
            # if displayPicture is starting this frame...
            if displayPicture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                displayPicture.frameNStart = frameN  # exact frame index
                displayPicture.tStart = t  # local t and not account for scr refresh
                displayPicture.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(displayPicture, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'displayPicture.started')
                # update status
                displayPicture.status = STARTED
                displayPicture.setAutoDraw(True)
            
            # if displayPicture is active this frame...
            if displayPicture.status == STARTED:
                # update params
                displayPicture.setImage(curImage, log=False)
            
            # *polygon_2* updates
            
            # if polygon_2 is starting this frame...
            if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_2.started')
                # update status
                polygon_2.status = STARTED
                polygon_2.setAutoDraw(True)
            
            # if polygon_2 is active this frame...
            if polygon_2.status == STARTED:
                # update params
                polygon_2.setFillColor([1,1,1], log=False)
                polygon_2.setOpacity(curOpacity2, log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        
        
        
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "response1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response1.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_2
        options = [folder + curSet[T1_loc-1]]
        shuffle(options)
        opt1 = options[0]
        trials.addData('opt1_t1', opt1)
        
        option1_t1.setImage(opt1)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        response1Components = [polygon_4, option1_t1, key_resp]
        for thisComponent in response1Components:
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
        
        # --- Run Routine "response1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_4* updates
            
            # if polygon_4 is starting this frame...
            if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_4.frameNStart = frameN  # exact frame index
                polygon_4.tStart = t  # local t and not account for scr refresh
                polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_4.started')
                # update status
                polygon_4.status = STARTED
                polygon_4.setAutoDraw(True)
            
            # if polygon_4 is active this frame...
            if polygon_4.status == STARTED:
                # update params
                pass
            
            # *option1_t1* updates
            
            # if option1_t1 is starting this frame...
            if option1_t1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                option1_t1.frameNStart = frameN  # exact frame index
                option1_t1.tStart = t  # local t and not account for scr refresh
                option1_t1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(option1_t1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'option1_t1.started')
                # update status
                option1_t1.status = STARTED
                option1_t1.setAutoDraw(True)
            
            # if option1_t1 is active this frame...
            if option1_t1.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','right', 'down', 'up'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response1" ---
        for thisComponent in response1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response1.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_2
        if key_resp.keys == 'right' and skip1 == False:
            cor1 = 1
        elif key_resp.keys == 'left' and skip1 == True:
            cor1 = 1
        else: 
            cor1 = 0
            
        trials.addData("cor1", cor1)
        
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # the Routine "response1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "response2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_3
        options = [folder + curSet[T2_loc-1]]
        shuffle(options)
        opt1 = options[0]
        
        trials.addData('opt1_t1', opt1)
        
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        textbox_2.reset()
        # keep track of which components have finished
        response2Components = [polygon_5, key_resp_2, textbox_2]
        for thisComponent in response2Components:
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
        
        # --- Run Routine "response2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_5* updates
            
            # if polygon_5 is starting this frame...
            if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_5.frameNStart = frameN  # exact frame index
                polygon_5.tStart = t  # local t and not account for scr refresh
                polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_5.started')
                # update status
                polygon_5.status = STARTED
                polygon_5.setAutoDraw(True)
            
            # if polygon_5 is active this frame...
            if polygon_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left','right', 'up', 'down'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *textbox_2* updates
            
            # if textbox_2 is starting this frame...
            if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_2.frameNStart = frameN  # exact frame index
                textbox_2.tStart = t  # local t and not account for scr refresh
                textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_2.started')
                # update status
                textbox_2.status = STARTED
                textbox_2.setAutoDraw(True)
            
            # if textbox_2 is active this frame...
            if textbox_2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response2" ---
        for thisComponent in response2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response2.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_3
        if key_resp_2.keys == 'right' and skip2 == False:
            cor2 = 1
        elif key_resp_2.keys == 'left' and skip2 == True:
            cor2 = 1
        else: 
            cor2 = 0
            
        
        trials.addData("cor2", cor2)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
            trials.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "response2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_6
        if cor1 == 1 and cor2==1:
            snip1 = "\n                           2/2 ทำถูก"
        if cor1==1 and cor2==0: 
            snip1 = "\n                            1/2 ทำถูก"
        if cor1==0 and cor2==1:
            snip1 = "\n                            1/2 ทำถูก"
        if cor1==0 and cor2==0:
            snip1 = "\n                            ผิดทั้งคู่ "
        
        
        feedback = snip1
        textbox_3.reset()
        textbox_3.setText(feedback)
        # keep track of which components have finished
        feedbackComponents = [textbox_3]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textbox_3* updates
            
            # if textbox_3 is starting this frame...
            if textbox_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_3.frameNStart = frameN  # exact frame index
                textbox_3.tStart = t  # local t and not account for scr refresh
                textbox_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_3.started')
                # update status
                textbox_3.status = STARTED
                textbox_3.setAutoDraw(True)
            
            # if textbox_3 is active this frame...
            if textbox_3.status == STARTED:
                # update params
                pass
            
            # if textbox_3 is stopping this frame...
            if textbox_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textbox_3.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    textbox_3.tStop = t  # not accounting for scr refresh
                    textbox_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_3.stopped')
                    # update status
                    textbox_3.status = FINISHED
                    textbox_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "break_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('break_2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_4
        try:
            cur = [58,116,174].index(trials2.thisTrialN) 
            breakTime = 10000
            if cur==0:
                breakText = "\n    พักสักครู่ ตอนนี้ผ่านการทดลองมาแล้ว 25% กด Spacebar เพื่อเริ่มต้นใหม่ หากท่านพร้อมแล้ว"
            elif cur==1:
                breakText = "\n    พักสักครู่ ตอนนี้ผ่านการทดลองมาแล้ว 50% กด Spacebar เพื่อเริ่มต้นใหม่ หากท่านพร้อมแล้ว"
            else:
                breakText = "\n    พักสักครู่ ตอนนี้ผ่านการทดลองมาแล้ว 75% กด Spacebar เพื่อเริ่มต้นใหม่ หากท่านพร้อมแล้ว"
        except: 
            breakTime = .01
            breakText = ""
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        textbox_6.reset()
        textbox_6.setText(breakText)
        # keep track of which components have finished
        break_2Components = [key_resp_3, textbox_6]
        for thisComponent in break_2Components:
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
        
        # --- Run Routine "break_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_4
            if breakTime<1:
                continueRoutine = False
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *textbox_6* updates
            
            # if textbox_6 is starting this frame...
            if textbox_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_6.frameNStart = frameN  # exact frame index
                textbox_6.tStart = t  # local t and not account for scr refresh
                textbox_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_6.started')
                # update status
                textbox_6.status = STARTED
                textbox_6.setAutoDraw(True)
            
            # if textbox_6 is active this frame...
            if textbox_6.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('break_2.stopped', globalClock.getTime())
        
        
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials.addData('key_resp_3.rt', key_resp_3.rt)
            trials.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'trials'
    
    
    # --- Prepare to start Routine "mainInstructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('mainInstructions.started', globalClock.getTime())
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # Run 'Begin Routine' code from code_16
    correctRecord = []
    curStimTim = .1
    stimTimRec = []
    params = np.array([-10,150])
    textbox_4.reset()
    # keep track of which components have finished
    mainInstructionsComponents = [key_resp_7, textbox_4]
    for thisComponent in mainInstructionsComponents:
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
    
    # --- Run Routine "mainInstructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_7* updates
        waitOnFlip = False
        
        # if key_resp_7 is starting this frame...
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_7.started')
            # update status
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *textbox_4* updates
        
        # if textbox_4 is starting this frame...
        if textbox_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_4.frameNStart = frameN  # exact frame index
            textbox_4.tStart = t  # local t and not account for scr refresh
            textbox_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_4.started')
            # update status
            textbox_4.status = STARTED
            textbox_4.setAutoDraw(True)
        
        # if textbox_4 is active this frame...
        if textbox_4.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mainInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mainInstructions" ---
    for thisComponent in mainInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('mainInstructions.stopped', globalClock.getTime())
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    thisExp.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        thisExp.addData('key_resp_7.rt', key_resp_7.rt)
        thisExp.addData('key_resp_7.duration', key_resp_7.duration)
    thisExp.nextEntry()
    # the Routine "mainInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionAB_main.xlsx'),
        seed=None, name='trials2')
    thisExp.addLoop(trials2)  # add the loop to the experiment
    thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            globals()[paramName] = thisTrials2[paramName]
    
    for thisTrials2 in trials2:
        currentLoop = trials2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
        if thisTrials2 != None:
            for paramName in thisTrials2:
                globals()[paramName] = thisTrials2[paramName]
        
        # --- Prepare to start Routine "optionsMain_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('optionsMain_2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_13
        
        curSet = np.random.choice(picFiles,17, False)
        shuffle(curSet)
        for kk in range(0,17):
            trials.addData('img'+str(kk), curSet[kk])
        
        ii = 0
        curImage = folder + curSet[ii]
        checkForOff = True
        checkForOn = False
        
        options = [folder + curSet[T1_loc-1],  folder + curSet[T2_loc-1]]
        #shuffle(options)
        opt1 = options[0]
        opt2 = options[1]
        #opt3 = options[2]
        #opt4 = options[3]
        option1_3.setImage(opt1)
        # keep track of which components have finished
        optionsMain_2Components = [option1_3, text_7]
        for thisComponent in optionsMain_2Components:
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
        
        # --- Run Routine "optionsMain_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_13
            
            #model = LogisticRegression(solver='liblinear', random_state=0).fit(curStimTim, correctRecord)
            if len(correctRecord)>5:
                
                y = np.array(correctRecord)
                x = np.reshape(np.array(stimTimRec), (-1,1))
               # params = np.array(params)
                
                
                if len(x[:,0]) < len(x[0,:]):
                    x = x.T
                    
                X = np.hstack((np.ones((len(x),1)),x))
                print(X)
                print(params)
                iterations = 50
                learning_rate = .03
            
                m = len(stimTimRec)
                
                for i in range(iterations):
                    weights = sqrt(np.arange(0,len(y),1))
                    weights = weights / sum(weights)
                    weights = weights * len(y)
                    params = params - (learning_rate/m) * (X.T @ ((1/(1+np.exp(-(X[:,0]*params[0] + X[:,1]*params[1])))) - y)) 
                    
                if np.isnan(params[0]):
                    params[0] = -1
                    params[1] = 4
            
               
            
            # *option1_3* updates
            
            # if option1_3 is starting this frame...
            if option1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                option1_3.frameNStart = frameN  # exact frame index
                option1_3.tStart = t  # local t and not account for scr refresh
                option1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(option1_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'option1_3.started')
                # update status
                option1_3.status = STARTED
                option1_3.setAutoDraw(True)
            
            # if option1_3 is active this frame...
            if option1_3.status == STARTED:
                # update params
                pass
            
            # if option1_3 is stopping this frame...
            if option1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > option1_3.tStartRefresh + 2.75-frameTolerance:
                    # keep track of stop time/frame for later
                    option1_3.tStop = t  # not accounting for scr refresh
                    option1_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'option1_3.stopped')
                    # update status
                    option1_3.status = FINISHED
                    option1_3.setAutoDraw(False)
            
            # *text_7* updates
            
            # if text_7 is starting this frame...
            if text_7.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.started')
                # update status
                text_7.status = STARTED
                text_7.setAutoDraw(True)
            
            # if text_7 is active this frame...
            if text_7.status == STARTED:
                # update params
                pass
            
            # if text_7 is stopping this frame...
            if text_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_7.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_7.tStop = t  # not accounting for scr refresh
                    text_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_7.stopped')
                    # update status
                    text_7.status = FINISHED
                    text_7.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in optionsMain_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "optionsMain_2" ---
        for thisComponent in optionsMain_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('optionsMain_2.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_13
        if len(correctRecord)>5:
            B1 = params[1]
            B0 = params[0]
            trials2.addData("B0", B0)
            trials2.addData("B1", B1)
        
            curStimTim = -((np.log(1/.80 - 1) + B0) / B1)
            curStimTim = curStimTim + np.random.rand() * .01 - .005
        
            if len(y)>10:
                if sum(y[len(y)-10:len(y)])>=8:
                    curStimTim = curStimTim - .005; 
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # --- Prepare to start Routine "trial_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial_2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_14
        curImage = folder + curSet[0]
        curOpacity = 0
        curOpacity2 = 0
        curOpacity3 = .2
        
        trialClock.reset()
        # keep track of which components have finished
        trial_2Components = [displayPicture_4, polygon_16]
        for thisComponent in trial_2Components:
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
        
        # --- Run Routine "trial_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_14
            t = trialClock.getTime()
            if phase == "ramp":
                curStimTim = stimLen
            trials2.addData('curStimTim', curStimTim)
            onSets = np.linspace(curStimTim+isi, (curStimTim+isi)*15, 15)
            offSets = np.linspace(curStimTim, (curStimTim+isi)*15 - isi, 15)
            if checkForOff: #there's an image on screen and we need to know to take it off
                if t>offSets[ii]:
                    print(str(t) + "offset!")
                    trials2.addData('stimOFF'+str(ii), str(t))
                    curOpacity2 = 1
                    maskCol = [random.random(), random.random(), random.random()]
                    checkForOff = False
                    checkForOn = True
            else: #the mask is up right now, check for new image
                if t>onSets[ii]:
                    print(str(t) + "onSet!")
                    trials2.addData('stimON'+str(ii), str(t))
                    curOpacity2 = 0
                    checkForOff = True
                    checkForOn = False
                    ii = ii + 1
                    if ii==15:
                        continueRoutine = False
                        trials2.addData('lastPresent', ii-1)
                    elif ii==T2_loc+3:
                        trials2.addData('lastPresent', ii-1)
                        continueRoutine = False
                    else:
                        curImage = folder + curSet[ii]
                        if T1_loc-1==ii:
                            if random.random()<skipProb: #skip target 1
                                curImage = folder + curSet[15]       
                                trials2.addData('skip1', 1)
                                skip1 = True
                            else:
                                trials2.addData('skip1', 0)
                                skip1 = False
                            curOpacity = 1
                        elif T2_loc-1==ii:
                            curImage = "blender.jpg"
                            if random.random()<skipProb: #skip target 2
                                curImage = folder + curSet[16]      
                                trials2.addData('skip2', 1)
                                skip2 = True
                            else:
                                trials2.addData('skip2', 0)
                                skip2 = False
                            
                            curOpacity3 = 1
                        else:
                            curOpacity = 0
                            curOpacity3 = 0
                        
            
            
            
            
            # *displayPicture_4* updates
            
            # if displayPicture_4 is starting this frame...
            if displayPicture_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                displayPicture_4.frameNStart = frameN  # exact frame index
                displayPicture_4.tStart = t  # local t and not account for scr refresh
                displayPicture_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(displayPicture_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'displayPicture_4.started')
                # update status
                displayPicture_4.status = STARTED
                displayPicture_4.setAutoDraw(True)
            
            # if displayPicture_4 is active this frame...
            if displayPicture_4.status == STARTED:
                # update params
                displayPicture_4.setImage(curImage, log=False)
            
            # *polygon_16* updates
            
            # if polygon_16 is starting this frame...
            if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_16.frameNStart = frameN  # exact frame index
                polygon_16.tStart = t  # local t and not account for scr refresh
                polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_16.started')
                # update status
                polygon_16.status = STARTED
                polygon_16.setAutoDraw(True)
            
            # if polygon_16 is active this frame...
            if polygon_16.status == STARTED:
                # update params
                polygon_16.setFillColor([1,1,1], log=False)
                polygon_16.setOpacity(curOpacity2, log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_2" ---
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial_2.stopped', globalClock.getTime())
        
        
        
        
        
        # Run 'End Routine' code from code_14
        trials2.addData('curStimTim', curStimTim)
        # the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "response1Main" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response1Main.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_9
        options = [folder + curSet[T1_loc-1]]
        shuffle(options)
        opt1 = options[0]
        trials2.addData('opt1_t1', opt1)
        
        option1_t1_2.setImage(opt1)
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # keep track of which components have finished
        response1MainComponents = [polygon_7, option1_t1_2, key_resp_6]
        for thisComponent in response1MainComponents:
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
        
        # --- Run Routine "response1Main" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_7* updates
            
            # if polygon_7 is starting this frame...
            if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_7.frameNStart = frameN  # exact frame index
                polygon_7.tStart = t  # local t and not account for scr refresh
                polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_7.started')
                # update status
                polygon_7.status = STARTED
                polygon_7.setAutoDraw(True)
            
            # if polygon_7 is active this frame...
            if polygon_7.status == STARTED:
                # update params
                pass
            
            # *option1_t1_2* updates
            
            # if option1_t1_2 is starting this frame...
            if option1_t1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                option1_t1_2.frameNStart = frameN  # exact frame index
                option1_t1_2.tStart = t  # local t and not account for scr refresh
                option1_t1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(option1_t1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'option1_t1_2.started')
                # update status
                option1_t1_2.status = STARTED
                option1_t1_2.setAutoDraw(True)
            
            # if option1_t1_2 is active this frame...
            if option1_t1_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_6* updates
            waitOnFlip = False
            
            # if key_resp_6 is starting this frame...
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.started')
                # update status
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['left','right', 'down', 'up'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response1MainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response1Main" ---
        for thisComponent in response1MainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response1Main.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_9
        if key_resp_6.keys == 'right' and skip1 == False:
            cor1 = 1
        elif key_resp_6.keys == 'left' and skip1 == True:
            cor1 = 1
        else: 
            cor1 = 0
            
        
        trials2.addData("cor1", cor1)
        
        correctRecord.append(cor1)
        correctRecord.append(0)
        correctRecord.append(1)
        stimTimRec.append(curStimTim)
        stimTimRec.append(0)
        stimTimRec.append(.2)
        
        
        
        
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        trials2.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            trials2.addData('key_resp_6.rt', key_resp_6.rt)
            trials2.addData('key_resp_6.duration', key_resp_6.duration)
        # the Routine "response1Main" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "response2_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response2_2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_15
        options = [folder + curSet[T2_loc-1]]
        shuffle(options)
        opt1 = options[0]
        
        trials2.addData('opt1_t1', opt1)
        
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        textbox_5.reset()
        # keep track of which components have finished
        response2_2Components = [polygon_17, key_resp_8, textbox_5]
        for thisComponent in response2_2Components:
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
        
        # --- Run Routine "response2_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_17* updates
            
            # if polygon_17 is starting this frame...
            if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_17.frameNStart = frameN  # exact frame index
                polygon_17.tStart = t  # local t and not account for scr refresh
                polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_17.started')
                # update status
                polygon_17.status = STARTED
                polygon_17.setAutoDraw(True)
            
            # if polygon_17 is active this frame...
            if polygon_17.status == STARTED:
                # update params
                pass
            
            # *key_resp_8* updates
            waitOnFlip = False
            
            # if key_resp_8 is starting this frame...
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.started')
                # update status
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['left','right', 'up', 'down'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *textbox_5* updates
            
            # if textbox_5 is starting this frame...
            if textbox_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_5.frameNStart = frameN  # exact frame index
                textbox_5.tStart = t  # local t and not account for scr refresh
                textbox_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_5.started')
                # update status
                textbox_5.status = STARTED
                textbox_5.setAutoDraw(True)
            
            # if textbox_5 is active this frame...
            if textbox_5.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response2_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response2_2" ---
        for thisComponent in response2_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response2_2.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_15
        if key_resp_8.keys == 'right' and skip2 == False:
            cor2 = 1
        elif key_resp_8.keys == 'left' and skip2 == True:
            cor2 = 1
        else: 
            cor2 = 0
            
        
        trials.addData("cor2", cor2)
        
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
        trials2.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            trials2.addData('key_resp_8.rt', key_resp_8.rt)
            trials2.addData('key_resp_8.duration', key_resp_8.duration)
        # the Routine "response2_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "break_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('break_2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_4
        try:
            cur = [58,116,174].index(trials2.thisTrialN) 
            breakTime = 10000
            if cur==0:
                breakText = "\n    พักสักครู่ ตอนนี้ผ่านการทดลองมาแล้ว 25% กด Spacebar เพื่อเริ่มต้นใหม่ หากท่านพร้อมแล้ว"
            elif cur==1:
                breakText = "\n    พักสักครู่ ตอนนี้ผ่านการทดลองมาแล้ว 50% กด Spacebar เพื่อเริ่มต้นใหม่ หากท่านพร้อมแล้ว"
            else:
                breakText = "\n    พักสักครู่ ตอนนี้ผ่านการทดลองมาแล้ว 75% กด Spacebar เพื่อเริ่มต้นใหม่ หากท่านพร้อมแล้ว"
        except: 
            breakTime = .01
            breakText = ""
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        textbox_6.reset()
        textbox_6.setText(breakText)
        # keep track of which components have finished
        break_2Components = [key_resp_3, textbox_6]
        for thisComponent in break_2Components:
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
        
        # --- Run Routine "break_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_4
            if breakTime<1:
                continueRoutine = False
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *textbox_6* updates
            
            # if textbox_6 is starting this frame...
            if textbox_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_6.frameNStart = frameN  # exact frame index
                textbox_6.tStart = t  # local t and not account for scr refresh
                textbox_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_6.started')
                # update status
                textbox_6.status = STARTED
                textbox_6.setAutoDraw(True)
            
            # if textbox_6 is active this frame...
            if textbox_6.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('break_2.stopped', globalClock.getTime())
        
        
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials2.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials2.addData('key_resp_3.rt', key_resp_3.rt)
            trials2.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'trials2'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


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


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
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
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
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
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
