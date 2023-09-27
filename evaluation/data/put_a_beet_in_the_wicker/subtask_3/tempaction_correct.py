

def act(robot, env, camera):
    leafylawwn = registry(env, 'leafylashwn')
    MoveBot(env, robot, leafylawwn, camera)
    donothing(env)
