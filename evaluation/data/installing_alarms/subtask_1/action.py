import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    alarm_tone_189 = registry(env, "fire_alarm_88")
    MoveBot(env, robot, alarm_tone_189, camera)
    donothing(env)
