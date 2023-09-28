

def act(robot, env, camera):
    leaf_275 = registry(env, 'leaf_275')
    MoveBot(env, robot, leaf_275, camera)
    donothing(env)
