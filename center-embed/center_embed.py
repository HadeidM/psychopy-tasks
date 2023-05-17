#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on March 29, 2023, at 17:32
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
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# setup sound 
prefs.hardware['audioLib'] = ['PTB']
rewardS = sound.Sound(value='./sound.wav')
fullRewardS = sound.Sound(value='./fullAchieve')
wrongS = sound.Sound(value='./wrong.wav',stopTime=0.6)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'untitled'  # from the Builder filename that created this script
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
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\hadei\\Desktop\\psychoPy\\center_embed\\untitled.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
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

# --- Initialize components for Routine "trial" ---
blue_circ = visual.ImageStim(
    win=win,
    name='blue_circ', 
    image='C:/Users/hadei/Desktop/psychoPy/center_embed/blue_circ.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
blue_tri = visual.ImageStim(
    win=win,
    name='blue_tri', 
    image='C:/Users/hadei/Desktop/psychoPy/center_embed/blue_tri.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
red_tri = visual.ImageStim(
    win=win,
    name='red_tri', 
    image='C:/Users/hadei/Desktop/psychoPy/center_embed/red_tri.png', mask=None, anchor='center',
    ori=0.0, pos=(0.25, 0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
red_circ = visual.ImageStim(
    win=win,
    name='red_circ', 
    image='C:/Users/hadei/Desktop/psychoPy/center_embed/red_circ.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, 0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "end_dash" ---


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc

############################################################
# The code below sets up the number of trials to train the subject
# currently, the number of reps (nReps) is set to 3, you can change it 
# to any number. for example: nReps = 200.0 [NOTE]
############################################################

trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

# set up global variables
trialNum = 0
trialSuccess = 0
firstTouch = 0
secondTouch = 0
thirdTouch = 0
import random
random.seed(2)
for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code
    clicked_list = []
    currC = 0
    trialNum += 1
    # keep track of which components have finished

    ##################################################################################################
    # Code below sets position for each stimulus at a random position out of the 4 on-screen positions
    ##################################################################################################
    trialComponents = [blue_circ, blue_tri, red_tri, red_circ, mouse]
    count = 0
    rand1 = random.randint(0,3)
    pos_list = [(-0.4, 0.25), (-0.4, -0.25),(0.4, -0.25),(0.4, 0.25)] 
    posSet = []
    while count != 4:
        if not rand1 in posSet:
            print(rand1)
            posSet.append(rand1)
            count += 1
        else:
            rand1 = random.randint(0,3)
    idx = 0
    print(posSet)
    for comp in trialComponents[:4]:
        comp.pos = pos_list[posSet[idx]]
        idx+=1
    ####################################################################################################
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
    
    clickables1 = [blue_circ, blue_tri, red_tri, red_circ]
    wrongSelect = False
    allClicks = []
    
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blue_circ* updates
        if blue_circ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_circ.frameNStart = frameN  # exact frame index
            blue_circ.tStart = t  # local t and not account for scr refresh
            blue_circ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_circ, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blue_circ.started')
            blue_circ.setAutoDraw(True)
        
        # *blue_tri* updates
        if blue_tri.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blue_tri.frameNStart = frameN  # exact frame index
            blue_tri.tStart = t  # local t and not account for scr refresh
            blue_tri.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blue_tri, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blue_tri.started')
            blue_tri.setAutoDraw(True)
        
        # *red_tri* updates
        if red_tri.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_tri.frameNStart = frameN  # exact frame index
            red_tri.tStart = t  # local t and not account for scr refresh
            red_tri.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_tri, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_tri.started')
            red_tri.setAutoDraw(True)
        
        # *red_circ* updates
        if red_circ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_circ.frameNStart = frameN  # exact frame index
            red_circ.tStart = t  # local t and not account for scr refresh
            red_circ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_circ, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_circ.started')
            red_circ.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
        # Run 'Each Frame' code from code
        ### setting up the correct sequence
        clickables = [blue_circ, blue_tri, red_tri, red_circ]
        startTime = -1
        for clickable in clickables:
            if mouse.isPressedIn(clickable):
                clock1 = core.Clock();
                #####################################################
                ## Code below checks whether the subject is following 
                ## the sequence correctly
                #####################################################
                if not wrongSelect and clickable == clickables1[currC]:
                    if currC == 0:
                        firstTouch += 1
                    elif currC == 1:
                        secondTouch += 1
                    elif currC == 2:
                        thirdTouch += 1
                    ########################
                    # Add Pellet dispenser code below
                    rewardS.play()
                    clicked_list.append(clickable.name)
                    clickable.opacity -= 0.5
                    while clock1.getTime() < 0.25:
                        win.flip()
                    clickable.opacity += 0.5
                    win.flip()
                    print(clickable.name, currC)
                    currC+=1
                    print("CurrC: ", currC)
                else:
                    wrongSelect = True
                    ##### The reward sound plays regardless of whethere the subject follows the correct sequence
                    ########################
                    # Add Pellet dispenser code below
                    rewardS.play()
                    clicked_list.append(clickable.name)
                    clickable.opacity -= 0.5
                    while clock1.getTime() < 0.25:
                        win.flip()
                    clickable.opacity += 0.5
                    win.flip()
                    print(clickable.name, currC)
                    currC+=1
                    print("CurrC: ", currC)
            
        if len(clicked_list) == 4:
            # Only count successful sequence if the subject did not mess up the sequence
            if not wrongSelect:
                trialSuccess += 1
                fullRewardS.play()
            print(clicked_list)
            allClicks.append(clicked_list)
            
            for clickable in trialComponents[:4]:
                clickable.setAutoDraw(False)
            clock3 = core.Clock()
            while clock3.getTime() < 0.8:
                win.flip()     
            for clickable in trialComponents[:4]:
                clickable.setAutoDraw(True)
            currC = 0
            clicked_list = []
            continueRoutine = False
            print("trial Num: ", trialNum)
        
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
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    thisExp.addData('mouse.clickedList', allClicks)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'trials'


# --- Prepare to start Routine "end_dash" ---

##########################################################################
# End dash screen displays the number of successful touch metrics and the no.
# of successfully completed trials. 
##########################################################################

continueRoutine = True
routineForceEnded = False
text = visual.TextStim(win=win, name='text',
    text=f'1st picture touch success rate: {firstTouch/trials.nReps * 100:.2f}%\n\n2nd picture touch success rate: {secondTouch/trials.nReps * 100:.2f}%\n\n3rd picture touch success rate: {thirdTouch/trials.nReps * 100:.2f}%\n\nNo. of successful trials: {trialSuccess} out of {trials.nReps}',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# update component parameters for each repeat
# keep track of which components have finished
end_dashComponents = [text]
for thisComponent in end_dashComponents:
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

# --- Run Routine "end_dash" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == STARTED:
        t1 = core.Clock()
        while t1.getTime() < 5.0:
            continue
        continueRoutine = False
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_dashComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_dash" ---
for thisComponent in end_dashComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end_dash" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
