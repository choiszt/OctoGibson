def act(robot,env,camera):
    # Subtask 1: Move the robot to the 'alarm_tone_189' object
    alarm_tone_189 = registry(env,"alarm_tone_189")
    MoveBot(env, robot, alarm_tone_189, camera)
    donothing(env)

