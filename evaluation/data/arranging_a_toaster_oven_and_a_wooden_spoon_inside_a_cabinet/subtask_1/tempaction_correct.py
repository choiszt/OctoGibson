

def act(robot, env, camera):
    toasteroven_188 = registry(env, 'toasteroven_188')
    MoveBot(env, robot, toasteroven_188, camera)
    donothing(env)
