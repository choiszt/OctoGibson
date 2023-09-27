

def act(robot, env, camera):
    alarm_tone_189 = registry(env, 'alarm_tone_189')
    MoveBot(env, robot, alarm_tone_189, camera)
    donothing(env)
