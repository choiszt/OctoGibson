

def act(robot, env, camera):
    fridge = registry(env, 'fridge_xyejdx_0')
    MoveBot(camera, fridge, camera)
    donothing(env)
