

def act(robot, env, camera):
    alarm_condition_1 = ['robot', 'nextto', 'alarm', 'condition', '1']
    MoveBot(env, robot, robot, camera)
    donothing(env)
