

def act(robot, env, camera):
    fridge = registry(env, 'fridge_xyejdx_0')
    MoveBot(env, robot, fridge, camera)
