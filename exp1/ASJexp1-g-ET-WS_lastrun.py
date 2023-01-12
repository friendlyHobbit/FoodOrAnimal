#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on January 12, 2023, at 18:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'FoodAnimal'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'gender': ["male" , "female", "other"],
    'Year of birth': '',
    'Do you own a pet?': ["yes", "no"],
    'Would you consider adopting a pet?': ["yes", "no"],
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
    originPath='C:\\Git\\ETH_winterschool\\FoodOrAnimal\\exp1\\ASJexp1-g-ET-WS_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
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

# Setup eyetracking
ioConfig['eyetracker.hw.gazepoint.gp3.EyeTracker'] = {
    'name': 'tracker',
    'network_settings': {
        'ip_address': '127.0.0.1',
        'port': 4242.0
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='FoodAnimal', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "startInstr" ---
welcome_instr = visual.ImageStim(
    win=win,
    name='welcome_instr', 
    image='instructions/welcome_i.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
space_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "survey" ---
survey_ques_txt = visual.TextStim(win=win, name='survey_ques_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
survey_resp = visual.Slider(win=win, name='survey_resp',
    startValue=None, size=(0.5, 0.02), pos=(0, -0.2), units=None,
    labels=["Not much at all", "Very much"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='blue', lineColor='gray', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "calib_instr" ---
calib_inst = visual.ImageStim(
    win=win,
    name='calib_inst', 
    image='instructions/calib_I.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_calib_i = keyboard.Keyboard()

# --- Initialize components for Routine "valid_instr" ---
validation_image = visual.ImageStim(
    win=win,
    name='validation_image', 
    image='instructions/valid_i.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_val = keyboard.Keyboard()

# --- Initialize components for Routine "calib_cont" ---
# Run 'Begin Experiment' code from code_calib_contr
timeout = 10

from math import atan2, degrees

h=22.2
d=57
r=1080

deg_per_px = degrees(atan2(0.5*h, d))/(0.5*r)

deg_per_hu = deg_per_px *r


calib_text = visual.TextStim(win=win, name='calib_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
calib_resp = keyboard.Keyboard()

# --- Initialize components for Routine "mainInstr" ---
space_resp = keyboard.Keyboard()
main_instr = visual.ImageStim(
    win=win,
    name='main_instr', 
    image='instructions/instr.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "task" ---
task_img = visual.ImageStim(
    win=win,
    name='task_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
space_resp_1 = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
fix_cross = visual.ShapeStim(
    win=win, name='fix_cross', vertices='cross',
    size=(0.15, 0.15),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "stim_exposure" ---
# Run 'Begin Experiment' code from code_io
#ioServer.sendMesssageEvent(text='%s' % (win.units), category='units')
etRecord = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
stim_img = visual.ImageStim(
    win=win,
    name='stim_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "task_resp" ---
task_resp_slider = visual.Slider(win=win, name='task_resp_slider',
    startValue=None, size=(1.0, 0.02), pos=(0, -0.2), units=None,
    labels=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='blue', lineColor='gray', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=0, readOnly=False)
count_ques_txt = visual.TextStim(win=win, name='count_ques_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "task_difficult" ---
diff_rate_ques = visual.TextStim(win=win, name='diff_rate_ques',
    text='How difficult was this task?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
difficult_rate_slider = visual.Slider(win=win, name='difficult_rate_slider',
    startValue=None, size=(1.0, 0.02), pos=(0, -0.2), units=None,
    labels=["Very easy", "Very difficult"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='black', markerColor='blue', lineColor='gray', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-1, readOnly=False)

# --- Initialize components for Routine "end" ---
end_img = visual.ImageStim(
    win=win,
    name='end_img', 
    image='instructions/end_i.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "startInstr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_resp_2.keys = []
space_resp_2.rt = []
_space_resp_2_allKeys = []
# keep track of which components have finished
startInstrComponents = [welcome_instr, space_resp_2]
for thisComponent in startInstrComponents:
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

# --- Run Routine "startInstr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_instr* updates
    if welcome_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_instr.frameNStart = frameN  # exact frame index
        welcome_instr.tStart = t  # local t and not account for scr refresh
        welcome_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_instr, 'tStartRefresh')  # time at next scr refresh
        welcome_instr.setAutoDraw(True)
    
    # *space_resp_2* updates
    waitOnFlip = False
    if space_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_resp_2.frameNStart = frameN  # exact frame index
        space_resp_2.tStart = t  # local t and not account for scr refresh
        space_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_resp_2, 'tStartRefresh')  # time at next scr refresh
        space_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_resp_2.clock.reset)  # t=0 on next screen flip
    if space_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = space_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _space_resp_2_allKeys.extend(theseKeys)
        if len(_space_resp_2_allKeys):
            space_resp_2.keys = _space_resp_2_allKeys[-1].name  # just the last key pressed
            space_resp_2.rt = _space_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "startInstr" ---
for thisComponent in startInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "startInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
survey_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('survey_ques.csv'),
    seed=None, name='survey_trials')
thisExp.addLoop(survey_trials)  # add the loop to the experiment
thisSurvey_trial = survey_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSurvey_trial.rgb)
if thisSurvey_trial != None:
    for paramName in thisSurvey_trial:
        exec('{} = thisSurvey_trial[paramName]'.format(paramName))

for thisSurvey_trial in survey_trials:
    currentLoop = survey_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSurvey_trial.rgb)
    if thisSurvey_trial != None:
        for paramName in thisSurvey_trial:
            exec('{} = thisSurvey_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "survey" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    survey_ques_txt.setText(surv_ques)
    survey_resp.reset()
    # keep track of which components have finished
    surveyComponents = [survey_ques_txt, survey_resp]
    for thisComponent in surveyComponents:
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
    
    # --- Run Routine "survey" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *survey_ques_txt* updates
        if survey_ques_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            survey_ques_txt.frameNStart = frameN  # exact frame index
            survey_ques_txt.tStart = t  # local t and not account for scr refresh
            survey_ques_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(survey_ques_txt, 'tStartRefresh')  # time at next scr refresh
            survey_ques_txt.setAutoDraw(True)
        
        # *survey_resp* updates
        if survey_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            survey_resp.frameNStart = frameN  # exact frame index
            survey_resp.tStart = t  # local t and not account for scr refresh
            survey_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(survey_resp, 'tStartRefresh')  # time at next scr refresh
            survey_resp.setAutoDraw(True)
        
        # Check survey_resp for response to end routine
        if survey_resp.getRating() is not None and survey_resp.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in surveyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "survey" ---
    for thisComponent in surveyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    survey_trials.addData('survey_resp.response', survey_resp.getRating())
    # the Routine "survey" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'survey_trials'


# --- Prepare to start Routine "calib_instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_calib_i.keys = []
key_resp_calib_i.rt = []
_key_resp_calib_i_allKeys = []
# keep track of which components have finished
calib_instrComponents = [calib_inst, key_resp_calib_i]
for thisComponent in calib_instrComponents:
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

# --- Run Routine "calib_instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calib_inst* updates
    if calib_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calib_inst.frameNStart = frameN  # exact frame index
        calib_inst.tStart = t  # local t and not account for scr refresh
        calib_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calib_inst, 'tStartRefresh')  # time at next scr refresh
        calib_inst.setAutoDraw(True)
    
    # *key_resp_calib_i* updates
    waitOnFlip = False
    if key_resp_calib_i.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_calib_i.frameNStart = frameN  # exact frame index
        key_resp_calib_i.tStart = t  # local t and not account for scr refresh
        key_resp_calib_i.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_calib_i, 'tStartRefresh')  # time at next scr refresh
        key_resp_calib_i.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_calib_i.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_calib_i.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_calib_i.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_calib_i.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_calib_i_allKeys.extend(theseKeys)
        if len(_key_resp_calib_i_allKeys):
            key_resp_calib_i.keys = _key_resp_calib_i_allKeys[-1].name  # just the last key pressed
            key_resp_calib_i.rt = _key_resp_calib_i_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calib_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "calib_instr" ---
for thisComponent in calib_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "calib_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
calib_loop = data.TrialHandler(nReps=timeout, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='calib_loop')
thisExp.addLoop(calib_loop)  # add the loop to the experiment
thisCalib_loop = calib_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCalib_loop.rgb)
if thisCalib_loop != None:
    for paramName in thisCalib_loop:
        exec('{} = thisCalib_loop[paramName]'.format(paramName))

for thisCalib_loop in calib_loop:
    currentLoop = calib_loop
    # abbreviate parameter names if possible (e.g. rgb = thisCalib_loop.rgb)
    if thisCalib_loop != None:
        for paramName in thisCalib_loop:
            exec('{} = thisCalib_loop[paramName]'.format(paramName))
    # define target for calibration
    calibrationTarget = visual.TargetStim(win, 
        name='calibrationTarget',
        radius=0.01, fillColor='', borderColor='black', lineWidth=1.0,
        innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=1.0,
        colorSpace='rgb', units=None
    )
    # define parameters for calibration
    calibration = hardware.eyetracker.EyetrackerCalibration(win, 
        eyetracker, calibrationTarget,
        units=None, colorSpace='rgb',
        progressMode='time', targetDur=1.5, expandScale=1.5,
        targetLayout='FIVE_POINTS', randomisePos=True, textColor='black',
        movementAnimation=True, targetDelay=1.0
    )
    # run calibration
    calibration.run()
    # clear any keypresses from during calibration so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "valid_instr" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_val.keys = []
    key_resp_val.rt = []
    _key_resp_val_allKeys = []
    # keep track of which components have finished
    valid_instrComponents = [validation_image, key_resp_val]
    for thisComponent in valid_instrComponents:
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
    
    # --- Run Routine "valid_instr" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *validation_image* updates
        if validation_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            validation_image.frameNStart = frameN  # exact frame index
            validation_image.tStart = t  # local t and not account for scr refresh
            validation_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(validation_image, 'tStartRefresh')  # time at next scr refresh
            validation_image.setAutoDraw(True)
        
        # *key_resp_val* updates
        waitOnFlip = False
        if key_resp_val.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_val.frameNStart = frameN  # exact frame index
            key_resp_val.tStart = t  # local t and not account for scr refresh
            key_resp_val.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_val, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_val.started')
            key_resp_val.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_val.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_val.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_val.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_val.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_val_allKeys.extend(theseKeys)
            if len(_key_resp_val_allKeys):
                key_resp_val.keys = _key_resp_val_allKeys[-1].name  # just the last key pressed
                key_resp_val.rt = _key_resp_val_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in valid_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "valid_instr" ---
    for thisComponent in valid_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "valid_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # define target for validation
    validationTarget = visual.TargetStim(win, 
        name='validationTarget',
        radius=0.01, fillColor='', borderColor='black', lineWidth=1.0,
        innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=1.0,
        colorSpace='rgb', units=None
    )
    # define parameters for validation
    validation = iohub.ValidationProcedure(win,
        target=validationTarget,
        gaze_cursor='green', 
        positions='FIVE_POINTS', randomize_positions=True,
        expand_scale=1.5, target_duration=1.5,
        enable_position_animation=True, target_delay=1.0,
        progress_on_key=None, text_color='black',
        show_results_screen=True, save_results_screen=True,
        color_space='rgb', unit_type=None
    )
    # run validation
    validation.run()
    # clear any keypresses from during validation so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "validation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "calib_cont" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_calib_contr
    #present validation results
    results = validation.getValidationResults()
    valid_results = "Validation Results in height units\nMin: %.4f, Max: %.4f, Mean: %.4f (%s units)\n" % \
      (results['min_error'], results['max_error'], results['mean_error'], \
       results['reporting_unit_type'])
    
    valid_results_deg = "Validation Results in degree visual angle\nMin: %.4f, Max: %.4f, Mean: %.4f" % \
      (results['min_error']*deg_per_hu, results['max_error']*deg_per_hu, results['mean_error']*deg_per_hu)
    
    calib_query = "%s\n%s\n\nRecalibrate (y/n)?" % (valid_results,valid_results_deg)
    
    calib_text.setText(calib_query)
    calib_resp.keys = []
    calib_resp.rt = []
    _calib_resp_allKeys = []
    # keep track of which components have finished
    calib_contComponents = [calib_text, calib_resp]
    for thisComponent in calib_contComponents:
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
    
    # --- Run Routine "calib_cont" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *calib_text* updates
        if calib_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calib_text.frameNStart = frameN  # exact frame index
            calib_text.tStart = t  # local t and not account for scr refresh
            calib_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calib_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calib_text.started')
            calib_text.setAutoDraw(True)
        
        # *calib_resp* updates
        waitOnFlip = False
        if calib_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calib_resp.frameNStart = frameN  # exact frame index
            calib_resp.tStart = t  # local t and not account for scr refresh
            calib_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calib_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calib_resp.started')
            calib_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(calib_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(calib_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if calib_resp.status == STARTED and not waitOnFlip:
            theseKeys = calib_resp.getKeys(keyList=['y','n'], waitRelease=False)
            _calib_resp_allKeys.extend(theseKeys)
            if len(_calib_resp_allKeys):
                calib_resp.keys = [key.name for key in _calib_resp_allKeys]  # storing all keys
                calib_resp.rt = [key.rt for key in _calib_resp_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in calib_contComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "calib_cont" ---
    for thisComponent in calib_contComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_calib_contr
    #calib_resp Keyboard component must have set Store: all keys
    if calib_resp is not None and 'n' in calib_resp.keys:
        calib_loop.finished = True
    # check responses
    if calib_resp.keys in ['', [], None]:  # No response was made
        calib_resp.keys = None
    calib_loop.addData('calib_resp.keys',calib_resp.keys)
    if calib_resp.keys != None:  # we had a response
        calib_loop.addData('calib_resp.rt', calib_resp.rt)
    # the Routine "calib_cont" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed timeout repeats of 'calib_loop'


# --- Prepare to start Routine "mainInstr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_resp.keys = []
space_resp.rt = []
_space_resp_allKeys = []
# keep track of which components have finished
mainInstrComponents = [space_resp, main_instr]
for thisComponent in mainInstrComponents:
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

# --- Run Routine "mainInstr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_resp* updates
    waitOnFlip = False
    if space_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_resp.frameNStart = frameN  # exact frame index
        space_resp.tStart = t  # local t and not account for scr refresh
        space_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_resp, 'tStartRefresh')  # time at next scr refresh
        space_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space_resp.clock.reset)  # t=0 on next screen flip
    if space_resp.status == STARTED and not waitOnFlip:
        theseKeys = space_resp.getKeys(keyList=['space'], waitRelease=False)
        _space_resp_allKeys.extend(theseKeys)
        if len(_space_resp_allKeys):
            space_resp.keys = _space_resp_allKeys[-1].name  # just the last key pressed
            space_resp.rt = _space_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *main_instr* updates
    if main_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        main_instr.frameNStart = frameN  # exact frame index
        main_instr.tStart = t  # local t and not account for scr refresh
        main_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(main_instr, 'tStartRefresh')  # time at next scr refresh
        main_instr.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mainInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mainInstr" ---
for thisComponent in mainInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "mainInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks.csv'),
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
    
    # --- Prepare to start Routine "task" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    task_img.setImage(task_inst)
    space_resp_1.keys = []
    space_resp_1.rt = []
    _space_resp_1_allKeys = []
    # keep track of which components have finished
    taskComponents = [task_img, space_resp_1]
    for thisComponent in taskComponents:
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
    
    # --- Run Routine "task" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_img* updates
        if task_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_img.frameNStart = frameN  # exact frame index
            task_img.tStart = t  # local t and not account for scr refresh
            task_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_img, 'tStartRefresh')  # time at next scr refresh
            task_img.setAutoDraw(True)
        
        # *space_resp_1* updates
        waitOnFlip = False
        if space_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_resp_1.frameNStart = frameN  # exact frame index
            space_resp_1.tStart = t  # local t and not account for scr refresh
            space_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_resp_1, 'tStartRefresh')  # time at next scr refresh
            space_resp_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_resp_1.clock.reset)  # t=0 on next screen flip
        if space_resp_1.status == STARTED and not waitOnFlip:
            theseKeys = space_resp_1.getKeys(keyList=['space'], waitRelease=False)
            _space_resp_1_allKeys.extend(theseKeys)
            if len(_space_resp_1_allKeys):
                space_resp_1.keys = _space_resp_1_allKeys[-1].name  # just the last key pressed
                space_resp_1.rt = _space_resp_1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task" ---
    for thisComponent in taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fix" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix_cross]
    for thisComponent in fixComponents:
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
    
    # --- Run Routine "fix" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_cross* updates
        if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_cross.frameNStart = frameN  # exact frame index
            fix_cross.tStart = t  # local t and not account for scr refresh
            fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
            fix_cross.setAutoDraw(True)
        if fix_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix_cross.tStop = t  # not accounting for scr refresh
                fix_cross.frameNStop = frameN  # exact frame index
                fix_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fix" ---
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "stim_exposure" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_io
    # BEGIN ROUTINE
    ioServer.sendMessageEvent(text='%s%s' % ('start:',trial_id), category = 'trial_answer')
    stim_img.setImage(stim)
    # keep track of which components have finished
    stim_exposureComponents = [etRecord, stim_img]
    for thisComponent in stim_exposureComponents:
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
    
    # --- Run Routine "stim_exposure" ---
    while continueRoutine and routineTimer.getTime() < 5.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord* updates
        if etRecord.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            etRecord.status = STARTED
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                etRecord.tStop = t  # not accounting for scr refresh
                etRecord.frameNStop = frameN  # exact frame index
                etRecord.status = FINISHED
        
        # *stim_img* updates
        if stim_img.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim_img.frameNStart = frameN  # exact frame index
            stim_img.tStart = t  # local t and not account for scr refresh
            stim_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_img, 'tStartRefresh')  # time at next scr refresh
            stim_img.setAutoDraw(True)
        if stim_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_img.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                stim_img.tStop = t  # not accounting for scr refresh
                stim_img.frameNStop = frameN  # exact frame index
                stim_img.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim_exposureComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stim_exposure" ---
    for thisComponent in stim_exposureComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_io
    # END ROUTINE
    ioServer.sendMessageEvent(text='%s%s' % ('end:',trial_id), category = 'trial_answer')
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.500000)
    
    # --- Prepare to start Routine "task_resp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    task_resp_slider.reset()
    count_ques_txt.setText(count_ques)
    # keep track of which components have finished
    task_respComponents = [task_resp_slider, count_ques_txt]
    for thisComponent in task_respComponents:
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
    
    # --- Run Routine "task_resp" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *task_resp_slider* updates
        if task_resp_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_resp_slider.frameNStart = frameN  # exact frame index
            task_resp_slider.tStart = t  # local t and not account for scr refresh
            task_resp_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_resp_slider, 'tStartRefresh')  # time at next scr refresh
            task_resp_slider.setAutoDraw(True)
        
        # Check task_resp_slider for response to end routine
        if task_resp_slider.getRating() is not None and task_resp_slider.status == STARTED:
            continueRoutine = False
        
        # *count_ques_txt* updates
        if count_ques_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            count_ques_txt.frameNStart = frameN  # exact frame index
            count_ques_txt.tStart = t  # local t and not account for scr refresh
            count_ques_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(count_ques_txt, 'tStartRefresh')  # time at next scr refresh
            count_ques_txt.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_respComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_resp" ---
    for thisComponent in task_respComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('task_resp_slider.response', task_resp_slider.getRating())
    # the Routine "task_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "task_difficult" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    difficult_rate_slider.reset()
    # keep track of which components have finished
    task_difficultComponents = [diff_rate_ques, difficult_rate_slider]
    for thisComponent in task_difficultComponents:
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
    
    # --- Run Routine "task_difficult" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *diff_rate_ques* updates
        if diff_rate_ques.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            diff_rate_ques.frameNStart = frameN  # exact frame index
            diff_rate_ques.tStart = t  # local t and not account for scr refresh
            diff_rate_ques.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(diff_rate_ques, 'tStartRefresh')  # time at next scr refresh
            diff_rate_ques.setAutoDraw(True)
        
        # *difficult_rate_slider* updates
        if difficult_rate_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            difficult_rate_slider.frameNStart = frameN  # exact frame index
            difficult_rate_slider.tStart = t  # local t and not account for scr refresh
            difficult_rate_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(difficult_rate_slider, 'tStartRefresh')  # time at next scr refresh
            difficult_rate_slider.setAutoDraw(True)
        
        # Check difficult_rate_slider for response to end routine
        if difficult_rate_slider.getRating() is not None and difficult_rate_slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_difficultComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_difficult" ---
    for thisComponent in task_difficultComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('difficult_rate_slider.response', difficult_rate_slider.getRating())
    # the Routine "task_difficult" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_img]
for thisComponent in endComponents:
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

# --- Run Routine "end" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_img* updates
    if end_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_img.frameNStart = frameN  # exact frame index
        end_img.tStart = t  # local t and not account for scr refresh
        end_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_img, 'tStartRefresh')  # time at next scr refresh
        end_img.setAutoDraw(True)
    if end_img.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_img.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            end_img.tStop = t  # not accounting for scr refresh
            end_img.frameNStop = frameN  # exact frame index
            end_img.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
