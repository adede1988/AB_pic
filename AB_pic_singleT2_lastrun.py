#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on เมษายน 09, 2021, at 11:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'AB_pic_singleT2'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Employee\\Documents\\GitHub\\AB_pic\\AB_pic_singleT2_lastrun.py',
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
import random
#from sklearn.linear_model import LogisticRegression
 

folder = '.\\resources\\'
picFiles = os.listdir(folder)

#picFiles = np.random.choice(picFiles, 30, False)



key_resp_4 = keyboard.Keyboard()
textbox = visual.TextBox2(
     win, text='ในขั้นตอนนี้ ขอให้ท่านตั้งใจมองภาพบนหน้าจอ โดยแต่ละครั้งจะแสดงภาพวัตถุเพียง 1 ชนิด ในเวลา 3 วินาที ขอให้ท่านคิดว่าเป็นภาพวัตถุชนิดใด เมื่อปรากฎเครื่องหมาย + บนหน้าจอ ให้จ้องเครื่องหมาย + ท่านจะเห็นภาพหลายภาพปรากฎขึ้นอย่างรวดเร็ว และจะวนกลับไปที่ภาพแรกเมื่อสิ้นสุดการนำเสนอ ให้กดลูกศรชี้ไปทางขวา ‘ถ้าท่านเห็นภาพที่คิดไว้’ และกดลูกศรไปทางซ้าย ‘ถ้าท่านไม่เห็นภาพที่คิดไว้’  \nนอกจากนี้ ท่านควรมองหารูปเครื่องปั่น โดยเมื่อสิ้นสุดการทดลองผู้วิจัยจะสอบถามเกี่ยวกับรูปเครื่องปั่นอีกครั้ง ทั้งนี้ท่านจะได้รับการฝึกซ้อมก่อนการทดลองจริง และในการทดลองนี้ท่านจะได้รับคำแนะนำเกี่ยวกับผลการทดลองว่าถูกหรือผิด กด Spacebar เพื่อเริ่มการฝึกใช้งาน ', font='Browallia New',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=1.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=0.75,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox',
     autoLog=True,
)

# Initialize components for Routine "options"
optionsClock = core.Clock()
option1 = visual.ImageStim(
    win=win,
    name='option1', 
    image='sin', mask=None,
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
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
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(0.25, 0.25)[0], height=(0.25, 0.25)[1],
    ori=0, pos=(0, 0),
    lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='white',
    opacity=1.0, depth=-7.0, interpolate=True)

# Initialize components for Routine "response1"
response1Clock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4',
    vertices=[[-(0.8, 0.8)[0]/2.0,-(0.8, 0.8)[1]/2.0], [+(0.8, 0.8)[0]/2.0,-(0.8, 0.8)[1]/2.0], [0,(0.8, 0.8)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,0,0],
    opacity=1, depth=0.0, interpolate=True)
option1_t1 = visual.ImageStim(
    win=win,
    name='option1_t1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "response2"
response2Clock = core.Clock()
polygon_5 = visual.ShapeStim(
    win=win, name='polygon_5', vertices='star7',
    size=(0.7, 0.7),
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,1],
    opacity=1, depth=0.0, interpolate=True)
key_resp_2 = keyboard.Keyboard()
textbox_2 = visual.TextBox2(
     win, text='                            ท่านเห็นเครื่องปั่นหรือไม่ ', font='Browallia New',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_2',
     autoLog=True,
)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
textbox_3 = visual.TextBox2(
     win, text='', font='Browallia New',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_3',
     autoLog=True,
)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
# Set experiment start values for variable component breakText
breakText = ""
breakTextContainer = []
# Set experiment start values for variable component breakTime
breakTime = .1
breakTimeContainer = []
key_resp_3 = keyboard.Keyboard()
textbox_6 = visual.TextBox2(
     win, text='', font='Browallia New',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_6',
     autoLog=True,
)

# Initialize components for Routine "mainInstructions"
mainInstructionsClock = core.Clock()
key_resp_7 = keyboard.Keyboard()
textbox_4 = visual.TextBox2(
     win, text='ยอดเยี่ยม ! ท่านผ่านการฝึกใช้การแล้ว ต่อไปท่านจะเข้าสู่การทดลอง ซึ่งมีลักษณะเช่นเดียวกับที่ท่านได้ฝึกมาก่อนหน้านี้ ยกเว้นว่าในการทดลองนี้ท่านจะได้รับคำตอบว่าท่านตอบถูกหรือผิด ทั้งนี้การแสดงภาพในการหน้าจะจอจะเพิ่มความรวดเร็วขึ้น ซึ่งจะทำให้ท่านรู้สึกยากขึ้น ขอให้ท่านไม่ต้องกังวลใจ และทำการทดลองอย่างเต็มความสามารถ และเป็นความจริงที่สุด \n\nกด Spacebar', font='Browallia New',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=0.75,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_4',
     autoLog=True,
)

# Initialize components for Routine "optionsMain_2"
optionsMain_2Clock = core.Clock()
option1_3 = visual.ImageStim(
    win=win,
    name='option1_3', 
    image='sin', mask=None,
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

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
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
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
polygon_16 = visual.Rect(
    win=win, name='polygon_16',
    width=(0.25, 0.25)[0], height=(0.25, 0.25)[1],
    ori=0, pos=(0, 0),
    lineWidth=0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor='white',
    opacity=1.0, depth=-7.0, interpolate=True)

# Initialize components for Routine "response1Main"
response1MainClock = core.Clock()
polygon_7 = visual.ShapeStim(
    win=win, name='polygon_7',
    vertices=[[-(0.8, 0.8)[0]/2.0,-(0.8, 0.8)[1]/2.0], [+(0.8, 0.8)[0]/2.0,-(0.8, 0.8)[1]/2.0], [0,(0.8, 0.8)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,0,0],
    opacity=1, depth=0.0, interpolate=True)
option1_t1_2 = visual.ImageStim(
    win=win,
    name='option1_t1_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "response2_2"
response2_2Clock = core.Clock()
polygon_17 = visual.ShapeStim(
    win=win, name='polygon_17', vertices='star7',
    size=(0.7, 0.7),
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[0,0,1],
    opacity=1, depth=0.0, interpolate=True)
key_resp_8 = keyboard.Keyboard()
textbox_5 = visual.TextBox2(
     win, text='                            ท่านเห็นเครื่องปั่นหรือไม่ ', font='Browallia New',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_5',
     autoLog=True,
)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
# Set experiment start values for variable component breakText
breakText = ""
breakTextContainer = []
# Set experiment start values for variable component breakTime
breakTime = .1
breakTimeContainer = []
key_resp_3 = keyboard.Keyboard()
textbox_6 = visual.TextBox2(
     win, text='', font='Browallia New',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_6',
     autoLog=True,
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
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
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)
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
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "options"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    
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
    optionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "options"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = optionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=optionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *option1* updates
        if option1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option1.frameNStart = frameN  # exact frame index
            option1.tStart = t  # local t and not account for scr refresh
            option1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option1, 'tStartRefresh')  # time at next scr refresh
            option1.setAutoDraw(True)
        if option1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > option1.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                option1.tStop = t  # not accounting for scr refresh
                option1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(option1, 'tStopRefresh')  # time at next scr refresh
                option1.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in optionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "options"-------
    for thisComponent in optionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('option1.started', option1.tStartRefresh)
    trials.addData('option1.stopped', option1.tStopRefresh)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
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
            polygon_2.setFillColor([1,1,1])
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
    trials.addData('displayPicture.started', displayPicture.tStartRefresh)
    trials.addData('displayPicture.stopped', displayPicture.tStopRefresh)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response1"-------
    continueRoutine = True
    # update component parameters for each repeat
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
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        
        # *option1_t1* updates
        if option1_t1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option1_t1.frameNStart = frameN  # exact frame index
            option1_t1.tStart = t  # local t and not account for scr refresh
            option1_t1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option1_t1, 'tStartRefresh')  # time at next scr refresh
            option1_t1.setAutoDraw(True)
        
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
            theseKeys = key_resp.getKeys(keyList=['left', 'right', 'down', 'up'], waitRelease=False)
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
    trials.addData('polygon_4.started', polygon_4.tStartRefresh)
    trials.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    if key_resp.keys == 'right' and skip1 == False:
        cor1 = 1
    elif key_resp.keys == 'left' and skip1 == True:
        cor1 = 1
    else: 
        cor1 = 0
        
    trials.addData("cor1", cor1)
    
    trials.addData('option1_t1.started', option1_t1.tStartRefresh)
    trials.addData('option1_t1.stopped', option1_t1.tStopRefresh)
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
    options = [folder + curSet[T2_loc-1]]
    shuffle(options)
    opt1 = options[0]
    
    trials.addData('opt1_t1', opt1)
    
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
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
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        
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
            theseKeys = key_resp_2.getKeys(keyList=['left', 'right', 'up', 'down'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *textbox_2* updates
        if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_2.frameNStart = frameN  # exact frame index
            textbox_2.tStart = t  # local t and not account for scr refresh
            textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
            textbox_2.setAutoDraw(True)
        
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
    trials.addData('polygon_5.started', polygon_5.tStartRefresh)
    trials.addData('polygon_5.stopped', polygon_5.tStopRefresh)
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
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    trials.addData('textbox_2.started', textbox_2.tStartRefresh)
    trials.addData('textbox_2.stopped', textbox_2.tStopRefresh)
    # the Routine "response2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if cor1 == 1 and cor2==1:
        snip1 = "\n                           2/2 ทำถูก"
    if cor1==1 and cor2==0: 
        snip1 = "\n                            1/2 ทำถูก"
    if cor1==0 and cor2==1:
        snip1 = "\n                            1/2 ทำถูก"
    if cor1==0 and cor2==0:
        snip1 = "\n                            ผิดทั้งคู่ "
    
    
    feedback = snip1
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
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox_3* updates
        if textbox_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_3.frameNStart = frameN  # exact frame index
            textbox_3.tStart = t  # local t and not account for scr refresh
            textbox_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_3, 'tStartRefresh')  # time at next scr refresh
            textbox_3.setAutoDraw(True)
        if textbox_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                textbox_3.tStop = t  # not accounting for scr refresh
                textbox_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox_3, 'tStopRefresh')  # time at next scr refresh
                textbox_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('textbox_3.started', textbox_3.tStartRefresh)
    trials.addData('textbox_3.stopped', textbox_3.tStopRefresh)
    
    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_2"-------
    while continueRoutine:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if breakTime<1:
            continueRoutine = False
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *textbox_6* updates
        if textbox_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_6.frameNStart = frameN  # exact frame index
            textbox_6.tStart = t  # local t and not account for scr refresh
            textbox_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_6, 'tStartRefresh')  # time at next scr refresh
            textbox_6.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    trials.addData('textbox_6.started', textbox_6.tStartRefresh)
    trials.addData('textbox_6.stopped', textbox_6.tStopRefresh)
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "mainInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
correctRecord = []
curStimTim = .1
stimTimRec = []
params = np.array([-10,150])
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
mainInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "mainInstructions"-------
while continueRoutine:
    # get current time
    t = mainInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=mainInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *textbox_4* updates
    if textbox_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox_4.frameNStart = frameN  # exact frame index
        textbox_4.tStart = t  # local t and not account for scr refresh
        textbox_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox_4, 'tStartRefresh')  # time at next scr refresh
        textbox_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mainInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mainInstructions"-------
for thisComponent in mainInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('textbox_4.started', textbox_4.tStartRefresh)
thisExp.addData('textbox_4.stopped', textbox_4.tStopRefresh)
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
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "optionsMain_2"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    
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
    optionsMain_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "optionsMain_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = optionsMain_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=optionsMain_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        if option1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option1_3.frameNStart = frameN  # exact frame index
            option1_3.tStart = t  # local t and not account for scr refresh
            option1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option1_3, 'tStartRefresh')  # time at next scr refresh
            option1_3.setAutoDraw(True)
        if option1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > option1_3.tStartRefresh + 2.75-frameTolerance:
                # keep track of stop time/frame for later
                option1_3.tStop = t  # not accounting for scr refresh
                option1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(option1_3, 'tStopRefresh')  # time at next scr refresh
                option1_3.setAutoDraw(False)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in optionsMain_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "optionsMain_2"-------
    for thisComponent in optionsMain_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
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
    trials2.addData('option1_3.started', option1_3.tStartRefresh)
    trials2.addData('option1_3.stopped', option1_3.tStopRefresh)
    trials2.addData('text_7.started', text_7.tStartRefresh)
    trials2.addData('text_7.stopped', text_7.tStopRefresh)
    
    # ------Prepare to start Routine "trial_2"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_2"-------
    while continueRoutine:
        # get current time
        t = trial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
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
        if displayPicture_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            displayPicture_4.frameNStart = frameN  # exact frame index
            displayPicture_4.tStart = t  # local t and not account for scr refresh
            displayPicture_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(displayPicture_4, 'tStartRefresh')  # time at next scr refresh
            displayPicture_4.setAutoDraw(True)
        if displayPicture_4.status == STARTED:  # only update if drawing
            displayPicture_4.setImage(curImage)
        
        # *polygon_16* updates
        if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_16.frameNStart = frameN  # exact frame index
            polygon_16.tStart = t  # local t and not account for scr refresh
            polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
            polygon_16.setAutoDraw(True)
        if polygon_16.status == STARTED:  # only update if drawing
            polygon_16.setFillColor([1,1,1])
            polygon_16.setOpacity(curOpacity2)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_2"-------
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials2.addData('curStimTim', curStimTim)
    trials2.addData('displayPicture_4.started', displayPicture_4.tStartRefresh)
    trials2.addData('displayPicture_4.stopped', displayPicture_4.tStopRefresh)
    trials2.addData('polygon_16.started', polygon_16.tStartRefresh)
    trials2.addData('polygon_16.stopped', polygon_16.tStopRefresh)
    # the Routine "trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response1Main"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    response1MainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response1Main"-------
    while continueRoutine:
        # get current time
        t = response1MainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response1MainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_7* updates
        if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_7.frameNStart = frameN  # exact frame index
            polygon_7.tStart = t  # local t and not account for scr refresh
            polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
            polygon_7.setAutoDraw(True)
        
        # *option1_t1_2* updates
        if option1_t1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option1_t1_2.frameNStart = frameN  # exact frame index
            option1_t1_2.tStart = t  # local t and not account for scr refresh
            option1_t1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option1_t1_2, 'tStartRefresh')  # time at next scr refresh
            option1_t1_2.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['left', 'right', 'down', 'up'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response1MainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response1Main"-------
    for thisComponent in response1MainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials2.addData('polygon_7.started', polygon_7.tStartRefresh)
    trials2.addData('polygon_7.stopped', polygon_7.tStopRefresh)
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
    
    
    
    
    trials2.addData('option1_t1_2.started', option1_t1_2.tStartRefresh)
    trials2.addData('option1_t1_2.stopped', option1_t1_2.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    trials2.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials2.addData('key_resp_6.rt', key_resp_6.rt)
    trials2.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    trials2.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "response1Main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response2_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    options = [folder + curSet[T2_loc-1]]
    shuffle(options)
    opt1 = options[0]
    
    trials2.addData('opt1_t1', opt1)
    
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
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
    response2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response2_2"-------
    while continueRoutine:
        # get current time
        t = response2_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response2_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_17* updates
        if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_17.frameNStart = frameN  # exact frame index
            polygon_17.tStart = t  # local t and not account for scr refresh
            polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
            polygon_17.setAutoDraw(True)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['left', 'right', 'up', 'down'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *textbox_5* updates
        if textbox_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_5.frameNStart = frameN  # exact frame index
            textbox_5.tStart = t  # local t and not account for scr refresh
            textbox_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_5, 'tStartRefresh')  # time at next scr refresh
            textbox_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response2_2"-------
    for thisComponent in response2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials2.addData('polygon_17.started', polygon_17.tStartRefresh)
    trials2.addData('polygon_17.stopped', polygon_17.tStopRefresh)
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
    trials2.addData('key_resp_8.started', key_resp_8.tStartRefresh)
    trials2.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
    trials2.addData('textbox_5.started', textbox_5.tStartRefresh)
    trials2.addData('textbox_5.stopped', textbox_5.tStopRefresh)
    # the Routine "response2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_2"-------
    while continueRoutine:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if breakTime<1:
            continueRoutine = False
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *textbox_6* updates
        if textbox_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_6.frameNStart = frameN  # exact frame index
            textbox_6.tStart = t  # local t and not account for scr refresh
            textbox_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_6, 'tStartRefresh')  # time at next scr refresh
            textbox_6.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials2.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials2.addData('key_resp_3.rt', key_resp_3.rt)
    trials2.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials2.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    trials2.addData('textbox_6.started', textbox_6.tStartRefresh)
    trials2.addData('textbox_6.stopped', textbox_6.tStopRefresh)
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'


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
