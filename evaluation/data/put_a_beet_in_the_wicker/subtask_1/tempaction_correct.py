

def act(robot, env, camera):
    leafy_lawn_276 = registry(env, 'leafy-laswn')
    MoveBot(env, robot, leafy_lawn_276, camera)
    donothing(env)
