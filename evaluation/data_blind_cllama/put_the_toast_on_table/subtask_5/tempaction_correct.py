

def act(robot, env, camera):
    toast_150 = registry(env, 'toast_150')
    MoveBot(env, robot, toast_150, camera)
    donothing(env)
