#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on February 15, 2023, at 23:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
import pandas as pd
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import time
import psychopy.iohub as io
from psychopy.hardware import keyboard

# Sound initialization 
prefs.hardware['audioLib'] = ['PTB']
rewardS = sound.Sound(value='sound.wav', stopTime=0.7)
wrongS = sound.Sound(value='wrong.wav',stopTime=0.6)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'test1'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
#expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    ## THIS PATH SHOULD BE CHANGED in different machines
    originPath='C:\\Users\\hadei\\Desktop\\psychoPy\\test1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename, autoLog=False)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False

# --- Setup input devices ---
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

# --- Initialize components for Routine "WelcomeScreen" ---


### Setting up components for delay and no. of distractor select screen
textWelcom = visual.TextStim(win=win, name='textWelcom',
    text='Welcome to Match-to-sample task!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

textDelay1 = visual.TextStim(win=win, name='one',
    text='[1 second]',
    font='Open Sans',
    pos=(-0.25, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

textDelay2 = visual.TextStim(win=win, name='two',
    text='[2 seconds]',
    font='Open Sans',
    pos=(0.25, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
    
textDistractor1 = visual.TextStim(win=win, name='D-one',
    text='[1 distractor]',
    font='Open Sans',
    pos=(-0.25, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

textDistractor2 = visual.TextStim(win=win, name='D-two',
    text='[2 distractors]',
    font='Open Sans',
    pos=(0.25, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

chooseText = visual.TextStim(win=win, name='chose',
    text='Please choose a stimulus display delay from below (click)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

chooseDist = visual.TextStim(win=win, name='choseD',
    text='Please chose no. of distractors (click)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
    
mouseRespStart = event.Mouse(win=win)
x, y = [None, None]
mouseRespStart.mouseClock = core.Clock()

# --- Initialize components for Routine "trial" ---
target = visual.ImageStim(
    win=win,
    name='target', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouseResp = event.Mouse(win=win)
x, y = [None, None]
mouseResp.mouseClock = core.Clock()

# --- Initialize components for Routine "blank250" ---
textBreak250 = visual.TextStim(win=win, name='textBreak250',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "trial2" ---
imageTarg = visual.ImageStim(
    win=win,
    name='imageTarg', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
distractor = visual.ImageStim(
    win=win,
    name='distractor', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
distractor1 = visual.ImageStim(
    win=win,
    name='distractor1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
distractor2 = visual.ImageStim(
    win=win,
    name='distractor2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mouseResp2 = event.Mouse(win=win)
x, y = [None, None]
mouseResp2.mouseClock = core.Clock()

# --- Initialize components for Routine "GoodbyeScreen" ---
textGoodbye = visual.TextStim(win=win, name='textGoodbye',
    text='Goodbye!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "WelcomeScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
mouseRespStart.x = []
mouseRespStart.y = []
mouseRespStart.leftButton = []
mouseRespStart.midButton = []
mouseRespStart.rightButton = []
mouseRespStart.time = []
mouseRespStart.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
WelcomeScreenComponents = [textWelcom, mouseRespStart, textDelay2, 
                            chooseText, textDelay1,textDistractor2, textDistractor1, chooseDist]
for thisComponent in WelcomeScreenComponents:
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

ITDelay = 0
select = [False, False]
# --- Run Routine "WelcomeScreen" ---

############################################################################
# Code below allows user to choose the stimuli display delay
# which is the delay after the subject has been shown 
# a single stimuli image. Currently, there can be either a 1 or 2 second delay
# but these values can be changed in the code. (setting ITDelay)
############################################################################

while continueRoutine: #  and routineTimer.getTime() < 1.0
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcom* updates
    if textWelcom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcom.frameNStart = frameN  # exact frame index
        textWelcom.tStart = t  # local t and not account for scr refresh
        textWelcom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcom, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
#        thisExp.timestampOnFlip(win, 'textWelcom.started')
        textWelcom.setAutoDraw(True)
        
        
    if textWelcom.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textWelcom.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            textWelcom.tStop = t  # not accounting for scr refresh
            textWelcom.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
#            thisExp.timestampOnFlip(win, 'textWelcom.stopped')
            textWelcom.setAutoDraw(False)
            textDelay2.setAutoDraw(True)
            textDelay1.setAutoDraw(True)
            chooseText.setAutoDraw(True)
            
    if mouseRespStart.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseRespStart.frameNStart = frameN  # exact frame index
            mouseRespStart.tStart = t  # local t and not account for scr refresh
            mouseRespStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseRespStart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
#            thisExp.addData('mouseResp.started', t)
            mouseRespStart.status = STARTED
            mouseRespStart.mouseClock.reset()
            prevButtonState = mouseRespStart.getPressed()  # if button is down already this ISN'T a new click
    if mouseRespStart.status == STARTED:  # only update if started and not finished!
                buttons = mouseRespStart.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([textDelay2,textDelay1])
                            clickableList = [textDelay2,textDelay1]
                        except:
                            clickableList = [[textDelay2,textDelay1]]
                        for obj in clickableList:
                            if obj.contains(mouseRespStart):
                                if obj.name == "two":
                                    ITDelay = 2.0
                                    textDelay2.setAutoDraw(False)
                                    chooseText.setAutoDraw(False)
                                    textDelay1.setAutoDraw(False)
                                    textDelay2.status = FINISHED
                                    textDelay2.tStop = t  # not accounting for scr refresh
                                    textDelay2.frameNStop = frameN
                                elif obj.name == "one":
                                    ITDelay = 1.0
                                    textDelay1.setAutoDraw(False)
                                    textDelay2.setAutoDraw(False)
                                    chooseText.setAutoDraw(False)
                                    textDelay1.status = FINISHED
                                    textDelay1.tStop = t  # not accounting for scr refresh
                                    textDelay1.frameNStop = frameN
                                gotValidClick = True
                                mouseRespStart.clicked_name.append(obj.name)
                        x, y = mouseRespStart.getPos()
                        mouseRespStart.x.append(x)
                        mouseRespStart.y.append(y)
                        buttons = mouseRespStart.getPressed()
                        mouseRespStart.leftButton.append(buttons[0])
                        mouseRespStart.midButton.append(buttons[1])
                        mouseRespStart.rightButton.append(buttons[2])
                        mouseRespStart.time.append(mouseRespStart.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
        
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "WelcomeScreen" ---
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)


t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1
continueRoutine = True
mode = 0
path = ''
WelcomeScreenComponents = [textDistractor2, textDistractor1, chooseDist, mouseRespStart]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
        

#########################################################
# Code below allows users to select the number of distractors 
# that are going to be shown alongside the original stimulus image
# Currently, users can only choose 1 or 2
#########################################################

while continueRoutine: #  and routineTimer.getTime() < 1.0
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcom* updates
    if chooseDist.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        chooseDist.frameNStart = frameN  # exact frame index
        chooseDist.tStart = t  # local t and not account for scr refresh
        chooseDist.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(chooseDist, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
#        thisExp.timestampOnFlip(win, 'textWelcom.started')
        chooseDist.setAutoDraw(True)
        textDistractor2.setAutoDraw(True)
        textDistractor1.setAutoDraw(True)
            
    if mouseRespStart.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseRespStart.frameNStart = frameN  # exact frame index
            mouseRespStart.tStart = t  # local t and not account for scr refresh
            mouseRespStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseRespStart, 'tStartRefresh')  # time at next scr refresh
            mouseRespStart.status = STARTED
            mouseRespStart.mouseClock.reset()
            prevButtonState = mouseRespStart.getPressed()  # if button is down already this ISN'T a new click
    if mouseRespStart.status == STARTED:  # only update if started and not finished!
                buttons = mouseRespStart.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([textDistractor2, textDistractor1])
                            clickableList = [textDistractor2, textDistractor1]
                        except:
                            clickableList = [[textDistractor2, textDistractor1]]
                        for obj in clickableList:
                            if obj.contains(mouseRespStart):
                                if obj.name == "D-one":
                                    textDistractor2.setAutoDraw(False)
                                    textDistractor1.setAutoDraw(False)
                                    chooseDist.setAutoDraw(False)
                                    mode = 1
                                    path = 'images_200.xlsx'
                                    
                                elif obj.name == "D-two":
                                    textDistractor2.setAutoDraw(False)
                                    textDistractor1.setAutoDraw(False)
                                    chooseDist.setAutoDraw(False)
                                    mode = 2
                                    path = 'two_distractors.xlsx'
                                gotValidClick = True
                                mouseRespStart.clicked_name.append(obj.name)
                        x, y = mouseRespStart.getPos()
                        mouseRespStart.x.append(x)
                        mouseRespStart.y.append(y)
                        buttons = mouseRespStart.getPressed()
                        mouseRespStart.leftButton.append(buttons[0])
                        mouseRespStart.midButton.append(buttons[1])
                        mouseRespStart.rightButton.append(buttons[2])
                        mouseRespStart.time.append(mouseRespStart.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
        
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "WelcomeScreen" ---
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(path),
    seed=None, name='trials', autoLog=False)
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))
for thisTrial in trials: # added [:5] for five trials
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    target.setImage(target_img)
    # setup some python lists for storing info about the mouseResp
    mouseResp.x = []
    mouseResp.y = []
    mouseResp.leftButton = []
    mouseResp.midButton = []
    mouseResp.rightButton = []
    mouseResp.time = []
    mouseResp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [target, mouseResp]
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


    #######################################################################################
    # Code below just shows the subject the first image stimulus and waits for the click response
    #######################################################################################
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
#            thisExp.timestampOnFlip(win, 'target.started')
            target.setAutoDraw(True)
        # *mouseResp* updates
        if mouseResp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseResp.frameNStart = frameN  # exact frame index
            mouseResp.tStart = t  # local t and not account for scr refresh
            mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            mouseResp.status = STARTED
            mouseResp.mouseClock.reset()
            prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
        if mouseResp.status == STARTED:  # only update if started and not finished!
            buttons = mouseResp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([target,])
                        clickableList = [target,]
                    except:
                        clickableList = [[target,]]
                    for obj in clickableList:
                        if obj.contains(mouseResp):
                            ##### Play reward sound when the subject clicks on component
                            ##### Pellet dispenser code can be added around the rewardS.play() line below
                            rewardS.play()
                            clock1 = core.Clock()
                            target.setSize((0.5,0.5))
                            win.flip()
                            time.sleep(0.6)
                            while clock1.getTime() < 0.25:
                                continue
                            target.setSize((0.3,0.3))
                            gotValidClick = True
                            mouseResp.clicked_name.append(obj.name)
                    x, y = mouseResp.getPos()
                    mouseResp.x.append(x)
                    mouseResp.y.append(y)
                    buttons = mouseResp.getPressed()
                    mouseResp.leftButton.append(buttons[0])
                    mouseResp.midButton.append(buttons[1])
                    mouseResp.rightButton.append(buttons[2])
                    mouseResp.time.append(mouseResp.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
                        
                        

        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    trials.addData('mouseResp.time', mouseResp.time)
    trials.addData('mouseResp.clicked_name', mouseResp.clicked_name)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "blank250" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank250Components = [textBreak250]
    for thisComponent in blank250Components:
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
    
    # --- Run Routine "blank250" ---
    while continueRoutine and routineTimer.getTime() < 0.25:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBreak250* updates
        if textBreak250.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBreak250.frameNStart = frameN  # exact frame index
            textBreak250.tStart = t  # local t and not account for scr refresh
            textBreak250.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBreak250, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
#            thisExp.timestampOnFlip(win, 'textBreak250.started')
            textBreak250.setAutoDraw(True)
        if textBreak250.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBreak250.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                textBreak250.tStop = t  # not accounting for scr refresh
                textBreak250.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
#                thisExp.timestampOnFlip(win, 'textBreak250.stopped')
                textBreak250.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank250Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank250" ---
    for thisComponent in blank250Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)

    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.250000)


    ################################
    # Stimulus display delay that was set before
    ################################    
    cl1 = core.Clock()
    while cl1.getTime() < ITDelay: 
        continue
    # --- Prepare to start Routine "trial2" ---
    continueRoutine = True
    routineForceEnded = False

    # update component parameters for each repeat
    count = 0
    posSet = []
    pos_list = [(-0.4, 0.25), (-0.4, -0.25),(0.4, -0.25),(0.4, 0.25)]
    rand1 = randint(0,3)
    if mode == 1:   
        imageTarg.setImage(target_img)
        distractor.setImage(distractor_img)
        trial2Components = [mouseResp2,imageTarg, distractor]
        while count != 2:
            if not rand1 in posSet:
                posSet.append(rand1)
                count += 1
            else:
                rand1 = randint(0,3)
        idx = 0
        for comp in trial2Components[1:]:
            comp.pos = pos_list[posSet[idx]]
            idx+=1
    elif mode == 2: 
        imageTarg.setImage(target_img)
        distractor1.setImage(distractor1_img)
        distractor2.setImage(distractor2_img)
        trial2Components = [mouseResp2, imageTarg, distractor1, distractor2]
        while count != 3:
            if not rand1 in posSet:
                posSet.append(rand1)
                count += 1
            else:
                rand1 = randint(0,3)
        idx = 0
        for comp in trial2Components[1:]:
            comp.pos = pos_list[posSet[idx]]
            idx+=1
        
    # setup some python lists for storing info about the mouseResp2
    mouseResp2.x = []
    mouseResp2.y = []
    mouseResp2.leftButton = []
    mouseResp2.midButton = []
    mouseResp2.rightButton = []
    mouseResp2.time = []
    mouseResp2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    
    for thisComponent in trial2Components:
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
    
    # Randomizing position of image target and distractor
    
    #initialize boolean for distractor select
    distSelect = False
    # --- Run Routine "trial2" ---

    ##################################################################################
    # Code below displays the target and distractors and records subjects' responses 
    #
    # NOTE: there is a comment that points to where the pellet dispenser code should
    # be added                                                                    
    ##################################################################################

    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageTarg* updates
        if imageTarg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTarg.frameNStart = frameN  # exact frame index
            imageTarg.tStart = t  # local t and not account for scr refresh
            imageTarg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTarg, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
#            thisExp.timestampOnFlip(win, 'imageTarg.started')
            imageTarg.setAutoDraw(True)
        
        # *distractor* updates
        if mode == 1:
            if distractor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                distractor.frameNStart = frameN  # exact frame index
                distractor.tStart = t  # local t and not account for scr refresh
                distractor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(distractor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
    #            thisExp.timestampOnFlip(win, 'distractor.started')
                distractor.setAutoDraw(True)
        elif mode == 2:
            if distractor1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                distractor1.frameNStart = frameN  # exact frame index
                distractor1.tStart = t  # local t and not account for scr refresh
                distractor1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(distractor1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
    #            thisExp.timestampOnFlip(win, 'distractor.started')
                distractor1.setAutoDraw(True)
            if distractor2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                distractor2.frameNStart = frameN  # exact frame index
                distractor2.tStart = t  # local t and not account for scr refresh
                distractor2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(distractor2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
    #            thisExp.timestampOnFlip(win, 'distractor.started')
                distractor2.setAutoDraw(True)
        # *mouseResp2* updates
        if mouseResp2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseResp2.frameNStart = frameN  # exact frame index
            mouseResp2.tStart = t  # local t and not account for scr refresh
            mouseResp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseResp2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
#            thisExp.addData('mouseResp2.started', t)
            mouseResp2.status = STARTED
            mouseResp2.mouseClock.reset()
            prevButtonState = mouseResp2.getPressed()  # if button is down already this ISN'T a new click
        if mouseResp2.status == STARTED:  # only update if started and not finished!
            buttons = mouseResp2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        if mode == 1:
                            iter([imageTarg, distractor,])
                            clickableList = [imageTarg, distractor,]
                        elif mode == 2:
                            iter([imageTarg, distractor1, distractor2])
                            clickableList = [imageTarg, distractor1,distractor2]
                    except:
                        if mode == 1:
                            clickableList = [[imageTarg, distractor,]]
                        elif mode == 2:
                            clickableList = [[imageTarg, distractor1, distractor2]]
                    for obj in clickableList:
                        if obj.contains(mouseResp2):
                            if obj == imageTarg:
                                clk4 = core.Clock()
                                ##### Play reward sound when the subject response is correct
                                ##### Pellet dispenser code can be added around the rewardS.play() line below
                                rewardS.play()    
                                imageTarg.setSize((0.5,0.5))
                                win.flip()
                                time.sleep(0.97)
                                while clk4.getTime() < 0.25:
                                    continue
                                imageTarg.setSize((0.3,0.3))
                            elif (mode == 1 and obj == distractor) or (mode == 2 and (obj == distractor1 or obj == distractor2)):
                                distSelect = True
                                clock2 = core.Clock()
                                win.color = 'black'
                                if mode == 1:   
                                    distractor.setAutoDraw(False)
                                elif mode == 2:
                                    distractor1.setAutoDraw(False)
                                    distractor2.setAutoDraw(False)
                                imageTarg.setAutoDraw(False)
                                ##### Play failure sound when the subject response is wrong
                                wrongS.play()
                                time.sleep(0.6)
                                while clock2.getTime() < 1.8:
                                    win.flip()
                            if mode == 1:   
                                    distractor.setAutoDraw(False)
                            elif mode == 2:
                                    distractor1.setAutoDraw(False)
                                    distractor2.setAutoDraw(False)
                            imageTarg.setAutoDraw(False)
                            gotValidClick = True
                            mouseResp2.clicked_name.append(obj.name)
                    x, y = mouseResp2.getPos()
                    mouseResp2.x.append(x)
                    mouseResp2.y.append(y)
                    buttons = mouseResp2.getPressed()
                    mouseResp2.leftButton.append(buttons[0])
                    mouseResp2.midButton.append(buttons[1])
                    mouseResp2.rightButton.append(buttons[2])
                    mouseResp2.time.append(mouseResp2.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    ### Change window color and wait 2 seconds for next trial..
    clock3 = core.Clock()
    win.color = 'green'
    while clock3.getTime() < 2.0:
        win.flip()
    win.color = [0,0,0]
    # --- Ending Routine "trial2" ---
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('mouseResp2.time', mouseResp2.time)
    trials.addData('mouseResp2.clicked_name', mouseResp2.clicked_name)
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "GoodbyeScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
GoodbyeScreenComponents = [textGoodbye]
for thisComponent in GoodbyeScreenComponents:
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

# --- Run Routine "GoodbyeScreen" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textGoodbye* updates
    if textGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textGoodbye.frameNStart = frameN  # exact frame index
        textGoodbye.tStart = t  # local t and not account for scr refresh
        textGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textGoodbye, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
#        thisExp.timestampOnFlip(win, 'textGoodbye.started')
        textGoodbye.setAutoDraw(True)
    if textGoodbye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textGoodbye.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            textGoodbye.tStop = t  # not accounting for scr refresh
            textGoodbye.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
#            thisExp.timestampOnFlip(win, 'textGoodbye.stopped')
            textGoodbye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GoodbyeScreen" ---
for thisComponent in GoodbyeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
#df = thisExp.data.copy()
#if df:
#    print("DF found!")
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
#read the file that was just saved
df=pd.read_csv(filename+'.csv', encoding = "utf-8") 
# get rid of unneccessary columns
df2= df.drop(columns=["trials.thisN", "trials.thisIndex", "Unnamed: 14"]) 
print(df2)
#definin de2 will help you keep the original pdf

########### latestCleanDataOutput.csv contains all cleaned up trial data 
df2.to_csv('data/latestCleanDataOutput.csv', index=False)
print("allcode passed")
core.quit()





