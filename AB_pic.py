#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on March 15, 2021, at 11:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'AB_pic'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Employee\\Google Drive\\UP\\MyResearch\\TaskProgramming\\AB_pic\\AB_pic.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Set experiment start values for variable component curOpacity2
curOpacity2 = ''
curOpacity2Container = []
# Set experiment start values for variable component curOpacity
curOpacity = ''
curOpacityContainer = []
# Set experiment start values for variable component curImage
curImage = ''
curImageContainer = []
folder = 'C:\\Users\\Employee\\Google Drive\\UP\\MyResearch\\TaskProgramming\\AB_pic\\resources\\'
picFiles = os.listdir(folder)

picFiles = np.random.choice(picFiles, 40, False)

curOpacity = 0
curOpacity2 = 0

polygon = visual.Rect(
    win=win, name='polygon',
    width=(0.6, 0.6)[0], height=(0.6, 0.6)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
displayPicture = visual.ImageStim(
    win=win,
    name='displayPicture', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,1], fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)

# Initialize components for Routine "response1"
response1Clock = core.Clock()
option1_t1 = visual.ImageStim(
    win=win,
    name='option1_t1', 
    image='sin', mask=None,
    ori=0, pos=(-.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
option2_t1 = visual.ImageStim(
    win=win,
    name='option2_t1', 
    image='sin', mask=None,
    ori=0, pos=(.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "response2"
response2Clock = core.Clock()
option1_t2 = visual.ImageStim(
    win=win,
    name='option1_t2', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
option2_t2 = visual.ImageStim(
    win=win,
    name='option2_t2', 
    image='sin', mask=None,
    ori=0, pos=(-.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    #get the images for the current trial: 
    
    curSet = np.random.choice(picFiles,17, False)
    shuffle(curSet)
    ii = 0
    curImage = folder + curSet[ii]
    checkForOff = True
    checkForOn = False
    # keep track of which components have finished
    trialComponents = [polygon, displayPicture, polygon_2]
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
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        t = trialClock.getTime()
        onSets = np.linspace(stimLen+isi, (stimLen+isi)*15, 15)
        offSets = np.linspace(stimLen, (stimLen+isi)*15 - isi, 15)
        if checkForOff: #there's an image on screen and we need to know to take it off
            if t>offSets[ii]:
                print(str(t) + "offset!")
                curOpacity2 = 1
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
                else:
                    curImage = folder + curSet[ii]
                    if T1_loc-1==ii:
                        curOpacity = 1
                    elif T2_loc-1==ii:
                        curOpacity = 1
                    else:
                        curOpacity = 0
                    
        
        
        
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:  # only update if drawing
            polygon.setOpacity(curOpacity)
        
        # *displayPicture* updates
        if displayPicture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            displayPicture.frameNStart = frameN  # exact frame index
            displayPicture.tStart = t  # local t and not account for scr refresh
            displayPicture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(displayPicture, 'tStartRefresh')  # time at next scr refresh
            displayPicture.setAutoDraw(True)
        if displayPicture.status == STARTED:  # only update if drawing
            displayPicture.setImage(curImage)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:  # only update if drawing
            polygon_2.setOpacity(curOpacity2)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    trials.addData('displayPicture.started', displayPicture.tStartRefresh)
    trials.addData('displayPicture.stopped', displayPicture.tStopRefresh)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response1"-------
    continueRoutine = True
    # update component parameters for each repeat
    opt1 = folder + curSet[T1_loc-1]
    opt2 = folder + curSet[15]
    option1_t1.setImage(opt1)
    option2_t1.setImage(opt2)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    response1Components = [option1_t1, option2_t1, key_resp]
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
    response1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response1"-------
    while continueRoutine:
        # get current time
        t = response1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *option1_t1* updates
        if option1_t1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option1_t1.frameNStart = frameN  # exact frame index
            option1_t1.tStart = t  # local t and not account for scr refresh
            option1_t1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option1_t1, 'tStartRefresh')  # time at next scr refresh
            option1_t1.setAutoDraw(True)
        
        # *option2_t1* updates
        if option2_t1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option2_t1.frameNStart = frameN  # exact frame index
            option2_t1.tStart = t  # local t and not account for scr refresh
            option2_t1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option2_t1, 'tStartRefresh')  # time at next scr refresh
            option2_t1.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response1"-------
    for thisComponent in response1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('option1_t1.started', option1_t1.tStartRefresh)
    trials.addData('option1_t1.stopped', option1_t1.tStopRefresh)
    trials.addData('option2_t1.started', option2_t1.tStartRefresh)
    trials.addData('option2_t1.stopped', option2_t1.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "response1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response2"-------
    continueRoutine = True
    # update component parameters for each repeat
    opt1 = folder + curSet[T2_loc-1]
    opt2 = folder + curSet[16]
    option1_t2.setImage(opt1)
    option2_t2.setImage(opt2)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    response2Components = [option1_t2, option2_t2, key_resp_2]
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
    response2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response2"-------
    while continueRoutine:
        # get current time
        t = response2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *option1_t2* updates
        if option1_t2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option1_t2.frameNStart = frameN  # exact frame index
            option1_t2.tStart = t  # local t and not account for scr refresh
            option1_t2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option1_t2, 'tStartRefresh')  # time at next scr refresh
            option1_t2.setAutoDraw(True)
        
        # *option2_t2* updates
        if option2_t2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option2_t2.frameNStart = frameN  # exact frame index
            option2_t2.tStart = t  # local t and not account for scr refresh
            option2_t2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option2_t2, 'tStartRefresh')  # time at next scr refresh
            option2_t2.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response2"-------
    for thisComponent in response2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('option1_t2.started', option1_t2.tStartRefresh)
    trials.addData('option1_t2.stopped', option1_t2.tStopRefresh)
    trials.addData('option2_t2.started', option2_t2.tStartRefresh)
    trials.addData('option2_t2.stopped', option2_t2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "response2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
